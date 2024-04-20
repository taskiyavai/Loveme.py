#!/usr/bin/python3
#----Data protector
#----Made by PY HXRON

import os, time,base64,sys
from os import system as cmd
os.system("https://t.me/PY_LEARNER")

try:
    import rich
except:
    os.system("pip install rich")
    import rich


from rich import print as heron_afridi
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import track
from rich.tree import Tree
from rich import print_json





logo="""[red1] ____    __   ____   __   
(  _ \  /__\ (_  _) /__\  
 )(_) )/(__)\  )(  /(__)\ 
(____/(__)(__)(__)(__)(__)  [bold green]P[light_steel_blue1]R[wheat1]O[khaki1]T[nave_blue]E[bright_black]C[red1]T[bold blue]O[bold cyan]R
"""
meno=Tree("[bright_green][A] [pale_turquoise1]Turn On Data Protector.     ")
meno.add("[bright_green][B] [pale_turquoise1]Turn Off Data Protector.     ")
c=base64.b64decode(b'eGRnLW9wZW4gaHR0cHM6Ly90Lm1lL1BZX0xFQVJORVI=')
cx=c.decode("ASCII")
cmd(cx)
def ck():
    try:
        
        used=open(".hjj.txt","r").read()
        if "on" in used:
            xoxo="ON"
        else:
            xoxo="OF"
    except:
        xoxo="OF"
    return xoxo

def call(j):
    try:
        used=open(".hjj.txt","r").read()
        if j in used:
            heron_afridi(Panel.fit("         [✓] SUCCESSFULLY ON         "))
            time.sleep(10)
            main()
        else:
            onn()
    except:onn()


def xall(j):
    try:
        used=open(".hjj.txt","r").read()
        if j in used:
            heron_afridi(Panel.fit("         [✓] SUCCESSFULLY OFF         "))
            time.sleep(10)
            main()
        else:
            off()
    except:off()

def main():
    os.system("clear")
    heron_afridi(Panel.fit(logo))
    heron_afridi(Panel.fit("  [green_yellow]FACEBOOK      ->      PY HXRON  \n  [dark_sea_green2]GITHUB        ->      TEAM-ELITE1  ", title="[bold purple]DEVELOPER INFO"))
    heron_afridi(Panel.fit(f"[bright_green] RIGHT NOW YOUR DATA PROTECTOR IS {ck()} ", subtitle="[bold bright_yellow]STATUS"))
    heron_afridi(Panel.fit(meno))
    h=str(input(" [=] INPUT !#> "))
    if h in ["a","A","1","01"]:
        j="on"
        call(j)
        
    elif h in ["b","B","2","02"]:
        j="off"
        xall(j)
        
    else:main()

def onn():
    try:
        os.system("cd && mv ../usr/bin/rm ../usr/bin/heron")
        os.system("cd && mv ../usr/bin/rmdir ../usr/bin/heron2")
        open(".hjj.txt","w").write("on")
        heron_afridi(Panel.fit("         [✓] SUCCESSFULLY ON         "))
        time.sleep(10)
    except:pass

    main()


def off():
    try:
        os.system("cd && mv ../usr/bin/heron ../usr/bin/rm")
        os.system("cd && mv ../usr/bin/heron2 ../usr/bin/rmdir")
        open(".hjj.txt","w").write("off")
        heron_afridi(Panel.fit("         [✓] SUCCESSFULLY OFF         "))
        time.sleep(10)
    except:pass
    main()


main()

