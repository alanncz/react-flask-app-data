import pandas as pd
import plotly.graph_objects as go

def gerar_tabela(tabela, manual, file_type):
    if(file_type==".csv"):
        table = pd.read_csv(tabela)
    else:
        table = pd.read_excel(tabela)          #Abre o log de erro
    error_manual = pd.read_excel(manual)  #abre o manual de erro

    table_of_occurrences = table['TASK'].value_counts()                         #realiza a contagem dos valores e transforma em Series
    table_error = table_of_occurrences.to_frame()                               #Converte de Series para DataFrame
    table_error['Error'] = table_error.index                                    #Converte o index para uma coluna
    table_error.columns = ['Occurrence', 'Error Code']                          #Renomeia as colunas
    table_error.reset_index(drop=True, inplace=True)                            #Remove o index que é a mensagem de erro

    error_code = table_error['Error Code'].str[:9].to_frame()                   #Pega os 9 caracteres iniciais da coluna que é a mensagem de erro
    error_code['Occurrence'] = table_error['Occurrence']                        #Insere a coluna de quantidade de occorencias                      #
    error_code = error_code['Error Code'].str.replace(' ', '')                  #Remove os espaços do codigo de erro
    error_code = error_code.to_frame()                                          #Converte de Series para DataFrame
    error_code['Occurrence'] = table_error['Occurrence']                        #Inclui a tabela de occorências
    error_code = error_code.groupby(['Error Code'])                             #Agrupa os erros iguais
    error_code = error_code.sum()                                               #Soma os erros iguais
    error_code = error_code.sort_values(by=['Occurrence'], ascending=False)     #Coloca os erros de forma decrescente
    merged = pd.merge(error_code, error_manual, on='Error Code', how='left')    #faz a comparação entre as tabelas e junta elas
    merged = merged.drop(columns=['Error Type', 'Error Message'])               #Remove as colunas desnecessárias
    merged = merged[['Error Code', 'Occurrence', 'Cause', 'Remedy']]            #Ajusta a posição das colunas
    merged['Error Code'].replace('RESE', 'RESET', inplace=True)                 #Renomeia o Reset

    fig = go.Figure(data=[go.Table(                                             #Cria a tabela em plotly
        header=dict(values=list(merged.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[merged['Error Code'], merged['Occurrence'], merged['Cause'], merged['Remedy']],
                fill_color='lavender',
                align='left'))
    ])
    fig.write_json("tabela.json")                                                                  #Imprime a tabela em plotly