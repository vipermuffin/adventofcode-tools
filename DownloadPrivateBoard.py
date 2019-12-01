#!/usr/bin/env python3
import requests
import json
import subprocess
import os
import sys

# Import the email modules we'll need
from email.message import EmailMessage
import smtplib

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("Login info is kept in secrets.py, please add them there!")
    print("secrets = {")
    print("   'email' : '<sending email>',")
    print("   'email_rcvr' : '<receiving email>',")
    print("   'email_password' : '<sending email password>',")
    print("   'leaderboard_url' : '<unique id>.json', #not the full url, just the last piece")
    print("   'session_token' : '<login cookie>', #login session to Advent of Code in order to download leaderboard")
    print("   'smtp_server' : '<sending email server>',")
    print("}")
    
    raise

year = '2019'
if len(sys.argv) >= 2:
    year = sys.argv[1]
LdrBrd_url = 'https://adventofcode.com/{}/leaderboard/private/view/{}'.format(year,secrets['leaderboard_url'])
session = dict(session=secrets['session_token'])
resultsFile = 'current{}_results.txt'.format(year)
prevResults = 'previous{}_results.txt'.format(year)

#Class to store Programmer info
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

r = requests.get(LdrBrd_url,cookies=session)
data = r.json()

members = data['members']
coders = []
for member in members:
    if(members[member]['local_score'] > 0):
        c = Coder(members[member]['name'], members[member]['local_score'], members[member]['stars'])
        coders.append(c)
sortedC = sorted(coders, key=lambda coder: (coder.score,coder.stars,coder.name), reverse=True)

try:
    os.stat(resultsFile)
    os.stat(prevResults)
    from shutil import copyfile
    copyfile(resultsFile,prevResults)
except:
    print('Files not found')
    cmd = 'touch {} {}'.format(prevResults,resultsFile)
    os.system(cmd)

with open(resultsFile,"w+") as fp:
    msgStr = ""
    for c in sortedC:
        print(c.toString(),file=fp)
        msgStr += c.toString()+"\n"
    fp.close()
    
    out = subprocess.Popen(['diff',prevResults,resultsFile],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdStr = out.communicate()[0].decode("utf-8")

    if stdStr.strip():
        msgStr = stdStr + '\n------------------------------------\n\n' + msgStr
        msg = EmailMessage()
        msg.set_content(msgStr)
        msg['Subject'] = 'AoC Update {}'.format(year)
        msg['From'] = secrets['email']
        msg['To'] = secrets['email_rcvr']
        try:
            server=smtplib.SMTP(secrets['smtp_server'])
            server.starttls()
            server.login(secrets['email'],secrets['email_password'])
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(e)
