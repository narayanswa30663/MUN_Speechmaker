# -*- coding: utf-8 -*-

import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

print("Validating your credentials, please wait.")

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret2.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
if True:
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1zSj2icDHabI2J4606hPre-v9oKWvI6AoVpFH8NoRsC0'
    rangeName = 'Form Responses 1!C2:E'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    values = [[v[0].replace(':',''),v[2]] for v in values if v != []]

import uuid, re, time, random, datetime

user = '%012x' % uuid.getnode()

for i in values:
    if i[0] == user and i[1] == "Valid":
        print("Welcome!")
        break
else:
    print("You don't have valid credentials to run this software.")
    print("To proceed, go back to the main Github repository online")
    print("to register, and then contact us to make the payment.")
    exit()

import random as OO0OO0000OO0OOO0O #line:3
import textwrap as O000OOOOO0OO0OO00 #line:4
frvrb1 =OO0OO0000OO0OOO0O .choice (['provides','presents','proposes','offers','lays out','suggests'])#line:7
fradj1 =OO0OO0000OO0OOO0O .choice (['practical','workable','achievable','attainable','realistic','sensible','reasonable','suitable','helpful','constructive','logical','active'])#line:9
againstvrb1 =OO0OO0000OO0OOO0O .choice (['provides','presents','proposes','offers','lays out','suggests'])#line:11
againstadj =['infeasible','impractical','unachievable','unrealistic','unsuitable','unobtainable','unattainable']#line:13
country =input ("Which Country/Organization/Group are you representing? Your answer: ")#line:18
issue =input ("What is the issue/topic of debate?")#line:23
def userstance ():#line:29
    global stance #line:30
    stance =input ("What’s your stance? [f/a] Your answer: ")#line:31
    if (stance .lower ()not in ['f','a']):#line:32
        print ("Please make sure you answered either 'f' or 'a'.")#line:33
        userstance ()#line:34
userstance ()#line:35
sampleclause1 =input ("Which clause would you like to talk about first? [eg. 5/a/ii]").split ('/')#line:41
c1 ="clause "+sampleclause1 [0 ]#line:42
try :#line:43
    c1 +=", sub-clause "+(sampleclause1 [1 ])#line:44
    try :#line:45
        c1 +=", sub-sub-clause "+(sampleclause1 [2 ])#line:46
    except :#line:47
        pass #line:48
except :#line:49
    pass #line:50
suggested =input ("What is this clause suggesting/proposing? DO NOT put a period at the end of your response. Start your answer with 'This clause proposes that we...' Your answer: ")#line:54
if (stance .lower ()=='f'):#line:58
    goodclause1 =input ("Why is this clause good? Write in full sentences, and make sure to start your reason with 'This clause is very good because...' Also, elaborate a little bit on your reasoning. ")#line:59
elif (stance .lower ()=='a'):#line:60
    badclause1 =input ("Why is this clause bad? Write in full sentences, and make sure to start your reason with 'This clause is bad because...' Also, elaborate a little bit on your reasoning. ")#line:61
sampleclause2 =input ("Which clause would you like to talk about second? [eg. 5/a/ii]").split ('/')#line:67
c2 ="clause "+sampleclause2 [0 ]#line:68
try :#line:69
    c2 +=", sub-clause "+(sampleclause2 [1 ])#line:70
    try :#line:71
        c2 +=", sub-sub-clause "+(sampleclause2 [2 ])#line:72
    except :#line:73
        pass #line:74
except :#line:75
    pass #line:76
suggested2 =input ("What is this clause suggesting/proposing? DO NOT put a period at the end of your response. Start your answer with 'this clause proposes that we...' Your answer: ")#line:80
if (stance .lower ()=='f'):#line:84
    goodclause2 =input ("Why is this clause good? Write in full sentences, and make sure to start your reason with 'This clause is very good because...' Also, elaborate a little bit on your reasoning. ")#line:85
elif (stance .lower ()=='a'):#line:86
    badclause2 =input ("Why is this clause bad? Write in full sentences, and make sure to start your reason with 'This clause is bad because...' Also, elaborate a little bit on your reasoning. ")#line:87
consen =input ("Please enter one or more sentence(s) that sum(s) up your speech/your stance: ")#line:92
if (stance .lower ()=='a'):#line:97
    print ("Honorable chair, fellow delegates, and most esteemed guests, the delegate of %s urges all member states\
 to vote against this resolution, as the solutions that it %s are %s and %s, and do not help us solve the issue of %s.\
 This delegate would like to start by drawing the house's attention to %s. %s. %s Next, this delegate would like to\
 direct the attention of all member states to %s. %s. %s %s "%(country .title (),againstvrb1 ,OO0OO0000OO0OOO0O .choice (againstadj ),OO0OO0000OO0OOO0O .choice (againstadj ),issue ,c1 ,suggested ,badclause1 ,c2 ,suggested2 ,badclause2 ,consen ))#line:101
elif (stance .lower ()=="f"):#line:102
    print ("Honorable chair, fellow delegates, and most esteemed guests, the delegate of %s urges all member states\
 to vote in favor of this resolution, as it clearly %s %s solutions to solve the\
 issue of %s. This delegate would like to start by drawing the house's attention to %s. %s. %s Next, this delegate would like to\
 direct the attention of all member states to %s. %smeme. %s %s "%(country .title (),frvrb1 ,fradj1 ,issue ,c1 ,suggested ,goodclause1 ,c2 ,suggested2 ,goodclause2 ,consen ))
#e9015584e6a44b14988f13e2298bcbf9
