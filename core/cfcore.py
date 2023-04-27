#####################################################################
#                                                                   #
#                                                                   #
#                                                                   #
#'##:::'##:'####:'########::'########::'######::'########::'######::#
# ##::'##::. ##:: ##.... ##:..... ##::'##... ##: ##.....::'##... ##:#
# ##:'##:::: ##:: ##:::: ##::::: ##::: ##:::..:: ##::::::: ##:::..::#
# #####::::: ##:: ##:::: ##:::: ##::::. ######:: ######::: ##:::::::#
# ##. ##:::: ##:: ##:::: ##::: ##::::::..... ##: ##...:::: ##:::::::#
# ##:. ##::: ##:: ##:::: ##:: ##::::::'##::: ##: ##::::::: ##::: ##:#
# ##::. ##:'####: ########:: ########:. ######:: ########:. ######::#
#..::::..::....::........:::........:::......:::........:::......:::#
#                                                                   #
#          All Messages from Developer, it's just a joke lol        #
#                                                                   #
#####################################################################


import os, sys, time, colorama
from termcolor import cprint, colored
from colorama import init, Fore
from time import sleep as timeout
from datetime import datetime, date
from core.buildcore import *

#ERROR
def err():
  print("[$root ~/coffe/error ]# something error or coffe expired(please update)")
  time.sleep(1)
  backtomenu_option()

#Fuctions and more EIEI

def install():
  cprint('\n[COFFE SHOP]> Waiting... coffe is coming for you :)', 'yellow', attrs=['blink'])
  time.sleep(2)
  os.system('mkdir /opt/coffe')
  time.sleep(2)
  os.system('echo "cd /opt/coffe && python3 coffe.py" > coffe')
  time.sleep(2)
  os.system('chmod 755 coffe && mv coffe /usr/bin')
  os.system('mv $HOME/coffe/coffe.py /opt/coffe')
  os.system('mv $HOME/coffe/core /opt/coffe')
  os.system('mv $HOME/coffe/README.md /opt/coffe')
  time.sleep(3)
  os.system('clear')
  cprint('[Message from developer]> Thanks you for purchased, grab a coffe and pop the shells\n', 'green', attrs=['blink'])
  print(Fore.RED + "Hello neo, coffe has ordered to you system :) ")

def update():
  os.system('rm -rf coffe')
  time.sleep(4)
  os.system('git clone https://github.com/Plague1234/coffe')
  time.sleep(4)
  os.system('rm /opt/coffe/coffe.py')
  time.sleep(2)
  os.system('mv coffe/coffe.py /opt/coffe/')
  time.sleep(2)
  os.system('rm -rf /opt/coffe/core')
  time.sleep(2)
  os.system('mv coffe/core /opt/coffe/')
  time.sleep(2)
  os.system('rm /opt/coffe/README.md')
  time.sleep(2)
  os.system('mv coffe/README.md /opt/coffe/')
  cprint('[Message from coffe]> Update Successfully...\n', 'green', attrs=['blink'])
  time.sleep(3)
  os.system('coffe')

today = datetime.today()
#Date now
#print(time.strftime("%Y-%m-%d"))
now = today.strftime("%Y %H:%M")

def check_user():
  if os.geteuid()==0:
    print("Welcome Neo...")
  else:
    print("coffe requires root privileges for enter coffe shop to chillin :)")
    sys.exit()

def check_menu():
#Coffe menu check before run coffe script
  datet = '2023-05-7'
  expireDate = time.strftime("%Y-%m-%d")
  if expireDate >= datet:
    print("COFFE : CLOSED")
  else:
    print("Status: OPEN")

def closed():
  datez = '2023-05-7'
  expireDate = time.strftime("%Y-%m-%d")
  if expireDate >= datez:
    err()
  else:
    print() #Nothing to do

def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)
  curdir = os.getcwd()

backtomenu_banner = """

  [99] Back to main menu
  [00] Exit the Coffe

"""

def backtomenu_option():
  print(backtomenu_banner)
  backtomenu = input("[$root ~/coffe ]# ")

  if backtomenu == "99": restart_program()

  elif backtomenu == "0" or backtomenu == "00":
    sys.exit()

  else:
    print("ERROR : WRONG INPUT\n")
    timeout(2)
    restart_program()

#Malware functions
def trojan():
  cprint('[Warning]:: For Education only and pentest your system not allowed for personal use\n', 'yellow', attrs=['blink'])
  tj = input("[$root ~/coffe/trojan ]# ")

  if tj == "build trojan":
    buildexe()
  else:
    print("ERROR: command not found\n")
    backtomenu_option()

def worm():
  cprint('[Warning]:: For Education only and pentest your system not allowed for personal use\n', 'yellow', attrs=['blink'])
  wm = input("[root ~/coffe/worm ]# ")
  if wm == "build iloveyou":
    iloveyou()
  else:
    print("ERROR: command not found")
    backtomenu_option()

def spy():
  cprint('[Warning]:: For Education only and pentest your system not allowed for personal use\n', 'yellow', attrs=['blink'])
  sp = input("[root ~/coffe/spy ]# ")
  if sp == "build spyware":
    spyware()
  else:
    print("ERROR: command not found")
    backtomenu_option()

def ransomware():
  cprint('[Warning]:: For Education only and pentest your system not allowed for personal use\n', 'yellow', attrs=['blink'])
  rsw = input("[root ~/coffe/ransomware ]# ")
  if rsw == "build ransomware":
    ransomware()
  else:
    print("ERROR: command not found")
    backtomenu_option()

def admalware():
  cprint('[Warning]:: For Education only and pentest your system not allowed for personal use\n', 'yellow', attrs=['blink'])
  adm = input("[root ~/coffe/androidmalware ]# ")
  if adm == "build admalware":
    admalware()
  else:
    print("ERROR: command not found")
    backtomenu_option()

def rvshell():
  cprint('[Warning]:: For Education only and pentest your system not allowed for personal user\n', 'yellow', attrs=['blink'])
  rvs = input("[root ~/coffe/reverseshell ]# ")
  if rvs == "build reverseshell":
    rvshell()
  else:
    print("ERROR: command not found")
    backtomenu_option()

def addon():
  cprint('[Warning]:: This text for warning script-kiddies who not use thier /dev/bain!\n', 'red', attrs=['blink'])
  print(Fore.BLUE + "[Message from dev] : Installing of B4CKD00R to / ")
  timeout(2)
  print(Fore.YELLOW + "\nINSTALL Trojan to / ")
  timeout(2)
  print(Fore.RED + "INSTALL Backdoor to / ")
  timeout(2)
  print(Fore.YELLOW + "INSTALL iloveyou to / ")
  timeout(2)
  print(Fore.RED + "INSTALL RiPz to / ")
  timeout(2)
  print(Fore.YELLOW + "INSTALL KidzWare to / ")
  timeout(4)
  print(Fore.GREEN + "\nWake up, Neo...")
  sys.exit()

