
import os,sys

try:
    import requests
except:
    os.system("pip install requests")
    import requests



def server():
    try:
        database=requests.get("https://raw.githubusercontent.com/TEAM-ELITE1/Elite-Data-base/main/On_off_update.txt").text
    except:
         print(" Internet Error [✓] ")
         sys.exit()
    if "on" in database:
        pass
    elif "off" in database:
        print(" [✓] TOOL IS OFF")
        sys.exit()
    else:
        while True:
            print(" Tool is on update")

server()

print("tool is on")