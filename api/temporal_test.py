from itertools import chain
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import timedelta
from datetime import datetime
import time

#Objeto que representa um erro do robo
class Erro:
    def __init__(self, timestamp, task):
        self.timestamp = timestamp
        self.task = task

#captura todos os erros do arquivo csv
# dirRobot = ['errors_fanuc_new.xlsx']
def graficos_temporais(file_name):
    dirRobot = [file_name]

    objetos = []
    groupEvents = dict()
    groupReset = dict()
    groupLoadCapacity = dict()
    groupSpeedLimits = dict()
    groupMotorSpd = dict()
    groupFenceOpen = dict()

    dicTime = {}

    reset = {}

    for x in dirRobot:
        arquivo = pd.read_csv(x)
        for x in range(len(arquivo)):
            erro = Erro('{}'.format(arquivo.loc[x, 'TIMESTAMP']), '{}'.format(arquivo.loc[x, 'TASK']))
            if not(erro.timestamp == 'nan'): 
                erro.timestamp = datetime.strptime(erro.timestamp, " %d-%b-%y %H:%M:%S ")
                objetos.append(erro)
                
    DataStart = datetime(2021, 11, 14, 00,00,00)
    print("dataStart: ",DataStart.strftime("%d-%b-%y %H:%M:%S"))
    DataEnd = datetime(2021, 12, 2, 00,00,00)
    print("dataStart: ",DataEnd.strftime("%d-%b-%y %H:%M:%S"))



    for event in objetos:
        minutos = event.timestamp.strftime("%M")
        minutos = int(int(minutos)/10)*10
        data = event.timestamp.strftime(" %d-%b-%y %H:" + str(minutos) + ":00 ")
        data = datetime.strptime(data, " %d-%b-%y %H:%M:%S ")
        if((DataStart < data) and (data < DataEnd)):
            if data in dicTime.keys():
                dicTime[data].append(event)
            else:
                dicTime[data] = []
                dicTime[data].append(event)

    for key in sorted(dicTime.keys()):
        groupEvents[key] = len(dicTime[key])
        errosReset = 0
        loadCapacity = 0
        speedLimits = 0
        MotorSpd = 0
        FenceOpen = 0


        for erro in dicTime[key]:
            if(erro.task == " R E S E T                                         "):
                errosReset += 1
            elif(erro.task == " MOTN-170 Load is close to capacity                "):
                loadCapacity += 1
            elif(erro.task == " MOTN-056 Speed limits used (G:1)                  "):
                speedLimits += 1
            elif(erro.task == " SRVO-171 MotorSpd lim/DVC(G:1 A:6)                "):
                MotorSpd += 1
            elif(erro.task == " SRVO-004 Fence open                               "):
                FenceOpen += 1
            
        groupReset[key]= errosReset
        groupLoadCapacity[key]= loadCapacity
        groupSpeedLimits[key]= speedLimits
        groupMotorSpd[key]= MotorSpd
        groupFenceOpen[key]= FenceOpen

    Reset = {}
    Reset["TimeStrap"] = []
    Reset["Erros"] = []

    for event in groupReset:
        Reset["TimeStrap"].append(event)
        Reset["Erros"].append(groupReset[event])

    dr = pd.DataFrame(data=Reset)
    fig = px.line(dr, x="TimeStrap", y="Erros", title="Reset x Time") 
    fig.write_json('Reset.json')

    LoadCapacity = {}
    LoadCapacity["TimeStrap"] = []
    LoadCapacity["Erros"] = []

    for event in groupLoadCapacity:
        LoadCapacity["TimeStrap"].append(event)
        LoadCapacity["Erros"].append(groupLoadCapacity[event])

    dlc = pd.DataFrame(data=LoadCapacity)
    fig = px.line(dlc, x="TimeStrap", y="Erros", title="Load Capacity x Time") 
    fig.write_json('LoadCapacity.json')

    MotorSpd = {}
    MotorSpd["TimeStrap"] = []
    MotorSpd["Erros"] = []

    for event in groupMotorSpd:
        MotorSpd["TimeStrap"].append(event)
        MotorSpd["Erros"].append(groupMotorSpd[event])

    dms = pd.DataFrame(data=MotorSpd)
    fig = px.line(dms, x="TimeStrap", y="Erros", title="MotorSpd x Time") 
    fig.write_json('MotorSpd.json')

    speedLimits = {}
    speedLimits["TimeStrap"] = []
    speedLimits["Erros"] = []

    for event in groupSpeedLimits:
        speedLimits["TimeStrap"].append(event)
        speedLimits["Erros"].append(groupSpeedLimits[event])

    dsl = pd.DataFrame(data=speedLimits)
    fig = px.line(dsl, x="TimeStrap", y="Erros", title="Speed Limits x Time") 
    fig.write_json('speedLimits.json')

    FenceOpen = {}
    FenceOpen["TimeStrap"] = []
    FenceOpen["Erros"] = []

    for event in groupFenceOpen:
        FenceOpen["TimeStrap"].append(event)
        FenceOpen["Erros"].append(groupFenceOpen[event])

    dsl = pd.DataFrame(data=FenceOpen)
    fig = px.line(dsl, x="TimeStrap", y="Erros", title="Fence Open x Time") 
    fig.write_json('FenceOpen.json')

    d = {}
    d["TimeStrap"] = []
    d["Erros"] = []

    for event in groupEvents:
        d["TimeStrap"].append(event)
        d["Erros"].append(groupEvents[event])

    df = pd.DataFrame(data=d)
    fig = px.line(df, x="TimeStrap", y="Erros", title="Erros x Time") 
    fig.write_json('Erros.json')