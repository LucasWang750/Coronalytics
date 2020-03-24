


def getHourAmount():
    hourAmount=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    with open('/Users/wang/Documents/GitHub/Coronalytics/name4.txt') as f:
        for line in f:
            try:
                data = line
                index = data.index('2020-03-')
                spaceIndex = data.index(' ', index)
                newTime = data[spaceIndex+1:-7]
                hourAmount[(int(newTime)-1)] += 1
            except:
                break
    with open('/Users/wang/Documents/GitHub/Coronalytics/name.txt') as f:
        for line in f:
            try:
                data = line
                index = data.index('2020-03-')
                spaceIndex = data.index(' ', index)
                newTime = data[spaceIndex+1:-7]
                hourAmount[(int(newTime)-1)] += 1
            except:
                break
    for num in range(len(hourAmount)):
        hourAmount[num] /= 3
        hourAmount[num] = int(hourAmount[num])
    return hourAmount

def getHourAmountToday(date):
    hourAmount=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    with open('/Users/wang/Documents/GitHub/Coronalytics/name4.txt') as f:
        for line in f:
            data = line
            try:
                index = data.index(date)
                spaceIndex = data.index(' ', index)
                newTime = data[spaceIndex+1:-7]
                hourAmount[(int(newTime)-1)] += 1
            except:
                hourAmount[0] += 0
    with open('/Users/wang/Documents/GitHub/Coronalytics/name.txt') as f:
        for line in f:
            data = line
            try:
                index = data.index(date)
                spaceIndex = data.index(' ', index)
                newTime = data[spaceIndex+1:-7]
                hourAmount[(int(newTime)-1)] += 1
            except:
                hourAmount[0] += 0
    return hourAmount
