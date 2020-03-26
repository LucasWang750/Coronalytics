import plotly.express as px
import plotly.graph_objects as go

english = 0
french = 0
spanish = 0
turkish = 0
italian = 0
portuguese = 0

labels = ['english','french','spanish','turkish','italian','portuguese']

file = open("language.txt")

for line in file:
    if (line == "en"):
        english += 1
    else if(line == "fr"):
        french += 1
    else if(line == "es"):
        spanish += 1
    else if(line == "tr"):
        turkish += 1
    else if(line == "it"):
        italian += 1
    else if(line == "pt"):
        portuguese += 1
    
values = [english, french, spanish, turkish, italian, portuguese]


fig.update_layout(title_text='Coronavirus Language Pie Chart')
fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                             insidetextorientation='radial'
                            )])
fig.show()