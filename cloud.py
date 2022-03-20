import requests
import json
import os
import threading
from pystyle import Colors, Colorate
from colorama import Fore
import sys
import time
import ctypes

os.system("cls")

ctypes.windll.kernel32.SetConsoleTitleW(f"Cloud")

kill_thread = False

def loading_ani():
    modes = [
        "[-]",
        "[\]",
        "[/]",
        
        
    ]
    while True:
        for mode in modes:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Sending file to Cloud.. : {mode}")
            time.sleep(0.2)
        if kill_thread == True:
            try:
                sys.exit(1)
            except:
                sys.exit(1)


def upload(file):
    global kill_thread
    thread = threading.Thread(target=loading_ani)
    thread.start()
    f = open(file, "rb")
    url = "https://api.anonfiles.com/upload"
    payload = {"file": f}

    r = requests.post(url, files=payload)

    x = json.loads(r.content)

    
    file_data = [
        x["data"]["file"]["metadata"]["name"],
        x["data"]["file"]["metadata"]["size"]["bytes"],
        x["data"]["file"]["metadata"]["size"]["readable"]
    ]
    saved_file = x["data"]["file"]["url"]["full"]
    file_name = file_data[0]
    file_bytes = file_data[1]
    file_size = file_data[2]

    status = x["status"]
    
    if status == True:
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}+{Fore.LIGHTBLACK_EX}] {Fore.WHITE}File Upload Worked!")
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}+{Fore.LIGHTBLACK_EX}] {Fore.WHITE}File Size {Fore.LIGHTBLACK_EX}: {Fore.WHITE}{file_size} {Fore.MAGENTA}~ {Fore.WHITE}{file_bytes} B")
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}+{Fore.LIGHTBLACK_EX}] {Fore.WHITE}File Name {Fore.LIGHTBLACK_EX}: {Fore.WHITE}{file_name}")
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}+{Fore.LIGHTBLACK_EX}] {Fore.WHITE}File LOCATION {Fore.LIGHTBLACK_EX}: ", end="")
        print(Colorate.Horizontal(Colors.cyan_to_green, f"{saved_file}", 1))

    kill_thread = True
    
    

try:
    file = sys.argv[1]
except IndexError:
    print(f"{Fore.LIGHTBLACK_EX}[{Fore.RED}x{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Did not supply file name {Fore.LIGHTBLACK_EX}~ {Fore.YELLOW}Usage {Fore.LIGHTBLACK_EX}:{Fore.GREEN} cloud {Fore.LIGHTBLACK_EX}[{Fore.GREEN}filename{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    try:
        sys.exit(1)
    except:
        pass


try:
    print(f"{Fore.GREEN}Uploading File...\n{Fore.RESET}")
    thread = threading.Thread(target=upload(file))
    thread.start()
except FileNotFoundError:
    print(f"{Fore.LIGHTBLACK_EX}[{Fore.RED}x{Fore.LIGHTBLACK_EX}]{Fore.WHITE} Could not find file.")
    try:
        sys.exit(1)
    except:
        pass

print(f"\n{Fore.GREEN}Uploaded File!{Fore.RESET}")












