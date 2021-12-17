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
def gerar_graficos_temporais(filename):
    print('graficos wagner')
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
            # print(erro.timestamp)
            if not(erro.timestamp == 'nan'): 
                erro.timestamp = datetime.strptime(erro.timestamp, " %d-%b-%y %H:%M:%S ")
                objetos.append(erro)
                
    # DataStart = datetime(2021, 10, 29, 00,00,00)
    # print("dataStart: ",DataStart.strftime("%d-%b-%y %H:%M:%S"))
    # DataEnd = datetime(2021, 10, 30, 23,59,59)
    # DataEnd = datetime(2021, 12, 7, 23,59,59)
    # print("dataStart: ",DataEnd.strftime("%d-%b-%y %H:%M:%S"))



    for event in objetos:
        # De Minutos em Minutos
        # minutos = event.timestamp.strftime("%M")
        # minutos = int(int(minutos)/10)*10
        # data = event.timestamp.strftime(" %d-%b-%y %H:" + str(minutos) + ":00 ")
        # data = datetime.strptime(data, " %d-%b-%y %H:%M:%S ")
        
        # De Hora em Hora
        Hour = event.timestamp.strftime("%H")
        Hour = int(int(Hour)/1)*1
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
    Reset["TIMESTAMP (groups of 1h)"] = []
    Reset["Resets"] = []

    for event in groupReset:
        Reset["TIMESTAMP (groups of 1h)"].append(event)
        Reset["Resets"].append(groupReset[event])

    """ dr = pd.DataFrame(data=Reset)
    fig = px.line(dr, x="TIMESTAMP (groups of 1h)", y="Resets", title="R E S E T") 
    # fig.show()
    fig.write_json('Reset.json') """

    LoadCapacity = {}
    LoadCapacity["TIMESTAMP (groups of 1h)"] = []
    LoadCapacity["Load Capacity"] = []

    for event in groupLoadCapacity:
        LoadCapacity["TIMESTAMP (groups of 1h)"].append(event)
        LoadCapacity["Load Capacity"].append(groupLoadCapacity[event])

    dlc = pd.DataFrame(data=LoadCapacity)
    fig = px.line(dlc, x="TIMESTAMP (groups of 1h)", y="Load Capacity", title="MOTN-170 Load is close to capacity") 
    # fig.show()
    
    fig.write_json('LoadCapacity.json')
    print('salvou loadcapacity')
    MotorSpd = {}
    MotorSpd["TIMESTAMP (groups of 1h)"] = []
    MotorSpd["Motor SPD"] = []

    for event in groupMotorSpd:
        MotorSpd["TIMESTAMP (groups of 1h)"].append(event)
        MotorSpd["Motor SPD"].append(groupMotorSpd[event])

    dms = pd.DataFrame(data=MotorSpd)
    fig = px.line(dms, x="TIMESTAMP (groups of 1h)", y="Motor SPD", title="SRVO-171 MotorSpd lim/DVC(G:1 A:6)") 
    # fig.show()
    fig.write_json('MotorSpd.json')
    print('salvou motorspd')
    speedLimits = {}
    speedLimits["TIMESTAMP (groups of 1h)"] = []
    speedLimits["Speed Limits"] = []

    for event in groupSpeedLimits:
        speedLimits["TIMESTAMP (groups of 1h)"].append(event)
        speedLimits["Speed Limits"].append(groupSpeedLimits[event])

    dsl = pd.DataFrame(data=speedLimits)
    fig = px.line(dsl, x="TIMESTAMP (groups of 1h)", y="Speed Limits", title="MOTN-056 Speed limits used (G:1)") 
    # fig.show()
    fig.write_json('speedLimits.json')
    print('speedlimits')

    FenceOpen = {}
    FenceOpen["TIMESTAMP (groups of 1h)"] = []
    FenceOpen["Fence Open"] = []

    for event in groupFenceOpen:
        FenceOpen["TIMESTAMP (groups of 1h)"].append(event)
        FenceOpen["Fence Open"].append(groupFenceOpen[event])

    dsl = pd.DataFrame(data=FenceOpen)
    fig = px.line(dsl, x="TIMESTAMP (groups of 1h)", y="Fence Open", title="SRVO-004 Fence open") 
    # fig.show()
    fig.write_json('FenceOpen.json')
    print('salvou fenceopen')

    # d = {}
    # d["TIMESTAMP"] = []
    # d["Erros"] = []

    # for event in groupEvents:
    #     d["TIMESTAMP"].append(event)
    #     d["Erros"].append(groupEvents[event])

    # df = pd.DataFrame(data=d)
    # fig = px.line(df, x="TIMESTAMP", y="Erros", title="Erros x Time") 
    
    # fig.write_json('Erros.json')