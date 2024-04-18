#coder  : parvej ahmed 
#github : github.com/P4RVEJ
#---------color code--------#
I='\033[1;32m'
Q="\x1b[00m"
dt = f"{Q}[{I}•{Q}]"
n = '\n'
#---------import------------#
import os, sys
import requests 
from requests.structures import CaseInsensitiveDict
import random
#--------logo-------------#
logo=("""
██████  ██   ██ ██████  ██    ██ ███████      ██ 
██   ██ ██   ██ ██   ██ ██    ██ ██           ██ 
██████  ███████ ██████  ██    ██ █████        ██ 
██           ██ ██   ██  ██  ██  ██      ██   ██ 
██           ██ ██   ██   ████   ███████  █████  
 """)
#-------clear------------#
def clear():
    os.system("clear")
    print(logo)
    print(22*f'{Q} -')
    print(f' {dt} CODER    : PARVEJ AHMED ')
    print(f' {dt} Facebook : PARVEJ AHMED ')
    print(f' {dt} Github   : P4RVEJ')
    print(22*' -')
#-------line-------------#
def line():
    print(22*' -')
#---------menu-----------#
def menu():
  clear()
  print(f' {dt} [01] CUSTOM SMS')
  print(f' {dt} [02] CUSTOM SMS BBOMBER')
  print(f' {dt} [03] JOIN GROUP')
  print(f' {dt} [05] EXIT')
  user = input(f' {dt} CHOICE OPTION : ')
  if user in ['01', '1']:
    custom()
  elif user in ['02', '2']:
    customb()
  elif user in ['03', '3']:
    os.system('xdg-open https://t.me/BL4CK_H4X0R_Z0NE')
  else:
    exit(f' {dt} THANKS FOR USEING MY TOOLS ')
    
#-----------custom sms-----------#
def custom():
  clear()
  nmbr=input(f' {dt} ENTER NUMBER WITHOUT (+88) : ')
  msg=input(f' {dt} TEXT MESSAGE : ')
  line()
  api = f'https://csfcustomsms.000webhostapp.com/sms.php?number={nmbr}&sms={msg}'
  requests.get(api)
  print('SMS SENT SUCCESSFUL')
  
#----------custom sms bomber---------#
def customb():
  clear()
  nmbr=input(f' {dt} ENTER NUMBER WITHOUT (+88) : ')
  msg=input(f' {dt} TEXT MESSAGE : ')
  line()
  lmt = int(input(f' {dt} ENTER AMOUNT : '))
  for i in range(lmt):
    api = f'https://csfcustomsms.000webhostapp.com/sms.php?number={nmbr}&sms={msg}'
    requests.get(api)
    print((str(i+1))+f' {dt} SMS SENT SUCCESSFUL')
  print('CUSTOM SMS BOMBING SUCCESSFUL')
#-----------end-------------#
menu()