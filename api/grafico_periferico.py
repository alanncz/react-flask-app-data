import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def gerar_graficos_perifericos(file_name):

    df = pd.read_excel(file_name)

    # Filtro para remover erros fora do padrão
    df.loc[(df['STATUS'] != 8) & (df['STATUS'] != 16) &
        (df['STATUS'] != 128) & (df['STATUS'] != 1024), 'STATUS'] = 'null'

    # Filtro 330
    df.loc[(df['PL_330_LIM_CORRENTE'] > 1), 'PL_330_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_330_SOB_INVERSOR'] > 1), 'PL_330_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_330_LIM_TORQUE'] > 1), 'PL_330_LIM_TORQUE'] = 'null'

    # Filtro 205
    df.loc[(df['PL_205_LIM_CORRENTE'] > 1), 'PL_205_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_205_SOB_INVERSOR'] > 1), 'PL_205_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_205_LIM_TORQUE'] > 1), 'PL_205_LIM_TORQUE'] = 'null'

    # Filtro 220
    df.loc[(df['PL_220_LIM_CORRENTE'] > 1), 'PL_220_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_220_SOB_INVERSOR'] > 1), 'PL_220_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_220_LIM_TORQUE'] > 1), 'PL_220_LIM_TORQUE'] = 'null'

    # Filtro 240
    df.loc[(df['PL_240_LIM_CORRENTE'] > 1), 'PL_240_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_240_SOB_INVERSOR'] > 1), 'PL_240_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_240_LIM_TORQUE'] > 1), 'PL_240_LIM_TORQUE'] = 'null'

    # Filtro 250
    df.loc[(df['PL_250_LIM_CORRENTE'] > 1), 'PL_250_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_250_SOB_INVERSOR'] > 1), 'PL_250_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_250_LIM_TORQUE'] > 1), 'PL_250_LIM_TORQUE'] = 'null'

    # Filtro 255
    df.loc[(df['PL_255_LIM_CORRENTE'] > 1), 'PL_255_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_255_SOB_INVERSOR'] > 1), 'PL_255_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_255_LIM_TORQUE'] > 1), 'PL_255_LIM_TORQUE'] = 'null'

    # Filtro 390
    df.loc[(df['PL_390_LIM_CORRENTE'] > 1), 'PL_390_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_390_SOB_INVERSOR'] > 1), 'PL_390_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_390_LIM_TORQUE'] > 1), 'PL_390_LIM_TORQUE'] = 'null'

    # Filtro 400
    df.loc[(df['PL_400_LIM_CORRENTE'] > 1), 'PL_400_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_400_SOB_INVERSOR'] > 1), 'PL_400_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_400_LIM_TORQUE'] > 1), 'PL_400_LIM_TORQUE'] = 'null'

    # Filtro 420
    df.loc[(df['PL_420_LIM_CORRENTE'] > 1), 'PL_420_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_420_SOB_INVERSOR'] > 1), 'PL_420_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_420_LIM_TORQUE'] > 1), 'PL_420_LIM_TORQUE'] = 'null'

    # Filtro 440
    df.loc[(df['PL_440_LIM_CORRENTE'] > 1), 'PL_440_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_440_SOB_INVERSOR'] > 1), 'PL_440_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_440_LIM_TORQUE'] > 1), 'PL_440_LIM_TORQUE'] = 'null'

    # Filtro 450
    df.loc[(df['PL_450_LIM_CORRENTE'] > 1), 'PL_450_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_450_SOB_INVERSOR'] > 1), 'PL_450_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_450_LIM_TORQUE'] > 1), 'PL_450_LIM_TORQUE'] = 'null'

    # Filtro 470
    df.loc[(df['PL_470_LIM_CORRENTE'] > 1), 'PL_470_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_470_SOB_INVERSOR'] > 1), 'PL_470_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_470_LIM_TORQUE'] > 1), 'PL_470_LIM_TORQUE'] = 'null'

    # Filtro 480
    df.loc[(df['PL_480_LIM_CORRENTE'] > 1), 'PL_480_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_480_SOB_INVERSOR'] > 1), 'PL_480_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_480_LIM_TORQUE'] > 1), 'PL_480_LIM_TORQUE'] = 'null'

    # Filtro 550
    df.loc[(df['PL_550_LIM_CORRENTE'] > 1), 'PL_550_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_550_SOB_INVERSOR'] > 1), 'PL_550_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_550_LIM_TORQUE'] > 1), 'PL_550_LIM_TORQUE'] = 'null'

    # Filtro 560
    df.loc[(df['PL_560_LIM_CORRENTE'] > 1), 'PL_560_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_560_SOB_INVERSOR'] > 1), 'PL_560_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_560_LIM_TORQUE'] > 1), 'PL_560_LIM_TORQUE'] = 'null'

    # Filtro 570
    df.loc[(df['PL_570_LIM_CORRENTE'] > 1), 'PL_570_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_570_SOB_INVERSOR'] > 1), 'PL_570_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_570_LIM_TORQUE'] > 1), 'PL_570_LIM_TORQUE'] = 'null'

    # Filtro 580
    df.loc[(df['PL_580_LIM_CORRENTE'] > 1), 'PL_580_LIM_CORRENTE'] = 'null'
    df.loc[(df['PL_580_SOB_INVERSOR'] > 1), 'PL_580_SOB_INVERSOR'] = 'null'
    df.loc[(df['PL_580_LIM_TORQUE'] > 1), 'PL_580_LIM_TORQUE'] = 'null'


    # Gerando gráficos
    # Figura 330
    fig_330 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_330.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_330_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_330.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_330_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_330.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_330_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_330.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_330.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_330_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_330.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_330_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_330.update_layout(
        title='Transporte de entrada - M330',
        height=1000,
        showlegend=True,
    )

    # Figura 205
    fig_205 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_205.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_205_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_205.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_205_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_205.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_205_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_205.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_205.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_205_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_205.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_205_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_205.update_layout(
        title='Transporte empurrador - M205',
        height=1000,
        showlegend=True,
    )

    # Figura 220
    fig_220 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_220.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_220_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_220.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_220_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_220.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_220_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_220.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_220.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_220_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_220.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_220_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_220.update_layout(
        title='Transportador de camadas - M220',
        height=1000,
        showlegend=True,
    )

    # Figura 240
    fig_240 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_240.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_240_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_240.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_240_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_240.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_240_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_240.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_240.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_240_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_240.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_240_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_240.update_layout(
        title='Elevador de camadas - M240',
        height=1000,
        showlegend=True,
    )

    # Figura 250
    fig_250 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_250.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_250_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_250.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_250_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_250.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_250_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_250.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_250.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_250_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_250.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_250_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_250.update_layout(
        title='Saída de camadas - M250',
        height=1000,
        showlegend=True,
    )

    # Figura 255
    fig_255 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_255.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_255_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_255.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_255_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_255.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_255_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_255.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_255.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_255_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_255.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_255_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_255.update_layout(
        title='Introdutor de folhas separadoras - M255',
        height=1000,
        showlegend=True,
    )

    # Figura 390
    fig_390 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_390.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_390_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_390.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_390_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_390.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_390_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_390.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_390.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_390_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_390.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_390_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_390.update_layout(
        title='Transporte de palete - M390',
        height=1000,
        showlegend=True,
    )

    # Figura 400
    fig_400 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_400.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_400_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_400.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_400_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_400.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_400_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_400.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_400.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_400_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_400.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_400_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_400.update_layout(
        title='Transporte de palete - M400',
        height=1000,
        showlegend=True,
    )

    # Figura 420
    fig_420 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_420.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_420_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_420.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_420_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_420.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_420_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_420.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_420.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_420_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_420.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_420_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_420.update_layout(
        title='Transporte de palete - M420',
        height=1000,
        showlegend=True,
    )

    # Figura 440
    fig_440 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_440.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_440_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_440.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_440_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_440.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_440_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_440.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_440.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_440_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_440.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_440_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_440.update_layout(
        title='Transporte de palete - M440',
        height=1000,
        showlegend=True,
    )

    # Figura 450
    fig_450 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_450.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_450_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_450.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_450_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_450.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_450_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_450.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_450.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_450_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_450.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_450_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_450.update_layout(
        title='Transporte de palete - M450',
        height=1000,
        showlegend=True,
    )

    # Figura 470
    fig_470 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_470.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_470_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_470.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_470_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_470.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_470_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_470.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_470.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_470_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_470.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_470_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_470.update_layout(
        title='Transporte de palete - M470',
        height=1000,
        showlegend=True,
    )

    # Figura 480
    fig_480 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_480.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_480_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_480.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_480_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_480.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_480_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_480.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_480.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_480_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_480.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_480_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_480.update_layout(
        title='Transporte de palete - M480',
        height=1000,
        showlegend=True,
    )

    # Figura 550
    fig_550 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_550.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_550_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_550.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_550_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_550.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_550_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_550.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_550.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_550_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_550.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_550_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_550.update_layout(
        title='Elevador do centrador de folhas - M550',
        height=1000,
        showlegend=True,
    )

    # Figura 560
    fig_560 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_560.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_560_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_560.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_560_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_560.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_560_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_560.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_560.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_560_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_560.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_560_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_560.update_layout(
        title='Transporte de depósito de paletes - M560',
        height=1000,
        showlegend=True,
    )

    # Figura 570
    fig_570 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_570.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_570_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_570.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_570_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_570.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_570_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_570.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_570.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_570_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_570.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_570_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_570.update_layout(
        title='Transporte de depósito de paletes - M570',
        height=1000,
        showlegend=True,
    )

    # Figura 580
    fig_580 = make_subplots(rows=6, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}],
                            [{"type": "scatter"}]]
                        )

    fig_580.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_580_SOB_INVERSOR"],
            mode="lines",
            name="Sob. Inversor"
        ),
        row=1, col=1
    )

    fig_580.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_580_LIM_TORQUE"],
            mode="lines",
            name="Lim. Torque"
        ),
        row=2, col=1
    )

    fig_580.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["PL_580_LIM_CORRENTE"],
            mode="lines",
            name="Lim. Corrente"
        ),
        row=3, col=1
    )

    fig_580.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['STATUS']),
            mode='markers',
            name='STATUS'
        ),
        row=4, col=1
    )

    fig_580.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_580_CORRENTE']),
            mode="lines",
            name="Corrente"
        ),
        row=5, col=1
    )

    fig_580.add_trace(
        go.Scatter(
            x=df["Time"],
            y=(df['PL_580_KW']),
            mode="lines",
            name="kW"
        ),
        row=6, col=1
    )

    fig_580.update_layout(
        title='Transporte de depósito de paletes - M580',
        height=1000,
        showlegend=True,
    )
    fig_330.write_json("fig_330.json")
    fig_205.write_json("fig_205.json")
    fig_220.write_json("fig_220.json")
    fig_240.write_json("fig_240.json")
    fig_250.write_json("fig_250.json")
    fig_255.write_json("fig_255.json")
    fig_390.write_json("fig_390.json")
    fig_400.write_json("fig_400.json")
    fig_420.write_json("fig_420.json")
    fig_440.write_json("fig_440.json")
    fig_450.write_json("fig_450.json")
    fig_470.write_json("fig_470.json")
    fig_480.write_json("fig_480.json")
    fig_550.write_json("fig_550.json")
    fig_560.write_json("fig_560.json")
    fig_570.write_json("fig_570.json")
    fig_580.write_json("fig_580.json")
    print("17 graficos gerados")

