import plotly.express as px
import plotly.graph_objects as go

us = 0
uk = 0
mexico = 0
france = 0
italy = 0
china = 0
russia = 0

labels = ['USA','UK','mexico','france','italy','china','russia']

file = open("location.txt")

for line in file:
    if ("China" in file):
        china += 1 
    elif ("France" in file):
        france += 1
    elif ("Russia" in file):
        russia += 1
    elif ("Italy" in file):
        italy += 1
    elif ("Mexico" in file):
        mexico += 1
    elif ("US" or "USA" in file):
        us += 1
    elif ("UK" in file):
        uk += 1
    
values = [us, uk, mexico, france, italy, china, russia]


fig.update_layout(title_text='Coronavirus Location Pie Chart')
fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                             insidetextorientation='radial'
                            )])
fig.show()