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
    if "en" in line:
        english += 1
    elif "fr" in line:
        french += 1
    elif "es" in line:
        spanish += 1
    elif "tr" in line:
        turkish += 1
    elif "it" in line:
        italian += 1
    elif "pt" in line:
        portuguese += 1

    
values = [english, french, spanish, turkish, italian, portuguese]



#fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',insidetextorientation='radial')])
#fig.update_layout(title_text='Coronavirus Language Pie Chart')
#fig.show()
