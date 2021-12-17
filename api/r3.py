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
def gerar_graficos_temporais_reset(filename):
    dirRobot = [filename]

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
                
    # DataStart = df.loc[0,'TIMESTAMP']
    # DataEnd = df.loc[len(df)-1,'TIMESTAMP']
    dicTime ={}



    for event in objetos:
        Hour = event.timestamp.strftime("%H")
        Hour = int(int(Hour)/2)*2
        data = event.timestamp.strftime(" %d-%b-%y " + str(Hour) + ":00:00 ")
        data = datetime.strptime(data, " %d-%b-%y %H:%M:%S ")
        # if((DataStart < data) and (data < DataEnd)):
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
    Reset["TimeStra"] = []
    Reset["Reset"] = []

    for event in groupReset:
        Reset["TimeStra"].append(event)
        Reset["Reset"].append(groupReset[event])

    dr = pd.DataFrame(data=Reset)
    LoadCapacity = {}
    LoadCapacity["Ti"] = []
    LoadCapacity["Load Capacity"] = []

    for event in groupLoadCapacity:
        LoadCapacity["Ti"].append(event)
        LoadCapacity["Load Capacity"].append(groupLoadCapacity[event])

    dlc = pd.DataFrame(data=LoadCapacity)
    MotorSpd = {}
    MotorSpd["Timestamp"] = []
    MotorSpd["Motor Speed"] = []

    for event in groupMotorSpd:
        MotorSpd["Timestamp"].append(event)
        MotorSpd["Motor Speed"].append(groupMotorSpd[event])

    dms = pd.DataFrame(data=MotorSpd)
    speedLimits = {}
    speedLimits["Time"] = []
    speedLimits["Speed Limits"] = []

    for event in groupSpeedLimits:
        speedLimits["Time"].append(event)
        speedLimits["Speed Limits"].append(groupSpeedLimits[event])

    dsl = pd.DataFrame(data=speedLimits)
    FenceOpen = {}
    FenceOpen["TimeStr"] = []
    FenceOpen["Fence Open"] = []

    for event in groupFenceOpen:
        FenceOpen["TimeStr"].append(event)
        FenceOpen["Fence Open"].append(groupFenceOpen[event])

    dfo = pd.DataFrame(data=FenceOpen)
    df = pd.concat([dr,dlc,dms,dsl,dfo], axis=1)
    erro = pd.DataFrame(df['Timestamp'])
    erro['Reset'] = df['Reset']
    erro['Load Capacity'] = df['Load Capacity']
    erro['Fence Open'] = df['Fence Open']
    erro['Speed Limits'] = df['Speed Limits']
    erro['Motor Speed'] = df['Motor Speed']
    fig = px.bar(erro, x="Timestamp", y=['Reset', 'Load Capacity', 'Fence Open', 'Speed Limits',
        'Motor Speed'], title="Wide-Form Input")

    fig.show()
    fig.write_json('Reset.json')
