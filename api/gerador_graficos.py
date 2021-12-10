from itertools import chain
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# import matplotlib.pyplot as plt, mpld3



#Objeto que representa um erro do robo
class Erro:
    def __init__(self, #id, timestamp,
                 task):
                 #, message, device, status):
        #self.id = id
        #self.timestamp = timestamp
        self.task = task
        #self.message = message
        #self.device = device
        #self.status = status

#captura todos os erros do arquivo csv
def gerar_graficos(file, file_type):
    dirRobot = [file]
    objetos = []
    erros = []
    for x in dirRobot:
        if(file_type==".csv"):
            arquivo = pd.read_csv(x)
        else:
            arquivo = pd.read_excel(x)
        for x in range(len(arquivo)):
            erro = Erro(#'{}'.format(arquivo.loc[x, 'ID']),
                        #'{}'.format(arquivo.loc[x, 'TIMESTAMP']),
                        '{}'.format(arquivo.loc[x, 'TASK']),
                        #'{}'.format(arquivo.loc[x, 'MESSAGE']),
                        #'{}'.format(arquivo.loc[x, 'DEVICE']),
                        #'{}'.format(arquivo.loc[x, 'STATUS'])
                        )
            if erro.task.strip() != 'nan':
                erros.append(erro.task.strip())
                objetos.append(erro)

    #Indentifica cada tipo de erro existente
    errosUnicos = []
    qtdaErros = {}

    for item in chain(erros):
        if item not in errosUnicos:
            errosUnicos.append(item)
            qtdaErros[item] = 1
        else: qtdaErros[item] = qtdaErros[item] + 1

    #Filtro para remover dados invalidos
    cont = 0
    for item in errosUnicos:
        if item == '' or item == 'null':
            errosUnicos.remove(item)
            del qtdaErros[item]
            cont = cont + 1
        if cont == 2: break

    dados_x = errosUnicos
    dados_x_sem_erro = []
    for x in dados_x:
        frase = x
        remover_palavras  = ["MOTN-056", "MOTN-170", "INTP-685", "SRVO-171","SYST-034", "SRVO-004",
        "SRVO-199", "SRVO-007","SRVO-012","INTP-127","SRVO-037", "PROF-017","PROF-001","SRVO-300",
        "HOST-108","SP -012","HOST-028","FILE-069","FILE-071","FILE-077","FILE-078","SRVO-105"]
        lista_frase = frase.split()
        result = [palavra for palavra in lista_frase if palavra.upper() not in remover_palavras]

        retorno = ' '.join(result)

        dados_x_sem_erro.append(retorno)
    i = 0
    for linha in dados_x_sem_erro:
        
        if(linha == "SP -012 $0038000C-Dictionary not found"):
            dados_x_sem_erro[i] = "Dictionary not found"
            
            
        if(linha == "(RETURN, 19)TIMER[4] has already been started"):
            dados_x_sem_erro[i] = "Timer[4] has already been started"
            
            
        if(linha == "(TRACKING, 47)TIMER[3] has already been started"):
            dados_x_sem_erro[i] = "TIMER[3] has already been started"
            

        if(linha == "(HANDLING, 4)TIMER[7] has already been started"):
            dados_x_sem_erro[i] = "TIMER[7] has already been started" 
             
        i = i + 1 
    #montando grafico em piza
    
    dados_y = []
    for item in errosUnicos:
        dados_y.append(qtdaErros[item])

    df = px.data.iris()
    fig = px.pie(df, names = dados_x_sem_erro, values=dados_y, title="Program Error Categories: Percentage of all errors in the robot program.")
    fig.update_traces(textposition='inside')
    fig.update_layout(width=850)
    # fig.write_html("pizza.html", auto_open=True)
    fig.write_json('allErrors.json')
    
    x_maiores = []
    y_maiores = []
    j = 0
    i = 0
    for y in dados_y:
        if(y>=1000):
            x_maiores.append(dados_x_sem_erro[j]) 
            y_maiores.append(y)
            i = i + 1
        j = j + 1
    fig2 = px.pie(df, names=x_maiores, values=y_maiores, title="Program Error Categories: Percentage of the most common seen errors in the robot program")
    fig2.update_traces(textposition='inside')
    fig2.update_layout(width=850)
    # fig2.write_html("pizza.html", auto_open=True)
    fig2.write_json("mostCommonErrors.json")
    print("gráfico gerado")

if __name__ == "__main__":
    gerar_graficos("ERROR_fanuk.xlsx")