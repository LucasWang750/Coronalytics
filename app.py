import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output
import readFile
import plotly.graph_objects as go

external_stylesheets = ['style.css']

currentTime = str(datetime.datetime.utcnow())

style={'text-align':'center',
        'color': 'rgba(255,255,255,0.87)',
        'margin': '0 auto',
        'padding': '0'
    }
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H1('Number of #Coronavirus Tweets at each hour of the day',style=style),
        html.Div(id='live-update-text',style={
        'text-align':'center',
        'color': 'rgba(255,255,255,0.87)',
        'margin': '0 auto',
        'padding': '0',
        'margin-top': '1em'
        }),
        dcc.Graph(id='live-update-graph',style={'margin':'1em 1em 0px'}),
        dcc.Interval(
            id='interval-component',
            interval=5*1000, # in milliseconds
            n_intervals=0
        ),
        dcc.Interval(
            id='interval-component2',
            interval=1*1000, # in milliseconds
            n_intervals=0
        ),
    ]),
    style={
        'background-color':'#24292e',
        'height': '100vh',
        'width': '100vw'
    }
)

@app.callback(Output('live-update-graph', 'figure'),
            [Input('interval-component','n_intervals')])
def update_graph_live(n):
    currentTime = str(datetime.datetime.utcnow())
    data={
        'time':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
        'timeAmount':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'timeAmountToday':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    }

    data['timeAmount'] = readFile.getHourAmount()
    data['timeAmountToday'] = readFile.getHourAmountToday(currentTime[0:10])
    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 30
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}
    
    # fig.add_trace({
    #     'x': data['time'],
    #     'y': data['timeAmount'],
    #     'type': 'bar',
    #     'name': 'Average Tweets from last 3 days',
    #     'text': data['timeAmount'],
    #     'textposition':'outside',
    #     'marker_color':'blue'
    # },1,1)

    # fig.add_trace({
    #     'x': data['time'],
    #     'y': data['timeAmountToday'],
    #     'type': 'bar',
    #     'name': 'Tweets from today',
    #     'text': data['timeAmountToday'],
    #     'textposition':'outside',
    #     'marker_color':'indianred'
    # },1,1)


    fig.add_trace(go.Bar(
        x=data['time'],
        y = data['timeAmount'],
        name = 'Average Tweets from last 3 days',
        marker_color = 'rgb(55, 83, 109)',
        text = data['timeAmount'],
        textposition = 'outside'
    ))

    fig.add_trace(go.Bar(
        x=data['time'],
        y = data['timeAmountToday'],
        name = 'Tweets from today',
        marker_color = 'rgb(26, 118, 255)',
        text = data['timeAmountToday'],
        textposition = 'outside'
    ))

    # fig.add_trace(go.Scatter(x=data['time'], y=data['timeAmount'], 
    #                      line=dict(color='firebrick', width=4)))

    fig.update_layout(
 #       title = 'Twitter',
        xaxis=dict(
        title='Hour during day',
        titlefont_size=16,
        tickfont_size=14,
        ),
        yaxis=dict(
        title='Tweets',
        titlefont_size=16,
        tickfont_size=14,
        ),
        legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode = 'group',
        bargap = 0.15,
        bargroupgap = 0.1
    )

    return fig
    
@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component2', 'n_intervals')])
def update_metrics(n):
    currentTime = str(datetime.datetime.utcnow())
    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('Current Time(UTC): ' + currentTime[11:19], style=style)
        #html.Span('Amount: ' + str(read.getHourAmount()[int(currentTime[11:13])-1]), style=style),
    ]

if __name__ == '__main__':
    app.run_server(debug=True)