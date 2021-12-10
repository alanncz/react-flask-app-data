from pymongo import MongoClient
import gridfs

def fazer_upload(fileName):
    
    client = MongoClient("mongodb://newplatformdb:9TXjuzqgZX8EUFcLojLX0TxZ1hxORdsbhdBdBjAs3aOyMTLNQ8Gy5UaU52AVayHipVipGuYw2EfJXcezmzD5Mw==@newplatformdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@newplatformdb@")
    #acessa o banco de dados robodatabase
    db = client.get_database('robodatabase')
    name = fileName #nome do arquivo que vai ser feito o upload
    file_location = name #caminho do arquivo
    file_data = open(file_location, "rb") #le o arquivo
    data = file_data.read() 
    fs = gridfs.GridFS(db) 
    fs.put(data, filename = name)#faz upload para o banco de dados 
    print("sucsses upload")
    print(db.list_collection_names())

def fazer_upload_perifericos(fileName):
    
    client = MongoClient("mongodb://newplatformdb:9TXjuzqgZX8EUFcLojLX0TxZ1hxORdsbhdBdBjAs3aOyMTLNQ8Gy5UaU52AVayHipVipGuYw2EfJXcezmzD5Mw==@newplatformdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@newplatformdb@")
    #acessa o banco de dados robodatabase
    db = client.get_database('perifericodatabase')
    name = fileName #nome do arquivo que vai ser feito o upload
    file_location = name #caminho do arquivo
    file_data = open(file_location, "rb") #le o arquivo
    data = file_data.read() 
    fs = gridfs.GridFS(db) 
    fs.put(data, filename = name)#faz upload para o banco de dados 
    print("sucsses upload")
