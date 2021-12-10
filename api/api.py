
from flask import json, request, Flask, jsonify
from flask.templating import render_template
import upload_mongo
import os
from werkzeug.utils import secure_filename
import gerador_graficos
from pymongo import MongoClient 
import generate_table
from flask_cors import CORS

client = MongoClient("mongodb://newplatformdb:9TXjuzqgZX8EUFcLojLX0TxZ1hxORdsbhdBdBjAs3aOyMTLNQ8Gy5UaU52AVayHipVipGuYw2EfJXcezmzD5Mw==@newplatformdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@newplatformdb@")
db = client.get_database('robodatabase')

app = Flask(__name__, template_folder='templates', static_folder='static')
context = ('web.crt', 'web.key')
app.run('0.0.0.0', debug=True, port=5000, ssl_context='adhoc')
ALLOWED_EXTENSIONS = set(['.xlsx', '.csv'])
UPLOAD_FOLDER = ''
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)
@app.route('/graficos-relatorio', methods=['GET'])

def relatorio():
    try:
        allError = open('allErrors.json')
        tabela = open('tabela.json')
        mostCommom = open('mostCommonErrors.json')
        return jsonify({'files' : [json.load(allError),
            json.load(tabela),
            json.load(mostCommom)]})
    except:
        return "grafico ainda não foi gerado"


@app.route('/upload', methods=['POST'])
def upload():
    # try:
        print("POST recebido")
        file = request.files['inputFile']
        filename = secure_filename(file.filename)
        file_type = os.path.splitext(filename)[1]
        print(file_type)
        if(file_type not in app.config['ALLOWED_EXTENSIONS']):
            print("invalid type 400")
            return "invalid type", 400
        else:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("arquivo salvo")
            # upload_mongo.fazer_upload(file.filename)
            gerador_graficos.gerar_graficos(file.filename, file_type)

            generate_table.gerar_tabela(file.filename, "error_manual.xlsx", file_type)
            print("tabela gerada")
            print("Success")
            return "O gráfico foi gerado"
    # except:
        # return "erro na api"

@app.route('/upload-perifericos', methods=['POST'])
def upload_perifericos():
    print("POST periferico recebido")
    file = request.files['inputFilePeriferico']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # upload_mongo.fazer_upload_perifericos(file.filename)
    return "Arquivo perifericos salvo"

@app.route('/get_files', methods=['GET'])
def get_files():
    files = db['fs.files']
    dic = {}
    count=1
    for x in  files.find({}):
        x['_id']=count
        dic[count] = x
        count+=1
    return jsonify(dic)

@app.route('/files_defined/<int:valor>', methods=['GET'])
def files_defined(valor):
    files = db['fs.files']
    a = files.find({})[valor-1]
    a['_id'] = valor
    return {valor: a}

@app.route('/delete_file/<int:valor>', methods=['GET'])
def delete_file(valor):
    files = db['fs.files']

    a = files.find({})[valor-1]['_id']

    files.delete_one({'_id': a})
    return "Deletado com sucesso"

@app.after_request
def after_request(response):
    header = response.headers
    header['Acess-Control-Allow-Origin'] = '*'
    return response
