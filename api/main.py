""" from gerador_graficos import gerar_graficos
from pymongo import MongoClient
import pandas as pd
import os
import pymongo as py
import json
import http.server
import socketserver
import webbrowser
import gridfs
 """
#______________________________________arquivo usado para debugar______________________________________________

#____________________________________________Download________________________________________________________

# data = db.fs.files.find_one({'filename': name})
# my_id = data['_id']
# outputdata = fs.get(my_id).read()
# download_location = "/home/analaura/Área de Trabalho/ERROR_fanuk.xlsx"
# output = open(download_location, "wb")
# output.write(outputdata)
# output.close()
#____________________________________________Parte de gerar graficos_________________________________________
# arquivo = "ERROR_fanuk.xlsx"
# gerar_graficos(arquivo)

# class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == '/':
#             self.path = '/index.html'
#         return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Handler = MyRequestHandler

# server = socketserver.TCPServer(('0.0.0.0', 3333), Handler)
# webbrowser.open('http://localhost:3333/')
# server.serve_forever()