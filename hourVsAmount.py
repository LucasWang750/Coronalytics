import plotly.express as px
import plotly.graph_objects as go
import time as Time

time=[]
username=[]
date=[]
fig = None

hourAmount=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hour = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
#Katja / 2020-03-19 06:06:00 example line from file
def getData():
    readFile('name.txt')
    readFile('name3.txt')

#print(date)
#print(username)
#print(hourAmount)

#fig = go.Figure(data=[go.Bar(x=x, y=y,
#            hovertext=['27% market share', '24% market share', '19% market share'])])

def readFile(file):
    with open(file) as f:
        for line in f:
            data = line
            index = data.index('2020-03-')
            spaceIndex = data.index(' ', index)
            newData = data[0:index-3]
            newDate = data[index:spaceIndex]
            newTime = data[spaceIndex+1:-7]
            hourAmount[(int(newTime)-1)-7] += 1
            date.append(newDate)
            username.append(newData)
            time.append(newTime)


getData()
fig = go.Figure(data=[go.Bar(x=hour, y=hourAmount)], layout_title_text='Amount of Tweets vs. Hour for coronavirus')
fig.show()

while True:  
    getData()
    #print(hourAmount)
    fig = go.Figure(data=[go.Bar(x=hour, y=hourAmount)], layout_title_text='Amount of Tweets vs. Hour for coronavirus')
    fig.update()
