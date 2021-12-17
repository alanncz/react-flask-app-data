
from r3 import gerar_graficos_temporais_reset
from temporal_pronto import gerar_graficos_temporais

from grafico_periferico import gerar_graficos_perifericos
from flask import json, request, Flask, jsonify
import upload_mongo
import os
from werkzeug.utils import secure_filename
import gerador_graficos
import generate_table
from flask_cors import CORS
from pymongo import MongoClient



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
    
    allError = open('allErrors.json')
    tabela = open('tabela.json')
    mostCommom = open('mostCommonErrors.json')   
    
    print("retornou todos os graficos")

    return jsonify({'files' : [json.load(allError), json.load(tabela), json.load(mostCommom)]})
""" except: 
            print("nao retornou os perifericos")
            return jsonify({'files' : [json.load(allError), json.load(tabela), json.load(mostCommom)]})
    except:
        print("erro")
        return "There is no graphic"
"""
@app.route('/graficos-relatorio-temporais', methods=['GET'])
def return_graficos_temporais():
    reset = open('Reset.json')
    load_capacity = open('LoadCapacity.json')
    motorSpd = open('MotorSpd.json')
    
    return jsonify({'files':[json.load(reset), json.load(load_capacity), json.load(motorSpd) 
    ]})

@app.route('/graficos-relatorio-temporais2')
def return_graficos_temporais2():
    speed_limits = open('speedLimits.json')
    fence_open = open('FenceOpen.json')
    

    return jsonify({'files': [json.load(speed_limits), json.load(fence_open)]})
    
@app.route('/graficos-relatorio-perifericos')
def return_perifericos():
    figura330 = open('fig_330.json')
  #  figura205 = open('fig_205.json')
   # figura220 = open("fig_220.json")
    #figura240 = open("fig_240.json")
    figura250 = open("fig_250.json")
    #figura255 = open("fig_255.json")
    figura390 = open("fig_390.json")
    #figura400 = open("fig_400.json")
    #figura420 = open("fig_420.json")
    
   
    return jsonify({'files' : [json.load(figura330),json.load(figura250), json.load(figura390)]})
"""
@app.route('/graficos-relatorio-perifericos2')
def return_perifericos2():
    figura440 = open("fig_440.json")
    figura450 = open("fig_450.json")
    figura470 = open("fig_470.json")
    figura480 = open("fig_480.json")
    figura550 = open("fig_550.json")
    figura560 = open("fig_560.json")
    figura570 = open("fig_570.json")
    figura580 = open("fig_580.json")
    return jsonify({'files' : [json.load(figura440),json.load(figura450),json.load(figura470),
    json.load(figura480), json.load(figura550), json.load(figura560), json.load(figura570),
    json.load(figura580)]})
"""
@app.route('/upload', methods=['POST'])
def upload():
     
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
        gerar_graficos_temporais(file.filename)
        gerar_graficos_temporais_reset(file.filename)
        print("tabela gerada")
        print("Success")
        return "O gráfico foi gerado"
     

@app.route('/upload-perifericos', methods=['POST'])
def upload_perifericos():
    file = request.files['inputFilePeriferico']
    filename = secure_filename(file.filename)
    file_type = os.path.splitext(filename)[1]
    if(file_type not in app.config['ALLOWED_EXTENSIONS']):
        print("invalid type 400")
        return "invalid type", 400
    else:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        gerar_graficos_perifericos(filename)
        # upload_mongo.fazer_upload_perifericos(file.filename)
        return "Graficos perifericos gerados"
    
    
    
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
