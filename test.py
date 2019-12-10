# -*- coding: utf-8 -*- 
import LINEPY
from LINEPY import *
from akad.ttypes import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
#import pyimgflip
from googletrans import Translator
import youtube_dl

print ("======[ MEMBUAT AKUN B❂TTR❂X Bots]======")
print ("===========[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]=============")
satria = LineClient()
#satria = LineClient(authToken='EFkWExcEoXPY6QwvTPe0.fGIUiExEjuE1/OChSHYIia.V8DOPt11Siy3LnSI0wL67kO+bWkQ0vJjBtFoNJ4ESUY=')
satria.log("Auth Token : " + str(satria.authToken))
channel = LineChannel(satria)
satria.log("Channel Access Token : " + str(channel.channelAccessToken))
print ("AKUN BOTTROX BOTS 1")
ki = LineClient()
#ki = LineClient(authToken='EFkWExcEoXPY6QwvTPe0.fGIUiExEjuE1/OChSHYIia.V8DOPt11Siy3LnSI0wL67kO+bWkQ0vJjBtFoNJ4ESUY=')
ki.log("Auth Token : " + str(ki.authToken))
channel1 = LineChannel(ki)
ki.log("Channel Access Token  : " + str(channel1.channelAccessToken))
print ("AKUN BOTTROX Ghost 1")
kz = LineClient()
#kz = LineClient(authToken='EFkWExcEoXPY6QwvTPe0.fGIUiExEjuE1/OChSHYIia.V8DOPt11Siy3LnSI0wL67kO+bWkQ0vJjBtFoNJ4ESUY=')
kz.log("Auth Token : " + str(kz.authToken))
channel2 = LineChannel(kz)
kz.log("Channel Access Token : " + str(channel2.channelAccessToken))
print ("AKUN BOTTROX Anjtijs 1")
kw = LineClient()
#kw = LineClient(authToken='EFkWExcEoXPY6QwvTPe0.fGIUiExEjuE1/OChSHYIia.V8DOPt11Siy3LnSI0wL67kO+bWkQ0vJjBtFoNJ4ESUY=')
kw.log("Auth Token : " + str(kw.authToken))
channel3 = LineChannel(kw)
kw.log("Channel Access Token : " + str(channel3.channelAccessToken))
print ("╔══╗─╔═══╗╔════╗╔════╗╔═══╗╔═══╗╔═╗╔═╗")
print ("║╔╗║─║╔═╗║║╔╗╔╗║║╔╗╔╗║║╔═╗║║╔═╗║╚╗╚╝╔╝")
print ("║╚╝╚╗║║─║║╚╝║║╚╝╚╝║║╚╝║╚═╝║║║─║║─╚╗╔╝─")
print ("║╔═╗║║║─║║──║║────║║──║╔╗╔╝║║─║║─╔╝╚╗─")
print ("║╚═╝║║╚═╝║──║║────║║──║║║╚╗║╚═╝║╔╝╔╗╚╗")
print ("╚═══╝╚═══╝──╚╝────╚╝──╚╝╚═╝╚═══╝╚═╝╚═╝")
print ("======⊰์◉⊱B❂T$ SIAP DI GUNAKAN⊰์◉⊱=======")

#ubah mid di dalem admin,owner,creator.json dengan mid kalian
poll = LinePoll(satria)
call = satria
creator = ["ub6f9d53713c5869f0d78e71febe13837"]
owner = ["ub6f9d53713c5869f0d78e71febe13837"]
admin = ["ub6f9d53713c5869f0d78e71febe13837"]
staff = ["ub6f9d53713c5869f0d78e71febe13837"]
mid = satria.getProfile().mid
Amid = ki.getProfile().mid
Wmid = kz.getProfile().mid
Zmid = kw.getProfile().mid
KAC = [satria,ki]
ABC = [ki]
Bots = [mid,Amid,Wmid,Zmid]
Satria = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []

welcome = []
simisimi = []
translateen = []
translateid = []
translateth = []
translatetw = []
translatear = []

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

aditProfile = satria.getProfile()
myProfile["displayName"] = aditProfile.displayName
myProfile["statusMessage"] = aditProfile.statusMessage
myProfile["pictureStatus"] = aditProfile.pictureStatus

responsename0 = satria.getProfile().displayName
responsename1 = ki.getProfile().displayName

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)    

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '\n🇲🇨 %02d Hari \n🇲🇨 %02d Jam \n🇲🇨 %02d Menit \n🇲🇨 %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '\n🇲🇨 %02d Hari \n🇲🇨 %02d Jam \n🇲🇨 %02d Menit \n🇲🇨 %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(satria.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        satria.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        satria.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers1(to, mids=[]):
   # if mids in mids: mids.remove(mid)
    parsed_len = len(mids)//20+1
    result = '╭───「 ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ 」\n'
    mention = '@zeroxyuuki\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '│ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰───「⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱」\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            satria.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''
        
def mentionMembers2(to, mid):
    try:
        arrData = ""
        textx = "Total User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(satria.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        satria.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        satria.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@SatriaSelf "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    satria.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    
def sendMeention2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@SatriaSelf "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    satria.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(satria.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        satria.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        satria.sendMessage(to, None, contentMetadata={"STKID":"15597499","STKPKGID":"1403265","STKVER":"1"}, contentType=7)
    except Exception as error:
        satria.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Haii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = satria.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nDi group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(satria.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        satria.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        satria.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Byee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nDari group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(satria.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        satria.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        satria.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = satria.getAllContactIds()
        gid = satria.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"⏩Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n⏩Group : "+str(len(gid))+"\n⏩Teman : "+str(len(teman))+"\n⏩Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n⏩Runtime : \n • "+bot
        satria.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        satria.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        satria.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        satria.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def sendMention2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@BotTroxBots "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    satria.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╔════════════════════╗" + "\n" + \
                  " ◄]·✪🔥╯═﷼͜͡❂Satria❂͜͡﷼🔥✪·[►" + "\n" + \
                  "╚════════════════════╝" + "\n" + \
                  "╔════════════════════╗" + "\n" + \
                  " ◄]·✪·Menu Admin·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ " + key + "Help\n" + \
                  "╠❂➣ " + key + "Help bot\n" + \
                  "╠❂➣ " + key + "Translate\n" + \
                  "╠❂➣ " + key + "Meme\n" + \
                  "╠❂➣ " + key + "Me\n" + \
                  "╠❂➣ " + key + "Mymid\n" + \
                  "╠❂➣ " + key + "Mid「@」\n" + \
                  "╠❂➣ " + key + "Info 「@」\n" + \
                  "╠❂➣ " + key + "Kick1 「@」\n" + \
                  "╠❂➣ " + key + "Mybot\n" + \
                  "╠❂➣ " + key + "Status\n" + \
                  "╠❂➣ " + key + "Status translate\n" + \
                  "╠❂➣ " + key + "About\n" + \
                  "╠❂➣ " + key + "Restart\n" + \
                  "╠❂➣ " + key + "Runtime\n" + \
                  "╠❂➣ " + key + "Creator\n" + \
                  "╠❂➣ " + key + "Respon\n" + \
                  "╠❂➣ " + key + "Speed/Sp\n" + \
                  "╠❂➣ " + key + "Sprespon\n" + \
                  "╠❂➣ " + key + "Tag\n" + \
                  "╠❂➣ " + key + "join\n" + \
                  "╠❂➣ " + key + "Assist join\n" + \
                  "╠❂➣ " + key + "Ginfo\n" + \
                  "╠❂➣ " + key + "Open\n" + \
                  "╠❂➣ " + key + "Close\n" + \
                  "╠❂➣ " + key + "Url grup\n" + \
                  "╠❂➣ " + key + "Reject\n" + \
                  "╠❂➣ " + key + "Gruplist\n" + \
                  "╠❂➣ " + key + "Infogrup「angka」\n" + \
                  "╠❂➣ " + key + "Infomem「angka」\n" + \
                  "╠❂➣ " + key + "Lurking「on/off」\n" + \
                  "╠❂➣ " + key + "Lurkers\n" + \
                  "╠❂➣ " + key + "Sider「on/off」\n" + \
                  "╠❂➣ " + key + "Updatefoto\n" + \
                  "╠❂➣ " + key + "Updategrup\n" + \
                  "╠❂➣ " + key + "Updatebot\n" + \
                  "╠❂➣ " + key + "Broadcast:「Text」\n" + \
                  "╠❂➣ " + key + "Setkey「New Key」\n" + \
                  "╠❂➣ " + key + "Mykey\n" + \
                  "╠❂➣ " + key + "Resetkey\n" + \
                  "╠════════════════════╗" + "\n" + \
                  " ◄]·✪·Hiburan·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ " + key + "Musik:「Judul Lagu」\n" + \
                  "╠❂➣ " + key + "Musik2:「Judul Lagu」\n" + \
                  "╠❂➣ " + key + "Playlist「Nama Penyanyi」\n" + \
                  "╠❂➣ " + key + "Ytmp3:「Judul Lagu」\n" + \
                  "╠❂➣ " + key + "Ytmp4:「Judul Video\n" + \
                  "╠❂➣ " + key + "Meme@Nama@Teks1@Teks2\n" + \
                  "╠❂➣ " + key + "1cak\n" + \
                  "╠❂➣ " + key + "Profilesmule:「ID Smule」\n" + \
                  "╠❂➣ " + key + "Randomnumber:「Nmor-Nmor」\n" + \
                  "╠❂➣ " + key + "Gimage:「Keyword」\n" + \
                  "╠❂➣ " + key + "Img food:「Nama Makanan」\n" + \
                  "╠❂➣ " + key + "Cekig:「ID IG」\n" + \
                  "╠❂➣ " + key + "Profileig:「Nama IG」\n" + \
                  "╠❂➣ " + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "╠❂➣ " + key + "Spamtag:「jumlahnya」\n" + \
                  "╠❂➣ " + key + "Spamtag「@」\n" + \
                  "╠❂➣ " + key + "Spamcall:「jumlahnya」\n" + \
                  "╠❂➣ " + key + "Spamcall\n" + \
                  "╠════════════════════╗" + "\n" + \
                  " ◄]·✪ CREATOR ✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ " + key + "Notag「on/off」\n" + \
                  "╠❂➣ " + key + "Allpro「on/off」\n" + \
                  "╠❂➣ " + key + "Protecturl「on/off」\n" + \
                  "╠❂➣ " + key + "Protectjoin「on/off」\n" + \
                  "╠❂➣ " + key + "Protectkick「on/off」\n" + \
                  "╠❂➣ " + key + "Protectcancel「on/off」\n" + \
                  "╠❂➣ " + key + "Protectinvite「on/off」\n" + \
                  "╠════════════════════╗" + "\n" + \
                  " ◄]·✪ OWNER ✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ " + key + "Unsend「on/off」\n" + \
                  "╠❂➣ " + key + "Jointicket「on/off」\n" + \
                  "╠❂➣ " + key + "Sticker「on/off」\n" + \
                  "╠❂➣ " + key + "Respon「on/off」\n" + \
                  "╠❂➣ " + key + "Respongift「on/off」\n" + \
                  "╠❂➣ " + key + "Contact「on/off」\n" + \
                  "╠❂➣ " + key + "Autojoin「on/off」\n" + \
                  "╠❂➣ " + key + "Autoadd「on/off」\n" + \
                  "╠❂➣ " + key + "Welcome「on/off」\n" + \
                  "╠❂➣ " + key + "Simi「on/off」\n" + \
                  "╠❂➣ " + key + "Autoleave「on/off」\n" + \
                  "╠══════════════════════════════╗" + "\n" + \
                  "     ◄]·✪ OWNER ✪·[►" + "\n" + \
                  "╠══════════════════════════════╝" + "\n" + \
                  "╠❂➣ " + key + "Admin:on\n" + \
                  "╠❂➣ " + key + "Admin:delete\n" + \
                  "╠❂➣ " + key + "Staff:on\n" + \
                  "╠❂➣ " + key + "Staff:delete\n" + \
                  "╠❂➣ " + key + "Bot:on\n" + \
                  "╠❂➣ " + key + "Bot:delete\n" + \
                  "╠❂➣ " + key + "Adminadd「@」\n" + \
                  "╠❂➣ " + key + "Admindell「@」\n" + \
                  "╠❂➣ " + key + "Staffadd「@」\n" + \
                  "╠❂➣ " + key + "Staffdell「@」\n" + \
                  "╠❂➣ " + key + "Botadd「@」\n" + \
                  "╠❂➣ " + key + "Botdell「@」\n" + \
                  "╠❂➣ " + key + "Refresh\n" + \
                  "╠❂➣ " + key + "Listbot\n" + \
                  "╠❂➣ " + key + "Listadmin\n" + \
                  "╠❂➣ " + key + "Listprotect\n" + \
                  "╠❂➣ Ketik「 Refresh 」Jika Sudah\n╠❂➣ Menggunakan Command Diatas...\n" + \
                  "╠════════════════════╗" + "\n" + \
                  " ◄]·✪🔥╯═﷼͜͡❂Satria❂͜͡﷼🔥✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "◄]·✪line.me/ti/p/~iia008✪·[►" + "\n" + \
                  "╚════════════════════╝"
    return helpMessage
    
    

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╔════════════════════╗" + "\n" + \
                  " 🇲🇨 🔥╯═﷼͜͡❂Satria❂͜͡﷼🔥 🇲🇨" + "\n" + \
                  "╚════════════════════╝" + "\n" + \
                  "╔════════════════════╗" + "\n" + \
                  " ◄]·✪·BOT·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ " + key + "Mytoken\n" + \
                  "╠❂➣ " + key + "Cek sider\n" + \
                  "╠❂➣ " + key + "Cek spam\n" + \
                  "╠❂➣ " + key + "Cek pesan\n" + \
                  "╠❂➣ " + key + "Cek respon\n" + \
                  "╠❂➣ " + key + "Cek welcome\n" + \
                  "╠❂➣ " + key + "Cek leave\n" + \
                  "╠❂➣ " + key + "Set sider:「Text」\n" + \
                  "╠❂➣ " + key + "Set spam:「Text」\n" + \
                  "╠❂➣ " + key + "Set pesan:「Text」\n" + \
                  "╠❂➣ " + key + "Set respon:「Text」\n" + \
                  "╠❂➣ " + key + "Set welcome:「Text」\n" + \
                  "╠❂➣ " + key + "Set leave:「Text」\n" + \
                  "╠❂➣ " + key + "Myname:「Nama」\n" + \
                  "╠❂➣ " + key + "Bot1name:「Nama」\n" + \
                  "╠❂➣ " + key + "Bot2name:「Nama」\n" + \
                  "╠❂➣ " + key + "Bot1up「Kirim fotonya」\n" + \
                  "╠❂➣ " + key + "Bot2up「Kirim fotonya」\n" + \
                  "╠❂➣ " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "╠❂➣ " + key + "Spam:「Mid korban」「Jumlah」\n" + \
				  "╠❂➣ " + key + "Spamtag:「jumlahnya」\n" + \
                  "╠❂➣ " + key + "Spamtag「@」\n" + \
                  "╠❂➣ " + key + "Spamcall:「jumlahnya」\n" + \
                  "╠❂➣ " + key + "Spamcall\n" + \
				  "╠❂➣ " + key + "Updatefoto\n" + \
                  "╠❂➣ " + key + "Updategrup\n" + \
                  "╠❂➣ " + key + "Updatebot\n" + \
                  "╠❂➣ " + key + "Broadcast:「Text」\n" + \
                  "╠❂➣ " + key + "Setkey「New Key」\n" + \
                  "╠❂➣ " + key + "Mykey\n" + \
                  "╠❂➣ " + key + "Resetkey\n" + \
				  "╠❂➣ " + key + "Self「on/off」\n" + \
				  "╠❂➣ " + key + "Hapus chat\n" + \
                  "╠❂➣ " + key + "Remove chat\n" + \
				  "╠❂➣ " + key + "Leave:「Namagrup」\n" + \
                  "╠════════════════════╗" + "\n" + \
                  " ◄]·✪ OWNER ✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ " + key + "Blc\n" + \
                  "╠❂➣ " + key + "Ban:on\n" + \
                  "╠❂➣ " + key + "Unban:on\n" + \
                  "╠❂➣ " + key + "Ban「@」\n" + \
                  "╠❂➣ " + key + "Unban「@」\n" + \
                  "╠❂➣ " + key + "Talkban「@」\n" + \
                  "╠❂➣ " + key + "Untalkban「@」\n" + \
                  "╠❂➣ " + key + "Talkban:on\n" + \
                  "╠❂➣ " + key + "Untalkban:on\n" + \
                  "╠❂➣ " + key + "Banlist\n" + \
                  "╠❂➣ " + key + "Talkbanlist\n" + \
                  "╠❂➣ " + key + "Clearban\n" + \
                  "╠❂➣ " + key + "Refresh\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "  ◄]·✪🔥╯═﷼͜͡❂Satria❂͜͡﷼🔥✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "◄]·✪line.me/ti/p/~iia008✪·[►" + "\n" + \
                  "╚════════════════════╝"
    return helpMessage1
    
def infomeme():
    helpMessage2 = """
╔═══════════════════════╗
       ◄]·✪🔥╯═﷼͜͡❂Satria❂͜͡﷼🔥✪·[►
╚═══════════════════════╝
╔═══════════════════════╗
    ◄]·✪·List Meme·✪·[►
╠═══════════════════════╝
╠❂➣ Buzz
╠❂➣ Spongebob
╠❂➣ Patrick
╠❂➣ Doge
╠❂➣ Joker
╠❂➣ Xzibit
╠❂➣ You_tried
╠❂➣ cb
╠❂➣ blb
╠❂➣ wonka
╠❂➣ keanu
╠❂➣ cryingfloor
╠❂➣ disastergirl
╠❂➣ facepalm
╠❂➣ fwp
╠❂➣ grumpycat
╠❂➣ captain
╠❂➣ mmm
╠❂➣ rollsafe
╠❂➣ sad-obama
╠❂➣ sad-clinton
╠❂➣ aag
╠❂➣ sarcasticbear
╠❂➣ sk
╠❂➣ sparta
╠❂➣ sad
╠❂➣ contoh:
╠❂➣ Meme@buzz@lu tau?@gatau
╠═══════════════════════╗
╠       ◄]·✪🔥╯═﷼͜͡❂Satria❂͜͡﷼🔥✪·[►
╠═══════════════════════╝
╠═══════════════════════╗
◄]·✪line.me/ti/p/~iia008✪·[►
╚═══════════════════════╝
"""
    return helpMessage2
    
def translate():
    helpTranslate =    "╔══════════════════════════╗" + "\n" + \
                       "     🇲🇨 🔥╯═﷼͜͡❂Satria❂͜͡﷼🔥 🇲🇨" + "\n" + \
                       "╚══════════════════════════╝" + "\n" + \
                       "╔══════════════════════════╗" + "\n" + \
                       "     ◄]·✪·Translate·✪·[►" + "\n" + \
                       "╠══════════════════════════╝" + "\n" + \
	                   "╠❂➣ Autotrans「en-on/en-off」\n" + \
                       "╠❂➣ Autotrans「id-on/id-off」\n" + \
                       "╠❂➣ Autotrans「th-on/th-off」\n" + \
                       "╠❂➣ Autotrans「tw-on/tw-off」\n" + \
                       "╠❂➣ Autotrans「ar-on/ar-off」\n" + \
                       "╠❂➣ af : afrikaans" + "\n" + \
                       "╠❂➣ sq : albanian" + "\n" + \
                       "╠❂➣ am : amharic" + "\n" + \
                       "╠❂➣ ar : arabic" + "\n" + \
                       "╠❂➣ hy : armenian" + "\n" + \
                       "╠❂➣ az : azerbaijani" + "\n" + \
                       "╠❂➣ eu : basque" + "\n" + \
                       "╠❂➣ be : belarusian" + "\n" + \
                       "╠❂➣ bn : bengali" + "\n" + \
                       "╠❂➣ bs : bosnian" + "\n" + \
                       "╠❂➣ bg : bulgarian" + "\n" + \
                       "╠❂➣ ca : catalan" + "\n" + \
                       "╠❂➣ ceb : cebuano" + "\n" + \
                       "╠❂➣ ny : chichewa" + "\n" + \
                       "╠❂➣ zh-cn : chinese (simplified)" + "\n" + \
                       "╠❂➣ zh-tw : chinese (traditional)" + "\n" + \
                       "╠❂➣ co : corsican" + "\n" + \
                       "╠❂➣ hr : croatian" + "\n" + \
                       "╠❂➣ cs : czech" + "\n" + \
                       "╠❂➣ da : danish" + "\n" + \
                       "╠❂➣ nl : dutch" + "\n" + \
                       "╠❂➣ en : english" + "\n" + \
                       "╠❂➣ eo : esperanto" + "\n" + \
                       "╠❂➣ et : estonian" + "\n" + \
                       "╠❂➣ tl : filipino" + "\n" + \
                       "╠❂➣ fi : finnish" + "\n" + \
                       "╠❂➣ fr : french" + "\n" + \
                       "╠❂➣ fy : frisian" + "\n" + \
                       "╠❂➣ gl : galician" + "\n" + \
                       "╠❂➣ ka : georgian" + "\n" + \
                       "╠❂➣ de : german" + "\n" + \
                       "╠❂➣ el : greek" + "\n" + \
                       "╠❂➣ gu : gujarati" + "\n" + \
                       "╠❂➣ ht : haitian creole" + "\n" + \
                       "╠❂➣ ha : hausa" + "\n" + \
                       "╠❂➣ haw : hawaiian" + "\n" + \
                       "╠❂➣ iw : hebrew" + "\n" + \
                       "╠❂➣ hi : hindi" + "\n" + \
                       "╠❂➣ hmn : hmong" + "\n" + \
                       "╠❂➣ hu : hungarian" + "\n" + \
                       "╠❂➣ is : icelandic" + "\n" + \
                       "╠❂➣ ig : igbo" + "\n" + \
                       "╠❂➣ id : indonesian" + "\n" + \
                       "╠❂➣ ga : irish" + "\n" + \
                       "╠❂➣ it : italian" + "\n" + \
                       "╠❂➣ ja : japanese" + "\n" + \
                       "╠❂➣ jw : javanese" + "\n" + \
                       "╠❂➣ kn : kannada" + "\n" + \
                       "╠❂➣ kk : kazakh" + "\n" + \
                       "╠❂➣ km : khmer" + "\n" + \
                       "╠❂➣ ko : korean" + "\n" + \
                       "╠❂➣ ku : kurdish (kurmanji)" + "\n" + \
                       "╠❂➣ ky : kyrgyz" + "\n" + \
                       "╠❂➣ lo : lao" + "\n" + \
                       "╠❂➣ la : latin" + "\n" + \
                       "╠❂➣ lv : latvian" + "\n" + \
                       "╠❂➣ lt : lithuanian" + "\n" + \
                       "╠❂➣ lb : luxembourgish" + "\n" + \
                       "╠❂➣ mk : macedonian" + "\n" + \
                       "╠❂➣ mg : malagasy" + "\n" + \
                       "╠❂➣ ms : malay" + "\n" + \
                       "╠❂➣ ml : malayalam" + "\n" + \
                       "╠❂➣ mt : maltese" + "\n" + \
                       "╠❂➣ mi : maori" + "\n" + \
                       "╠❂➣ mr : marathi" + "\n" + \
                       "╠❂➣ mn : mongolian" + "\n" + \
                       "╠❂➣ my : myanmar (burmese)" + "\n" + \
                       "╠❂➣ ne : nepali" + "\n" + \
                       "╠❂➣ no : norwegian" + "\n" + \
                       "╠❂➣ ps : pashto" + "\n" + \
                       "╠❂➣ fa : persian" + "\n" + \
                       "╠❂➣ pl : polish" + "\n" + \
                       "╠❂➣ pt : portuguese" + "\n" + \
                       "╠❂➣ pa : punjabi" + "\n" + \
                       "╠❂➣ ro : romanian" + "\n" + \
                       "╠❂➣ ru : russian" + "\n" + \
                       "╠❂➣ sm : samoan" + "\n" + \
                       "╠❂➣ gd : scots gaelic" + "\n" + \
                       "╠❂➣ sr : serbian" + "\n" + \
                       "╠❂➣ st : sesotho" + "\n" + \
                       "╠❂➣ sn : shona" + "\n" + \
                       "╠❂➣ sd : sindhi" + "\n" + \
                       "╠❂➣ si : sinhala" + "\n" + \
                       "╠❂➣ sk : slovak" + "\n" + \
                       "╠❂➣ sl : slovenian" + "\n" + \
                       "╠❂➣ so : somali" + "\n" + \
                       "╠❂➣ es : spanish" + "\n" + \
                       "╠❂➣ su : sundanese" + "\n" + \
                       "╠❂➣ sw : swahili" + "\n" + \
                       "╠❂➣ sv : swedish" + "\n" + \
                       "╠❂➣ tg : tajik" + "\n" + \
                       "╠❂➣ ta : tamil" + "\n" + \
                       "╠❂➣ te : telugu" + "\n" + \
                       "╠❂➣ th : thai" + "\n" + \
                       "╠❂➣ tr : turkish" + "\n" + \
                       "╠❂➣ uk : ukrainian" + "\n" + \
                       "╠❂➣ ur : urdu" + "\n" + \
                       "╠❂➣ uz : uzbek" + "\n" + \
                       "╠❂➣ vi : vietnamese" + "\n" + \
                       "╠❂➣ cy : welsh" + "\n" + \
                       "╠❂➣ xh : xhosa" + "\n" + \
                       "╠❂➣ yi : yiddish" + "\n" + \
                       "╠❂➣ yo : yoruba" + "\n" + \
                       "╠❂➣ zu : zulu" + "\n" + \
                       "╠❂➣ fil : Filipino" + "\n" + \
                       "╠❂➣ he : Hebrew" + "\n" + \
                       "╠══════════════════════════╗" + "\n" + \
                       "  Contoh: tr-en Satria" + "\n" + \
                       "╠══════════════════════════╝" + "\n" + \
                       "╠══════════════════════════╗" + "\n" + \
                       "◄]·✪line.me/ti/p/~iia008✪·[►" + "\n" + \
                       "╚══════════════════════════╝"
    return helpTranslate

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if satria.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            satria.reissueGroupTicket(op.param1)
                            X = satria.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            satria.updateGroup(X)
                            random.choice(ABC).sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            wait["blacklist"][op.param2] = True
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                ki.updateGroup(X)
                                random.choice(ABC).sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                wait["blacklist"][op.param2] = True
                    except:
                        pass

        if op.type == 11:
            if wait["qr"] == True:
                try:
                    if random.choice(ABC).getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            random.choice(ABC).reissueGroupTicket(op.param1)
                            X = random.choice(ABC).getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            random.choice(ABC).updateGroup(X)
                            random.choice(ABC).sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass             
                        
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        satria.acceptGroupInvitation(op.param1)
                        ginfo = satria.getGroup(op.param1)
                        satria.sendMessage(op.param1,"Haii, salken yaa ^^")
                    else:
                        satria.acceptGroupInvitation(op.param1)
                        ginfo = satria.getGroup(op.param1)
                        satria.sendMessage(op.param1,"Haii, salken yaa ^^")
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = satria.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                        except:
                            pass

        if op.type == 13:
            if wait["proinvite"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = random.choice(ABC).getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                    except:
                        pass
                        	
        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = satria.getGroup(op.param1)
                contact = satria.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                satria.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = satria.getGroup(op.param1)
                contact = satria.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                satria.sendImageWithURL(op.param1, image)

        #if op.type == 17:
           # if op.param1 in protectjoin:
                #if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    #wait["blacklist"][op.param2] = True
                   # try:
                        #if op.param3 not in wait["blacklist"]:
                        	#random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    #except:
                        #pass
                #return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        satria.sendMessage(op.param1, wait["message"])

#===========KICK============#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 19:
            if wait["prokick"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = satria.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        satria.updateGroup(G)
                        invsend = 0
                        Ticket = satria.reissueGroupTicket(op.param1)
                        kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kz.kickoutFromGroup(op.param1,[op.param2])
                        kz.leaveGroup(op.param1)
                        X = satria.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        satria.updateGroup(X)
            except:
                pass             
                
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kw.acceptGroupInvitation(op.param1)
                        G = kw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kw.updateGroup(G)
                        Ticket = kw.reissueGroupTicket(op.param1)
                        satria.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      #  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kw.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        kw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        kw.leaveGroup(op.param1)
                        satria.inviteIntoGroup(op.param1,[Zmid])
                        satria.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        satria.kickoutFromGroup(op.param1,[op.param2])
                        satria.findAndAddContactsByMid(op.param3)
                        satria.inviteIntoGroup(op.param1,[Zmid])
                        satria.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        satria.kickoutFromGroup(op.param1,[op.param2])
                        satria.findAndAddContactsByMid(op.param3)
                        satria.inviteIntoGroup(op.param1,[Zmid])
                        satria.sendMessage(op.param1,"=AntiJS Invited=")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            satria.kickoutFromGroup(op.param1,[op.param2])
                            satria.findAndAddContactsByMid(op.param3)
                            satria.inviteIntoGroup(op.param1,[op.param3])
                            satria.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass
                                  
#===========Cancel============#

        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.findAndAddContactsByMid(op.param1,[Zmid])
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[Zmid])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                satria.findAndAddContactsByMid(op.param1,[Zmid])
                                satria.kickoutFromGroup(op.param1,[op.param2])
                                satria.inviteIntoGroup(op.param1,[Zmid])
                        except:
                            pass
                return

        if op.type == 32:
            if wait["procancel"] == True:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).findAndAddContactsByMid(op.param1,[Zmid])
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                    except:
                        pass
                        	
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        satria.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            satria.acceptGroupInvitationByTicket(op.param1,Ticket)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                        except:
                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        satria.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                        satria.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            G = satria.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            satria.updateGroup(G)
                            Ticket = satria.reissueGroupTicket(op.param1)
                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                            satria.kickoutFromGroup(op.param1,[op.param2])
                            G = satria.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            satria.updateGroup(G)
                            Ticket = satria.reissueGroupTicket(op.param1)
                        except:
                            pass
                return


            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.findAndAddContactsByMid(op.param1,admin)
                        ki.inviteIntoGroup(op.param1,admin)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            satria.findAndAddContactsByMid(op.param1,admin)
                            satria.inviteIntoGroup(op.param1,admin)
                            satria.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            satria.findAndAddContactsByMid(op.param1,staff)
                            satria.inviteIntoGroup(op.param1,staff)
                            satria.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["readPoint"]:
                   if op.param2 in Setmain["readMember"][op.param1]:
                       pass
                   else:
                       Setmain["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = satria.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = satria.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        satria.sendImageWithURL(op.param1, image)                        
                        
                    
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = satria.getGroup(at)
                                Satria = satria.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(Satria.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Satria.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                satria.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                satria.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = satria.getGroup(at)
                                Satria = satria.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "⏩Pengirim : {}".format(str(Satria.displayName))
                                ret_ += "\n⏩Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n⏩Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n⏩Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                satria.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = satria.getGroup(at)
                                Satria = satria.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "⏩Pengirim : {}".format(str(Satria.displayName))
                                ret_ += "\n⏩Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n⏩Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                satria.sendMessage(at, str(ret_))
                                satria.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message                    
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://corrykalam.pw/api/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               satria.sendMessage(msg.to, str(data["answer"])) 
                   except Exception as error:
                       pass
                   
               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           satria.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                           
                           
               if msg.to in translateid:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='id')
                           A = hasil.text
                           satria.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translateth:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='th')
                           A = hasil.text
                           satria.sendMessage(msg.to, A)
                   except Exception as error:
                       pass
                   
               if msg.to in translatetw:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='zh-tw')
                           A = hasil.text
                           satria.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translatear:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='ar')
                           A = hasil.text
                           satria.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                    

        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           satria.sendMessage(msg.to, wait["Respontag"])
                           satria.sendMessage(msg.to, None, contentMetadata={"STKID":"52002747","STKPKGID":"11537","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           satria.sendMessage(msg.to, "Yang suka ngetag minta di gift yaa!?\nCek di chat, udah aku gift tuh...")
                           satria.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           satria.sendMessage(msg.to, "Jangan tag saya....")
                           satria.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    satria.sendMessage(msg.to,"「Cek ID Sticker」\n🐚 STKID : " + msg.contentMetadata["STKID"] + "\n⏩ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n⏩ STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    satria.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = satria.getContact(msg.contentMetadata["mid"])
                        path = satria.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        satria.sendMessage(msg.to,"⏩ Nama : " + msg.contentMetadata["displayName"] + "\n⏩ MID : " + msg.contentMetadata["mid"] + "\n⏩ Status : " + contact.statusMessage + "\n⏩ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        satria.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = satria.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n⏩Sticker ID : {}".format(stk_id)
                   ret_ += "\n⏩Sticker Version : {}".format(stk_ver)
                   ret_ += "\n⏩Sticker Package : {}".format(pkg_id)
                   ret_ += "\n•⏩Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = satria.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                                                      
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    satria.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    satria.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = satria.getContact(msg.contentMetadata["mid"])
                        path = satria.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        satria.sendMessage(msg.to,"⏩ Nama : " + msg.contentMetadata["displayName"] + "\n⏩ MID : " + msg.contentMetadata["mid"] + "\n⏩ Status : " + contact.statusMessage + "\n⏩ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        satria.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = ki.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = satria.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            ki.sendMessage(msg.to, "Maaf, dia ada di daftar blacklist\n")
                            break
                        else:
                            targets.append(invite["mid"])
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  ki.findAndAddContactsByMid(targetUserIds)
                                  ki.inviteIntoGroup(msg.to,[target])
                                  ryan = ki.getContact(targetUserIds)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 Sukses Invite 」\nNama "
                                  ret_ = "Ketik invite off jika sudah masuk"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  ki.sendReplyMessage(msg.id,msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  ki.sendMessage(msg.to,"ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʟɪᴍɪᴛ")
                                  wait["invite"] = False
                                  break                        
#===========ADD BOT============#
               if msg.contentType == 13:
                 if msg._from in creator:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        satria.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        satria.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        satria.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        satria.sendMessage(msg.to,"Contact itu bukan anggota BOT")
#===========ADD STAFF============#
                 if msg._from in creator:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        satria.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        satria.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        satria.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        satria.sendMessage(msg.to,"Contact itu bukan staff")
#===========ADD ADMIN============#
                 if msg._from in owner:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        satria.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        satria.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        satria.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        satria.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        satria.sendMessage(msg.to,"Contact itu bukan admin")
#===========ADD BLACKLIST============#
                 if msg._from in owner:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        satria.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        satria.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        satria.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        satria.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#===========TALKBAN============#
                 if msg._from in owner:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        satria.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        satria.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        satria.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        satria.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#===========UPDATE FOTO============#
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = satria.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            satria.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in owner:
                   if settings["groupPicture"] == True:
                     path = satria.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     satria.updateGroupPicture(msg.to, path)
                     satria.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in owner:
                       if mid in Setmain["foto"]:
                            path = satria.downloadObjectMsg(msg_id)
                            del Setmain["foto"][mid]
                            satria.updateProfilePicture(path)
                            satria.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in owner:
                        if Amid in Setmain["foto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["foto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in owner:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")               

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        satria.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               veza = satria.getContact(mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan =  "╭─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╮\n│✮sᴀᴛʀɪᴀᴮᴼᵀʟɪɴᴇ✯\n│★ᴜsᴇʀ : "
                               ret_ = str(helpMessage)
                               ry = str(veza.displayName)
                               pesan = ''
                               pesan2 = pesan+"@x \n\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan + zxc + ret_ + ""
                               satria.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                                                                       
                        if cmd == "self on":
                            if msg._from in owner:
                                wait["selfbot"] = True
                                satria.sendMessage(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in owner:
                                wait["selfbot"] = False
                                satria.sendMessage(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "help bot":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               helpMessage1 = helpbot()
                               veza = satria.getContact(mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan =  "╭─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╮\n│✮sᴀᴛʀɪᴀᴮᴼᵀʟɪɴᴇ✯\n│★ᴜsᴇʀ : "
                               ret_ = str(helpMessage1)
                               ry = str(veza.displayName)
                               pesan = ''
                               pesan2 = pesan+"@x \n\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan + zxc + ret_ + ""
                               satria.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                               
                        elif cmd == "meme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = infomeme()
                               veza = satria.getContact(mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan =  "╭─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╮\n│✮sᴀᴛʀɪᴀᴮᴼᵀʟɪɴᴇ✯\n│★ᴜsᴇʀ : "
                               ret_ = str(helpMessage2)
                               ry = str(veza.displayName)
                               pesan = ''
                               pesan2 = pesan+"@x \n\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan + zxc + ret_ + ""
                               satria.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                               
                        elif cmd == "translate":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpTranslate = translate()
                               satria.sendMessage(msg.to, str(helpTranslate))                               
                               
                        if cmd == "unsend on":
                            if msg._from in owner:
                                wait["unsend"] = True
                                satria.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")
                                
                        if cmd == "unsend off":
                            if msg._from in owner:
                                wait["unsend"] = False
                                satria.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")                                

                        elif cmd == "set":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = " ┏━━━━━━━━━━━━━━━━━\n┃┃          🐚 S T A T U S 🐚\n┃┣━━━━━━━━━━━━━━━━━━━━\n"
                                if wait["unsend"] == True: md+="┃┃🇲🇨 ✔️ Unsend「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Unsend「OFF」\n"                                
                                if wait["sticker"] == True: md+="┃┃🇲🇨 ✔️ Sticker「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Sticker「OFF」\n"
                                if wait["contact"] == True: md+="┃┃🇲🇨 ✔️ Contact「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Contact「OFF」\n"
                                if wait["talkban"] == True: md+="┃┃🇲🇨 ✔️ Talkban「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Talkban「OFF」\n"
                                if wait["Mentionkick"] == True: md+="┃┃🇲🇨 ✔️ Notag「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Notag「OFF」\n"
                                if wait["detectMention"] == True: md+="┃┃🇲🇨 ✔️ Respon「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Respon「OFF」\n"
                                if wait["Mentiongift"] == True: md+="┃┃🇲🇨 ✔️ Respongift「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Respongift「OFF」\n"                                
                                if wait["autoJoin"] == True: md+="┃┃🇲🇨 ✔️ Autojoin「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Autojoin「OFF」\n"
                                if settings["autoJoinTicket"] == True: md+="┃┃🇲🇨 ✔️ Jointicket「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Jointicket「OFF」\n"                                
                                if wait["autoAdd"] == True: md+="┃┃🇲🇨 ✔️ Autoadd「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Autoadd「OFF」\n"
                                if msg.to in welcome: md+="┃┃🇲🇨 ✔️ Welcome「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Welcome「OFF」\n"
                                if msg.to in simisimi: md+="┃┃🇲🇨 ✔️ Simisimi「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Simisimi「OFF」\n"                                
                                if wait["autoLeave"] == True: md+="┃┃🇲🇨 ✔️ Autoleave「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Autoleave「OFF」\n"
                                if msg.to in protectqr: md+="┃┃🇲🇨 ✔️ Protecturl「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Protecturl「OFF」\n"
                                if msg.to in protectjoin: md+="┃┃🇲🇨 ✔️ Protectjoin「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Protectjoin「OFF」\n"
                                if msg.to in protectkick: md+="┃┃🇲🇨 ✔️ Protectkick「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Protectkick「OFF」\n"
                                if msg.to in protectcancel: md+="┃┃🇲🇨 ✔️ Protectcancel「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Protectcancel「OFF」\n"
                                if msg.to in protectinvite: md+="┃┃🇲🇨 ✔️ Protectinvite「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Protectinvite「OFF」\n"                                                
                                ginfo = satria.getGroup(msg.to)
                                ryan = satria.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╮\n│「 sᴇᴛ user」\n│⏩ Creator: "
                                ret_ = "│⏩ ɢʀᴏᴜᴘ: {}\n".format(str(ginfo.name))
                                ret_ += str(md)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + "┝────────────────\n│⏩ ᴄʟᴏᴄᴋ: 「"+ datetime.strftime(timeNow,'%H:%M:%S')+"」 "+"\n│⏩ ᴮᴼᵀᵀᴿᴼˣʙᴏᴛs ᴅᴀᴛᴇ: 「"+ datetime.strftime(timeNow,'%Y-%m-%d') +"」\n╚──[ ᴮᴼᵀᵀᴿᴼˣʙᴏᴛsˢᴱᴸᶠ ]───╝"
                                satria.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                
                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "  ┏━━━━━━━━━━━━━━━━━\n┃┃ 🐚 STATUS TRANSLATE 🐚\n┃┣━━━━━━━━━━━━━━━━━━━━\n"
                                if msg.to in translateen: md+="┃┃🇲🇨 ✔️ English「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ English「OFF」\n"
                                if msg.to in translateid: md+="┃┃🇲🇨 ✔️ Indonesia「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Indonesia「OFF」\n"
                                if msg.to in translateth: md+="┃┃🇲🇨 ✔️ Thailand「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Thailand「OFF」\n"
                                if msg.to in translatetw: md+="┃┃🇲🇨 ✔️ Taiwan「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Taiwan「OFF」\n"
                                if msg.to in translatear: md+="┃┃🇲🇨 ✔️ Arab「ON」\n"
                                else: md+="┃┃🇲🇨 ✖ Arab「OFF」\n"       
                                ginfo = satria.getGroup(msg.to)
                                ryan = satria.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╮\n│「 sᴇᴛ user」\n│⏩ Creator: "
                                ret_ = "│⏩ ɢʀᴏᴜᴘ: {}\n".format(str(ginfo.name))
                                ret_ += str(md)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + "┝────────────────\n│⏩ ᴄʟᴏᴄᴋ: 「"+ datetime.strftime(timeNow,'%H:%M:%S')+"」 "+"\n│⏩ ᴮᴼᵀᵀᴿᴼˣʙᴏᴛs ᴅᴀᴛᴇ: 「"+ datetime.strftime(timeNow,'%Y-%m-%d') +"」\n╚──[ ᴮᴼᵀᵀᴿᴼˣʙᴏᴛsˢᴱᴸᶠ ]───╝"
                                satria.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "creator1" or text.lower() == 'creator1':
                            if msg._from in admin:
                               satria.sendContact(to, sender)
                               sendMention2(to, "╔─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╗\n│✆「sᴇʟғ ᴠ.0.11.0」 \n│✆「ᴛʏᴘᴇ sᴀᴛʀɪᴀᴮᴼᵀ」 \n│✆「ᴄᴏᴍᴇ ᴏɴ ᴏʀᴅᴇʀ」 \n│✆「ᴡᴇ ᴀʀᴇ sᴀᴛʀɪᴀᴮᴼᵀ」\n│✆「ᴜsᴇʀ: @! 」\n╚────[ ᴮᴼᵀᵀᴿᴼˣʙᴏᴛsˢᴱᴸᶠ ]────╝",[sender])
                               
                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                               satria.sendMessage(msg.to, "╔─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╗\n╠❂➣ MY CREATOR \n")
                               satria.sendContact(msg.to, "u1608ae21e5de2547b5fa8707b21ca220")
                               satria.sendMessage(msg.to, "╚────[ ᴮᴼᵀᵀᴿᴼˣʙᴏᴛsˢᴱᴸᶠ ]────╝")
				
                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 BotTrox BOT 」\n")
                               satria.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)
                               satria.sendImageWithURL(to, 'https://avatars0.githubusercontent.com/u/37049360?v=4')

                        elif cmd == "my" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               satria.sendContact(to, sender)
                               sendMention2(to, "╔─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╗\n│✆「sᴇʟғ ᴠ.0.11.0」 \n│✆「ᴛʏᴘᴇ sᴀᴛʀɪᴀᴮᴼᵀ」 \n│✆「ᴄᴏᴍᴇ ᴏɴ ᴏʀᴅᴇʀ」 \n│✆「ᴡᴇ ᴀʀᴇ sᴀᴛʀɪᴀᴮᴼᵀ」\n│✆「ᴜsᴇʀ: @! 」\n╚────[ ᴮᴼᵀᵀᴿᴼˣʙᴏᴛsˢᴱᴸᶠ ]────╝",[sender])

                        elif text.lower() == "mymid":
                            if msg._from in admin:
                               satria.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = satria.getContact(key1)
                               satria.sendMessage(msg.to, "╔─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╗\n│⏩ɴᴀᴍᴇ: "+str(mi.displayName)+"\n│⏩ᴍɪᴅ: " +key1+ "\n╚────[ ᴮᴼᵀᵀᴿᴼˣʙᴏᴛsˢᴱᴸᶠ ]─────╝")
                               satria.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = satria.getContact(key1)
                               satria.sendMessage(msg.to, "╔─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╗\n│⏩ Nama : "+str(mi.displayName)+"\n│⏩ Mid : " +key1+"\n│⏩ Status Message "+str(mi.statusMessage)+"\n╚────[ ᴮᴼᵀᵀᴿᴼˣʙᴏᴛsˢᴱᴸᶠ ]─────╝")
                               satria.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(satria.getContact(key1)):
                                   satria.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   satria.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               satria.sendMessage(msg.to, "╔─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╗\n╠❂➣ MY BOTS TEAM\n")
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               satria.sendMessage1(msg)
                               satria.sendContact(msg.to, "u9a3947a3947b568f264b1584a8c791bf")
                               satria.sendContact(msg.to, "u030a264c24f957ccf2388bab6fadffe8")
                               satria.sendContact(msg.to, "u3bc96c4457042e18c71c61b23f2dde72")
                               satria.sendContact(msg.to, "u73abe1f40b294203111ed9eb66564708")
                               satria.sendContact(msg.to, "u13c44e1c33d853effdda460eb408eceb")
                               satria.sendContact(msg.to, "u345f29417fc28a310f90ff4ee16b3d76")
                               satria.sendContact(msg.to, "u07fff90ec4c33e18a23c76eefbadb7ce")
                               satria.sendContact(msg.to, "ubd3be894b483e90be0a75524d5df522c")
                               satria.sendContact(msg.to, "u6882ac8f90063f82f1948c8c31ae7405")
                               satria.sendContact(msg.to, "u141397ac1e3188035f8ca9f514c10caf")
                               satria.sendContact(msg.to, "u67d9e2f8ef3a144a4f42a16fd232c75b")
                               satria.sendMessage(msg.to, "╚─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╝")                               
                               satria.sendImageWithURL(to, 'https://avatars0.githubusercontent.com/u/37049360?v=4')

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               try:
                                   satria.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   satria.sendMessage(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = satria.getGroupIdsJoined()
                               for group in saya:
                                   satria.sendMessage(group,"=======[BROADCAST]=======\n\n"+pesan+"\n\nCreator : line.me/ti/p/~adit_cmct")

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               satria.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   satria.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   satria.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               satria.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               satria.sendMessage(msg.to, "Restart Sukses Bos!...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               satria.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = satria.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(satria.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                satria.sendMessage(msg.to, "❧ BOT Grup Info\n\n ❧ Nama Group : {}".format(G.name)+ "\n🐚 ID Group : {}".format(G.id)+ "\n🐚 Pembuat : {}".format(G.creator.displayName)+ "\n🐚 Waktu Dibuat : {}".format(str(timeCreated))+ "\n🐚 Jumlah Member : {}".format(str(len(G.members)))+ "\n🐚 Jumlah Pending : {}".format(gPending)+ "\n🐚 Group Qr : {}".format(gQr)+ "\n🐚 Group Ticket : {}".format(gTicket))
                                satria.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                satria.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                satria.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = satria.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = satria.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(satria.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "⏩ BOT Grup Info\n"
                                ret_ += "\n⏩ Name : {}".format(G.name)
                                ret_ += "\n⏩ ID : {}".format(G.id)
                                ret_ += "\n⏩ Creator : {}".format(gCreator)
                                ret_ += "\n⏩ Created Time : {}".format(str(timeCreated))
                                ret_ += "\n⏩ Member : {}".format(str(len(G.members)))
                                ret_ += "\n⏩ Pending : {}".format(gPending)
                                ret_ += "\n⏩ Qr : {}".format(gQr)
                                ret_ += "\n⏩ Ticket : {}".format(gTicket)
                                ret_ += ""
                                satria.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = satria.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = satria.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "⏩ "+ str(no) + ". " + mem.displayName
                                satria.sendMessage(to,"⏩ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = satria.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = satria.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    satria.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = satria.getAllContactIds()
                               for i in gid:
                                   G = satria.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.displayName+ "\n"
                               satria.sendMessage(msg.to,"┏━━[ FRIEND LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = satria.getGroupIdsJoined()
                               for i in gid:
                                   G = satria.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               satria.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Groups ]")


                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                if msg.toType == 2:
                                   x = ki.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      ki.updateGroup(x)
                                   gurl = ki.reissueGroupTicket(msg.to)
                                   ki.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                                   
                                   
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = satria.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      satria.rejectGroupInvitation(gid)
                                  satria.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  satria.sendMessage(to, "Tidak ada undangan yang tertunda")

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                satria.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                settings["changePicture"] = True
                                ki.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                Setmain["foto"][mid] = True
                                satria.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot1up":
                            if msg._from in owner:
                                Setmain["foto"][Amid] = True
                                ki.sendMessage(msg.to,"Kirim fotonya.....")
                               

                        elif cmd.startswith("myname: "):
                          if msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = satria.getProfile()
                                profile.displayName = string
                                satria.updateProfile(profile)
                                satria.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "absen" or text.lower() == '😆':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	group = satria.getGroup(msg.to) 
                          Rmem = [contact.mid for contact in group.members]
                          Dmem = len(Rmem)//20
                          try:                          	
                              for mentionMembers in range(Dmem+1):
                                  no = 0
                                  ret_ = "       ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱  \n╔════════════\n   ✍͡❂͜͡ ❥༂ˢᴬᵀᴿᴵᴬ༂༻  [ √ ]\n╚════════════\n╔════════════"
                                  dataMid = []
                                  for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n╠ [{}] @!".format(str(no))
                                  ret_ += "\n╚══════════════\n╔═══════════════\n.  TOTAL MEMBER [ {} ]\n╚═══════════════\n.        ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱\n╰══ CREATOR: ©Satria \nhttps://line.me/ti/p/~iia008".format(str(len(dataMid))) 
                                  sendMeention2(msg.to, ret_, dataMid)                             
                          except Exception as Ewe:
                              print(Ewe)
                                  
                        elif cmd == "biji" or text.lower() == '😊':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                            	group = satria.getGroup(msg.to)
                          Rmem = [contact.mid for contact in group.members]
                          Dmem = len(Rmem)//20
                          try:                          	
                              for mentionMembers2 in range(Dmem+1):
                                  no = 0
                                  ret_ = "       ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱  \n╔════════════\n   ✍͡❂͜͡ ❥༂ˢᴬᵀᴿᴵᴬ༂༻ [ √  ]\n╚════════════\n╔════════════"
                                  dataMid = []
                                  for dataMention in group.members[mentionMembers2*20 : (mentionMembers2+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n╠.[{}] @!".format(str(no))
                                  ret_ += "\n╚══════════════\n╔═══════════════\n.  TOTAL MEMBER [ {} ]\n╚═══════════════\n.        ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱\n╰══ CREATOR: ©Satria \nhttps://line.me/ti/p/~iia008".format(str(len(dataMid))) 
                                  sendMeention(msg.to, ret_, dataMid)
                          except Exception as Ewe:
                              print(Ewe) 

                        elif cmd == 'tag':
                         #if wait["selfbot"] == True:
                         if msg._from in creator:
                            members = []
                            if msg.toType == 1:
                               room = satria.getRoom(to)
                               members = [mem.mid for mem in room.contacts]
                            elif msg.toType == 2:
                               group = satria.getGroup(to)
                               members = [mem.mid for mem in group.members]
                            else:
                               return satria.sendReplyMessage(msg_id, to, 'Failed mentionall members, use this command only on room or group chat')
                            if members:
                               mentionMembers1(to, members)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +satria.getContact(m_id).displayName + "\n"
                                satria.sendMessage(msg.to,"⏩ BOT\n\n"+ma+"\nTotal「%s」BOT" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +satria.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +satria.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +satria.getContact(m_id).displayName + "\n"
                                satria.sendMessage(msg.to,"⏩ Admin BOT\n\n⏩Creator BOT:\n"+ma+"\n⏩Admin:\n"+mb+"\n⏩Staff:\n"+mc+"\n⏩Total「%s」" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +satria.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +satria.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +satria.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +satria.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +satria.getGroup(group).name + "\n"                                    
                                satria.sendMessage(msg.to,"⏩ BOT Protection\n\n⏩ PROTECT URL :\n"+ma+"\n⏩ PROTECT KICK :\n"+mb+"\n⏩ PROTECT JOIN :\n"+md+"\n⏩ PROTECT CANCEL:\n"+mc+"\n⏩ PROTECT INVITE :\n"+me+"\nTotal「%s」Protect yang aktif" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	#satria.sendMessage(msg.to,responsename0)
                                ki.sendMessage(msg.to,responsename1)

                        elif cmd == "kuy":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                try:
                                    anggota = [Amid]
                                    satria.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    #ku.acceptGroupInvitation(msg.to)
                                    #kk.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                
                        elif cmd == "bot2invite":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                try:
                                    anggota = [Wmid,Zmid]
                                    satria.inviteIntoGroup(msg.to, anggota)
                                    kz.acceptGroupInvitation(msg.to)
                                    kw.acceptGroupInvitation(msg.to)
                                except:
                                    pass                                    
                                
                        elif cmd == "antijs stay":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                try:
                                    ginfo = satria.getGroup(msg.to)
                                    satria.inviteIntoGroup(msg.to, [Zmid])
                                    satria.sendMessage(msg.to,"Grup 「"+str(ginfo.name)+"」 Aman Dari JS")
                                except:
                                    pass                                
    
                        elif cmd == "join all":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                G = satria.getGroup(msg.to)
                                ginfo = satria.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                satria.updateGroup(G)
                                invsend = 0
                                Ticket = satria.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                            #    ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                               # kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = gg.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "bye":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                G = satria.getGroup(msg.to)
                                ki.sendMessage(msg.to, "Bye bye group "+str(G.name))
                                ki.leaveGroup(msg.to)
                               # ku.sendMessage(msg.to, "Bye bye group "+str(G.name))
                               # ku.leaveGroup(msg.to)
                               # kk.sendMessage(msg.to, "Bye bye group "+str(G.name))
                                #kk.leaveGroup(msg.to)
                                
                        elif cmd == "kicker bye":
                            if msg._from in creator:
                                G = satria.getGroup(msg.to)
                                kw.leaveGroup(msg.to)
                                
                        elif cmd == "ghost bye":
                            if msg._from in creator:
                                G = satria.getGroup(msg.to)
                                kz.leaveGroup(msg.to) 
                                
                        elif cmd.startswith("leave "):
                            if msg._from in creator:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = satria.getGroupIdsJoined()
                                for i in gid:
                                    h = satria.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        satria.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "assist1":
                            if msg._from in creator:
                                G = satria.getGroup(msg.to)
                                ginfo = satria.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                satria.updateGroup(G)
                                invsend = 0
                                Ticket = satria.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)


                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = aditmadzs.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = aditmadzs.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = aditmadzs.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                satria.sendMessage(msg.to, " ⏩BOT Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention1(msg.to, sender, "⏩sᴘᴇᴇᴅ ᴜᴘ\n⏩ᴜsᴇʀ:","")
                               start = time.time() 
                               time.sleep(0.0002)  
                               elapsed_time = time.time() - start
                               satria.sendMessage(msg.to,format(str(elapsed_time)))
                               ki.sendMessage(msg.to,format(str(elapsed_time)))

                        elif cmd == "cctv on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['readPoint'][msg.to] = msg_id
                                 Setmain['readMember'][msg.to] = {}
                                 satria.sendMessage(msg.to, "CCTV berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "cctv off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['readPoint'][msg.to]
                                 del Setmain['readMember'][msg.to]
                                 satria.sendMessage(msg.to, "CCTV berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "ciduk":
                          if msg._from in admin:
                            if msg.to in Setmain['readPoint']:
                                if Setmain['readMember'][msg.to] != {}:
                                    nad = []
                                    for x in Setmain['readMember'][msg.to]:
                                        nad.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Yang CCTV]\n1. ".format(str(len(nad)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in nad:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(nad):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(satria.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        satria.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['readPoint'][msg.to]
                                        del Setmain['readMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['readPoint'][msg.to] = msg.id
                                    Setmain['readMember'][msg.to] = {}
                                else:
                                    satria.sendMessage(msg.to, "User kosong...")
                            else:
                                satria.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  satria.sendMessage(msg.to, "╔─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╗\n╠ ⏩Cek sider diaktifkan\n╠═══════════════\n╠ ⏩Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠ ⏩Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╚────[ ᴮᴼᵀᵀᴿᴼˣʙᴏᴛsˢᴱᴸᶠ ]─────╝")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  satria.sendMessage(msg.to, "╔─[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]─╗\n╠ ⏩Cek sider dinonaktifkan\n╠═══════════════\n╠ ⏩Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠ ⏩ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╚────[ ᴮᴼᵀᵀᴿᴼˣʙᴏᴛsˢᴱᴸᶠ ]─────╝")
                              else:
                                  satria.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                                      
                        elif cmd.startswith("musik2: "):
                          if msg._from in admin:                        	
                            query = msg.text.replace("musik","")
                            search = query.replace(" ","+")
                            result = requests.get("https://api.zicor.ooo/joox.php?song={}".format(search))
                            data = result.text
                            data = json.loads(data)
                            ret_ = "-•••>> Play Music <<•••-"
                            ret_ += "\n- Judul : {}".format(data["title"])
                            ret_ += "\n- Artis : {}".format(data["singer"])
                            ret_ += "\n- Lirik :\n{}".format(data["lyric"])
                            satria.sendImageWithURL(to, data["image"])
                            #aditmadzs.sendMessage(msg_id, to, ret_)
                            satria.sendAudioWithURL(to, data["url"])

                        elif cmd.startswith("randomnumber: "):                            	
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                angka = msg.text.replace(separate[0] + " ","")  
                                tgb = angka.split("-")
                                num1 = tgb[0]
                                num2 = tgb[1]
                                r = requests.get("https://farzain.xyz/api/random.php?min="+num1+"&max="+num2)
                                data = r.json()
                                satria.sendMessage(msg.to,"Hasil : "+str(data["url"]))
                                
                                
                        elif cmd.startswith("1cak"):
                          if msg._from in admin:
                              r=requests.get("https://api-1cak.herokuapp.com/random")
                              data=r.text
                              data=json.loads(data)
                              print(data)
                              hasil = "Result :\n"
                              hasil += "\nID : " +str(data["id"])
                              hasil += "\nTitle : " + str(data["title"])
                              hasil += "\nUrl : " + str(data["url"]) 
                              hasil += "\nVotes : " + str(data["votes"])
                              satria.sendMessage(msg.to, str(hasil))
        
                        elif cmd.startswith("musik: "):
                          if msg._from in admin:    
                            try:
                                dan = msg.text.replace("musik2: ","")
                                r = requests.get("https://api.zicor.ooo/joox.php?song={}"+urllib.parse.quote(dan))
                                data = r.json()
                                l = data["lyric"].replace("ti:","Judul: ")
                                i = l.replace("ar:","Penyanyi: ")
                                r = i.replace("al:","Album: ")
                                ii = r.replace("[by:]","")
                                k = ii.replace("[offset:0]","")
                                lirik = k.replace("***Lirik didapat dari pihak ketiga***\n","")
                                satria.sendImageWithURL(msg.to, data["image"])
                                t = "[ Music ]"
                                t += "\n\nJudul: "+str(data["title"])
                                t+="\nPenyanyi: "+str(data["singer"])
                                t+="\n\n[ Finish ]\n\n"+str(lirik)
                                satria.sendMessage(msg.to, str(t))
                                satria.sendAudioWithURL(msg.to, data["url"])
                            except Exception as error:
                                pass
                            
                        elif cmd.startswith("playlist "):
                          if msg._from in admin:    
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = str(cond[0])
                                result = requests.get("https://api.zicor.ooo/joox.php?song={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━━[ List Lagu ]━━━━"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n❧「 {}Playlist {}:nomor 」 ".format(str(),str(search))
                                    ret_ += "\n❧「 {}Lirik {}:nomor 」 ".format(str(),str(search))
                                    satria.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "┏━━━━[ Detail Musik ]━━━━"
                                            ret_ += "\n┃┃ Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n┃┃ Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n┃┃ Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n┗━━[ Tunggu Audionya ]━━━"
                                            satria.sendMessage(msg.to, str(ret_))
                                            satria.sendAudioWithURL(msg.to, str(data["result"]["mp3"][0]))
                            except Exception as error:
                                pass
                            
                        elif cmd.startswith("lirik "):
                          if msg._from in admin:    
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = cond[0]
                                api = requests.get("https://api.zicor.ooo/joox.php?song={}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━━[ List Lirik ]━━━━"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n❧「 {}Lirik {}:nomor 」".format(str(),str(search))
                                    ret_ += "\n❧「 {}Playlist {}:nomor 」 ".format(str(),str(search))
                                    satria.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        satria.sendMessage(msg.to, str(lyric))
                            except Exception as error:
                                pass                                        
        
                        elif cmd.startswith("img food: "):
                          if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        satria.sendImageWithURL(msg.to, str(food["url"]))
                                        
                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                satria.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                satria.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                satria.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass                                
                            	
                        elif msg.text.lower().startswith("smule: "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            smule = "https://www.smule.com/"+ key
                            satria.sendMessage(to, "ini id smulenya kak\n" + smule)
                            satria.sendImageWithURL(msg.to, smule)
                           	
                        elif cmd.startswith("meme"):
                          if msg._from in admin:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            satria.sendImageWithURL(msg.to, image)
          
                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n❧ Author : ' + str(vid.author)
                                    durasi = '\n❧ Duration : ' + str(vid.duration)
                                    suka = '\n❧ Likes : ' + str(vid.likes)
                                    rating = '\n❧ Rating : ' + str(vid.rating)
                                    deskripsi = '\n❧ Deskripsi : ' + str(vid.description)
                                satria.sendVideoWithURL(msg.to, me)
                                satria.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                satria.sendMessage(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n❧ Author : ' + str(vid.author)
                                    durasi = '\n❧ Duration : ' + str(vid.duration)
                                    suka = '\n❧ Likes : ' + str(vid.likes)
                                    rating = '\n❧ Rating : ' + str(vid.rating)
                                    deskripsi = '\n❧ Deskripsi : ' + str(vid.description)
                                satria.sendImageWithURL(msg.to, me)
                                satria.sendAudioWithURL(msg.to, shi)
                                satria.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                satria.sendMessage(msg.to,str(e))
                                    
                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                satria.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                                satria.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                satria.sendMessage(msg.to, str(njer))
                                
                        elif cmd.startswith("cekig:"):
                            if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/ig_profile.php?apikey=arTdnVbJkW1EuzDNQrIxQDvHARIDcQ&id={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "┏━━[ Profile Instagram ]"
                                        ret_ += "\n┃┃ Nama : {}".format(str(data["info"]["full_name"]))
                                        ret_ += "\n┃┃ Username : {}".format(str(data["info"]["username"]))
                                        ret_ += "\n┃┃ Bio : {}".format(str(data["info"]["bio"]))
                                        ret_ += "\n┃┃ URL Bio : {}".format(str(data["info"]["url_bio"]))
                                        ret_ += "\n┃┃ Pengikut : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃┃ Diikuti : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃┃ Total Post : {}".format(str(data["count"]["post"]))
                                        ret_ += "\n┗━━[ https://www.instagram.com/{} ]".format(search)
                                        path = data["info"]["profile_pict"]
                                        satria.sendMessage(to, str(ret_))
                                        satria.sendImageWithURL(to, str(path))
                                except Exception as e:
                                    satria.sendMessage(msg.to, str(e))                                  

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91ARs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            satria.sendMessage(msg.to,"🐚 I N F O R M A S I 🐚\n\n"+"🐚 Date Of Birth : "+lahir+"\n🐚 Age : "+usia+"\n🐚 Ultah : "+ultah+"\n🐚 Zodiak : "+zodiak)

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["limit"] = num
                                satria.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                satria.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spam "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                satria.sendMessage1(msg)
                                            except Exception as e:
                                                satria.sendMessage(msg.to,str(e))
                                    else:
                                        satria.sendMessage(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = satria.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                satria.sendMessage(msg.to, "{} Undangan Call Grup Berhasil".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        satria.sendMessage(msg.to,str(e))
                                else:
                                    satria.sendMessage(msg.to,"Jumlah melebihi batas")
                                    
                        elif cmd.startswith("invite: "):
                          if msg._from in admin:
                               sep = text.split(" ")
                               idnya = text.replace(sep[0] + " ","")
                               conn = ki.findContactsByUserid(idnya)
                               ki.findAndAddContactsByMid(conn.mid)
                               ki.inviteIntoGroup(msg.to,[conn.mid])
                               group = ki.getGroup(msg.to)
                               xname = ki.getContact(conn.mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan = '「 Sukses Diinvite 」\nNama contact '
                               recky = str(xname.displayName)
                               pesan = ''
                               pesan2 = pesan+"@a\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':xname.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan+ zxc + "ke grup " + str(group.name) +""
                               ki.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                               
                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      satria.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      satria.sendMessage(midd, str(Setmain["ADITMADZSmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["ADITMADZSmessage1"]))

                                  
                        elif 'Mybottoken' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                               satria.sendMessage(msg.to,"Satria\n"+satria.authToken)
                               satria.sendMessage(msg.to,"KI\n"+ki.authToken)

#==============================================================================# 
                        elif msg.text.lower().startswith("tr-af "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='af')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sq "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sq')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-am "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='am')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ar "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ar')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hy "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hy')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-az "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='az')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-eu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='eu')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-be "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='be')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bn')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bs "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bs')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bg "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bg')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ca "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ca')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ceb "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ceb')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ny "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ny')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zh-cn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zh-cn')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zh-tw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zh-tw')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-co "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='co')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hr')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-cs "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='cs')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-da "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='da')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-nl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='nl')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-en "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='en')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-et "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='et')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fi')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fr')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fy "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fy')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-gl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='gl')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ka "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ka')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-de "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='de')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-el "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='el')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-gu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='gu')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ht "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ht')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ha "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ha')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-haw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='haw')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-iw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='iw')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hi')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hmn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hmn')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hu')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-is "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='is')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ig "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ig')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-id "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='id')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ga "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ga')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-it "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='it')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ja "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ja')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-jw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='jw')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-kn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='kn')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-kk "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='kk')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-km "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='km')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ko "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ko')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ku "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ku')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ky "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ky')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-lo "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='lo')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-la "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='la')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-lv "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='lv')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-lt "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='lt')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-lb "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='lb')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mk "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mk')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mg "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mg')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ms "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ms')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ml "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ml')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mt "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mt')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mi')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mr')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mn')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-my "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='my')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ne "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ne')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-no "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='no')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ps "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ps')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fa "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fa')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-pl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='pl')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-pt "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='pt')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-pa "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='pa')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ro "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ro')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ru "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ru')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sm "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sm')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-gd "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='gd')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sr')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-st "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='st')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sn')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sd "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sd')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-si "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='si')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sk "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sk')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sl')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-so "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='so')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-es "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='es')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-su "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='su')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sw')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sv "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sv')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-tg "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='tg')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ta "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ta')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-te "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='te')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-th "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='th')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-tr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='tr')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-uk "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='uk')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ur "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ur')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-uz "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='uz')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-vi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='vi')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-cy "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='cy')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-xh "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='xh')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-yi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='yi')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-yo "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='yo')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zu')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fil "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fil')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-he "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='he')
                            A = hasil.text
                            satria.sendMessage(msg.to, A)

#===========Settings============#
                        elif 'Simi ' in msg.text:
                              spl = msg.text.replace('Simi ','')
                              if spl == 'on':
                                  if msg.to in simisimi:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       simisimi.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in simisimi:
                                         simisimi.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Simi-simi Sudah Tidak Aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs) 
                                    
                        elif 'Autotrans th-' in msg.text:
                              spl = msg.text.replace('Autotrans th-','')
                              if spl == 'on':
                                  if msg.to in translateth:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateth.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateth:
                                         translateth.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                    
                                    
                        elif 'Autotrans en-' in msg.text:
                              spl = msg.text.replace('Autotrans en-','')
                              if spl == 'on':
                                  if msg.to in translateen:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateen.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateen:
                                         translateen.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Autotrans id-' in msg.text:
                              spl = msg.text.replace('Autotrans id-','')
                              if spl == 'on':
                                  if msg.to in translateid:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateid.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateid:
                                         translateid.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Autotrans tw-' in msg.text:
                              spl = msg.text.replace('Autotrans tw-','')
                              if spl == 'on':
                                  if msg.to in translatetw:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translatetw.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translatetw:
                                         translatetw.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Autotrans ar-' in msg.text:
                              spl = msg.text.replace('Autotrans ar-','')
                              if spl == 'on':
                                  if msg.to in translatear:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translatear.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translatear:
                                         translatear.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                    

                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = satria.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  satria.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = satria.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    satria.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
#===========Protection============#                                    

                        elif 'Protecturl ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = satria.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  satria.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = satria.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    satria.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = satria.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  satria.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = satria.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    satria.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = satria.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  satria.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = satria.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    satria.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = satria.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  satria.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = satria.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    satria.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Protectinvite ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = satria.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  satria.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = satria.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    satria.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                                                      

                        elif 'Antijs ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Antijs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Anti JS sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = satria.getGroup(msg.to)
                                       msgs = "Anti JS Diaktifkan\nDi Group : " +str(ginfo.name)
                                  satria.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = satria.getGroup(msg.to)
                                         msgs = "Anti JS Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    satria.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Ghost ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = satria.getGroup(msg.to)
                                       msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                  satria.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Sudah Tidak Aktif"
                                    satria.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                    
                                    
                        elif 'Allpro ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)                                      
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = satria.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = satria.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  satria.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""                                         
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = satria.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = satria.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    satria.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#

                        elif ("Kick1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           satria.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           satria.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           satria.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           satria.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Aditmadzs:
                                       try:
                                           staff.remove(target)
                                           satria.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Aditmadzs:
                                       try:
                                           Bots.remove(target)
                                           satria.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in creator:
                                wait["addadmin"] = True
                                satria.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:delete" or text.lower() == 'admin:delete':
                            if msg._from in creator:
                                wait["delladmin"] = True
                                satria.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in creator:
                                wait["addstaff"] = True
                                satria.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:delete" or text.lower() == 'staff:delete':
                            if msg._from in creator:
                                wait["dellstaff"] = True
                                satria.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in creator:
                                wait["addbots"] = True
                                satria.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:delete" or text.lower() == 'bot:delete':
                            if msg._from in creator:
                                wait["dellbots"] = True
                                satria.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in creator:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                satria.sendMessage(msg.to,"Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                                ma = ""
                                for i in admin:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                                ma = ""
                                for i in staff:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                                ma = ""
                                for i in Bots:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                ki.sendMessage(msg.to,"Silahkan kirim kontaknya,\nJika sudah slesai, ketik invite off")

                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                ki.sendMessage(msg.to,"Invite via contact dinonaktifkan")
                                
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentionkick"] = True
                                satria.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentionkick"] = False
                                satria.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = True
                                satria.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = False
                                satria.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = True
                                satria.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = False
                                satria.sendMessage(msg.to,"Auto respon dinonaktifkan")
                                
                        elif cmd == "respongift on" or text.lower() == 'respongift on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentiongift"] = True
                                satria.sendMessage(msg.to,"Auto respon gift diaktifkan")

                        elif cmd == "respongift off" or text.lower() == 'respongift off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentiongift"] = False
                                satria.sendMessage(msg.to,"Auto respon gift dinonaktifkan")                                

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoJoin"] = True
                                satria.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoJoin"] = False
                                satria.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoLeave"] = True
                                satria.sendMessage(msg.to,"Auto Leave Diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoLeave"] = False
                                satria.sendMessage(msg.to,"Auto Leave Dimatikan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = True
                                satria.sendMessage(msg.to,"Auto Add Diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = False
                                satria.sendMessage(msg.to,"Auto Add Dimatikan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = True
                                satria.sendMessage(msg.to,"Detect Sticker Diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = False
                                satria.sendMessage(msg.to,"Detect Sticker Dimatikan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                settings["autoJoinTicket"] = True
                                satria.sendMessage(msg.to,"Auto Join Ticket Diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                settings["autoJoinTicket"] = False
                                satria.sendMessage(msg.to,"Auto Join Ticket Dimatikan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           satria.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           satria.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkwblacklist"] = True
                                satria.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkdblacklist"] = True
                                satria.sendMessage(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           satria.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           satria.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["wblacklist"] = True
                                satria.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["dblacklist"] = True
                                satria.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              if wait["blacklist"] == {}:
                                satria.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +satria.getContact(m_id).displayName + "\n"
                                satria.sendMessage(msg.to,"⏩ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              if wait["Talkblacklist"] == {}:
                                satria.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +satria.getContact(m_id).displayName + "\n"
                                satria.sendMessage(msg.to,"⏩ Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["blacklist"] == {}:
                                    satria.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = satria.getContact(i)
                                        satria.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              wait["blacklist"] = {}
                              ragets = satria.getContacts(wait["blacklist"])
                              mc = "���%i」User Blacklist" % len(ragets)
                              satria.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in owner:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  satria.sendMessage(msg.to, "Gagal mengganti Pesan Message")
                              else:
                                  wait["message"] = spl
                                  satria.sendMessage(msg.to, "「Pesan Msg」\nPesan Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in owner:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  satria.sendMessage(msg.to, "Gagal mengganti Welcome Message")
                              else:
                                  wait["welcome"] = spl
                                  satria.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           if msg._from in owner:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  satria.sendMessage(msg.to, "Gagal mengganti Leave Message")
                              else:
                                  wait["leave"] = spl
                                  satria.sendMessage(msg.to, "「Leave Msg」\nLeave Message diganti jadi :\n\n「{}」".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           if msg._from in owner:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  satria.sendMessage(msg.to, "Gagal mengganti Respon Message")
                              else:
                                  wait["Respontag"] = spl
                                  satria.sendMessage(msg.to, "「Respon Msg」\nRespon Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in owner:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  satria.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["message1"] = spl
                                  satria.sendMessage(msg.to, "「Spam Msg」\nSpam Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in owner:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  satria.sendMessage(msg.to, "Gagal mengganti Sider Message")
                              else:
                                  wait["mention"] = spl
                                  satria.sendMessage(msg.to, "「Sider Msg」\nSider Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in owner:
                               satria.sendMessage(msg.to, "「Pesan Msg」\nPesan Message lu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in owner:
                               satria.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message lu :\n\n「 " + str(wait["welcome"]) + " 」")
                               
                        elif text.lower() == "cek leave":
                            if msg._from in owner:
                               satria.sendMessage(msg.to, "「Leave Msg」\nLeave Message lu :\n\n「 " + str(wait["leave"]) + " 」")                                 

                        elif text.lower() == "cek respon":
                            if msg._from in owner:
                               satria.sendMessage(msg.to, "「Respon Msg」\nRespon Message lu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in owner:
                               satria.sendMessage(msg.to, "「Spam Msg」\nSpam Message lu :\n\n「 " + str(Setmain["ADITMADZSmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in owner:
                               satria.sendMessage(msg.to, "「Sider Msg」\nSider Message lu :\n\n「 " + str(wait["mention"]) + " 」")
                               
                        elif text.lower() == "Hajar":
                          if msg.from_ in creator:
                           if msg.toType == 2:
                              print ("Ratain")
                              _name = msg.text.replace("Hajar","")
                              gs = satria.getGroup(msg.to)
                              satria.sendMessage(msg.to,"Hello Kk")
                              satria.sendMessage(msg.to,"Team BOTTROX Mau Bersih² Group Sampah Nih")
                              satria.sendMessage(msg.to,"Karna Ini Group Sampah Jadi Mau Di Bersihin Dulu Yah\n▶Jangan Baper...\n▶Jangan Nangis\n▶Jangan Cengeng\nBawa Enjoy Aja Kawan♪")
                              satria.sendMessage(to,"┣━━╦━━━BOTTTOX TEAM━━━╦━━╣")
                              satria.sendContact(to, mid)
                              satria.sendContact(to, Amid)
                              #satria.sendContact(to, Bmid)
                              satria.sendMessage(to,"┣━━╦━━━BOTTTOX TEAM━━━╦━━╣")
                              satria.sendMessage(msg.to,"This My Team")
                              targets = []
                              for g in gs.members:
                                if _name in g.displayName:
                                  targets.append(g.mid)
                              if targets == []:
                                satria.sendMessage(msg.to,"Not found")
                              else:
                                for target in targets:
                                  if target in admin:
                                    pass
                                  elif target in Bots:
                                    pass
                                  elif target in staff:
                                    pass
                                  else:
                                    try:
                                      klist=[satria,ki]
                                      kicker=random.choice(klist)
                                      kicker.kickoutFromGroup(msg.to,[target])
                                      #print (msg.to,[g.mid])
                                    except:
                                      try:
                                        satria.kickoutFromGroup(msg.to,[target])
                                      except:
                                        random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                        
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = satria.findGroupByTicket(ticket_id)
                                     satria.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     satria.sendMessage(msg.to, "OTW MASUK KE GROUP : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, " OTW MASUK KE GROUP : %s" % str(group.name))


    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
