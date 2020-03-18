import plotly.express as px
time=[]
username=[]
date=[]


with open('wow.txt') as f:
    for line in f:
        data = line


        index = data.index('2020-0')
        spaceIndex = data.index(' ', index)
        newData = data[0:index-3]
        newDate = data[index:spaceIndex]
        newTime = data[spaceIndex+1:-1]

        # print(newData)
        # print(newDate)
        # print(newTime)
        date.append(newDate)
        username.append(newData) 
        time.append(newTime)
#print(date)
#print(username)
fig = px.scatter(date, time)
fig.show()