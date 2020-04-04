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
    if ("China" in line):
        china += 1 
    elif ("France" in line):
        france += 1
    elif ("Russia" in line):
        russia += 1
    elif ("Italy" in line):
        italy += 1
    elif ("Mexico" in line):
        mexico += 1
    elif ("US" or "USA" in line):
        us += 1
    elif ("UK" in line):
        uk += 1

file.close()
values = [us, uk, mexico, france, italy, china, russia]



#fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
#                             insidetextorientation='radial'
   #                         )])
#fig.update_layout(title_text='Coronavirus Location Pie Chart')
#fig.show()
