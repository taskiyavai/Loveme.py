import os,time

#pip install rich

try:
    import rich
except:
    os.system("pip install rich")
    import rich

from rich.progress import track

def looood(heron):
    for i in track(range(500),description=heron):
        time.sleep(0.01) 



#looood("OPENING")