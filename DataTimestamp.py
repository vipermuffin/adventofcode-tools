import json
import sys
from datetime import datetime
#Class to store Programmer info
#This relies on DownloadPrivateBoard.py to download data locally
class Star:
    def __init__(self,name,day,part,timestamp):
        self.name = name
        self.day = int(day)
        self.part = int(part)
        self.ts = datetime.fromtimestamp(int(timestamp))
        
    def __repr__(self):
        return repr((self.day,self.part,self.ts.strftime("%m/%d/%Y, %H:%M:%S"),self.name))

class Coder:
    def __init__(self, name, score, stars):
        self.name = name
        self.score = score
        self.stars = stars

    def __repr__(self):
        return repr((self.name, self.score, self.stars))

    def toString(self):
        output = '(' + '{:04}'.format(self.score) + ':' + '{:02}'.format(self.stars) + ') ' + self.name
        return output
    
    def boardStr(self):
        output = self.name
        output += (25 - len(output)) * '.' + ' '
        output += str(self.score)
        output += (30 - len(output)) * ' '
        output += '*' * self.stars
        return output

year = '2021'
if len(sys.argv) >= 2:
    year = sys.argv[1]
with open('{}_jsonData.json'.format(year)) as jsonDataFile:
    #Read in the current leaderboard data
    data = json.load(jsonDataFile)
    members = data['members']
    coders = []
    starList = []
    for member in members:
        if(members[member]['local_score'] > 0):
            c = Coder(members[member]['name'], members[member]['local_score'], members[member]['stars'])
            coders.append(c)
            dt = datetime.fromtimestamp(int(members[member]['last_star_ts']))
            print(c.name + ' ' + dt.strftime("%m/%d/%Y, %H:%M:%S"))
            
            for starDay in members[member]['completion_day_level']:
                for starPart in members[member]['completion_day_level'][starDay]:
                    s = Star(members[member]['name'],starDay,starPart,members[member]['completion_day_level'][starDay][starPart]['get_star_ts'])
                    starList.append(s)
    sortedC = sorted(coders, key=lambda coder: (coder.score,coder.stars,coder.name), reverse=True)
    sortedSL = sorted(starList, key=lambda star: (star.day,star.ts))
    maxDay = max(sortedSL, key=lambda star : (star.day))
    print(maxDay.day)
    for d in range(1,maxDay.day+1):
        print("\n\n------------------")
        print(str.format("Report for Day {}",d))
        print("------------------")
        lastStar = None
        for star in sortedSL:
            if star.day == d:
                if(lastStar == None):
                    print(str.format("{} - {}:{}",star.ts,star.name,star.part))
                else:
                    print(str.format("{} - {}:{} (+{})",star.ts,star.name,star.part,star.ts - lastStar.ts))
                lastStar = star
