
from sys import platform
import Config, time, os, random
from consolemenu import *
from consolemenu.items import *
from colorama import Fore
import Lib.SenditLib as SenditLib

if platform == "linux" or platform == "linux2": # banner system
    os.system("clear")
elif platform == "win32":
    os.system("cls")
print("                _                 _                ")
time.sleep(0.2)
print(" /_/   __   _  /_`_  _   _/._/_  /_)_  _ _  /_ _  _")
time.sleep(0.2)
print("/`\/_///_/_\  ._//_'/ //_// /   /_)/_// / //_//_'/ ")
time.sleep(0.8)
print(f"\n\nWelcome To Kuros Sendit Bomber, made with python. OS ==> {platform}")
time.sleep(3)

Sendit = SenditLib.SenditLib
"""
   _____                        _           _     ______                _   _                 
  / ____|                      | |         | |   |  ____|              | | (_)                
 | (___  _ __   __ _ _ __   ___| |__   __ _| |_  | |__ _   _ _ __   ___| |_ _  ___  _ __  ___ 
  \___ \| '_ \ / _` | '_ \ / __| '_ \ / _` | __| |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
  ____) | | | | (_| | |_) | (__| | | | (_| | |_  | |  | |_| | | | | (__| |_| | (_) | | | \__ \
 |_____/|_| |_|\__,_| .__/ \___|_| |_|\__,_|\__| |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
                    | |                                                                       
                    |_|                                                                       
"""

def SnapchatBombSenditRotatingMessageTime():
    ConfigCorrectYN = input(Fore.RED + f"\n\nIs this config correct?\nTarget Link ID ==> {Config.TarLinkID}\nTarget App ID ==> {Config.TarAppID}\nTarget Recipient ID ==> {Config.TarRecipientID}\nTarget Shadow Token ==> {Config.TarShadowToken}\nY/N: ")
    if ConfigCorrectYN == "y" or "Y": 
        print("Starting...")
    elif ConfigCorrectYN == "n" or "N": 
        print("Exiting...")
        exit(0)
    else: print("Invalid Option")

    for gg in range(Config.TimeToRun):
        MessageToSend = random.choice(open("Messages.txt").read().splitlines())
        
        try:
            Sendit.send_snap_message(Config.TarLinkID, Config.TarAppID, Config.TarRecipientID, Config.TarShadowToken, MessageToSend)   
        except: print(Fore.RED + "Error Sending Message. Try Again Later Please.")
        time.sleep(0.4)
        
    print(Fore.GREEN + f"Done!")
    time.sleep(5)

def SnapchatBombSenditRotatingMessageAndAmount():
    ConfigCorrectYN = input(Fore.RED + f"\n\nIs this config correct?\nTarget Link ID ==> {Config.TarLinkID}\nTarget App ID ==> {Config.TarAppID}\nTarget Recipient ID ==> {Config.TarRecipientID}\nTarget Shadow Token ==> {Config.TarShadowToken}\nAmount to Send ==> {Config.AmountToSend}\nY/N: ")
    if ConfigCorrectYN == "y" or "Y": 
        print("Starting...")
    elif ConfigCorrectYN == "n" or "N": 
        print("Exiting...")
        exit(0)
    else: print("Invalid Option")

    for gg in range(Config.AmountToSend):
        MessageToSend = random.choice(open("Messages.txt").read().splitlines())
        
        try:
            Sendit.send_message(Config.TarLinkID, Config.TarAppID, Config.TarRecipientID, Config.TarShadowToken, MessageToSend)   
        except: print(Fore.RED + "Error Sending Message. Try Again Later Please.")
        time.sleep(0.2)
        
    print(Fore.GREEN + f"Done!")
    time.sleep(5)

def SnapchatBombSenditRotatingMessageUntilExit():
    ConfigCorrectYN = input(Fore.RED + f"\n\nIs this config correct?\nTarget Link ID ==> {Config.TarLinkID}\nTarget App ID ==> {Config.TarAppID}\nTarget Recipient ID ==> {Config.TarRecipientID}\nTarget Shadow Token ==> {Config.TarShadowToken}\nY/N: ")
    if ConfigCorrectYN == "y" or "Y": 
        print("Starting...")
    elif ConfigCorrectYN == "n" or "N": 
        print("Exiting...")
        exit(0)
    else: print("Invalid Option")
    inf = 9999999
    for gg in range(inf):
        MessageToSend = random.choice(open("Messages.txt").read().splitlines())
        try:
            Sendit.send_snap_message(Config.TarLinkID, Config.TarAppID, Config.TarRecipientID, Config.TarShadowToken, MessageToSend)   
        except: print(Fore.RED + "Error Sending Message. Try Again Later Please.")
        time.sleep(0.2)
        
    print(Fore.GREEN + f"Done!")
    time.sleep(5)

def SnapchatBombSenditSingleMessage():
    ConfigCorrectYN = input(Fore.RED + f"\n\nIs this config correct?\nTarget Link ID ==> {Config.TarLinkID}\nTarget App ID ==> {Config.TarAppID}\nTarget Recipient ID ==> {Config.TarRecipientID}\nTarget Shadow Token ==> {Config.TarShadowToken}\nY/N: ")
    if ConfigCorrectYN == "y" or "Y": 
        print("Starting...")
    elif ConfigCorrectYN == "n" or "N": 
        print("Exiting...")
        exit(0)
    else: print("Invalid Option")

    try:
        Sendit.send_snap_message(Config.TarLinkID, Config.TarAppID, Config.TarRecipientID, Config.TarShadowToken, Config.SingleMessage)   
    except: print(Fore.RED + "Error Sending Message. Try Again Later Please.")
    time.sleep(0.4)
        
    print(Fore.GREEN + f"Done!")
    time.sleep(5)

def SnapchatBombSendit():
    ConfigCorrectYN = input(Fore.RED + f"\n\nIs this config correct?\nTarget Link ID ==> {Config.TarLinkID}\nTarget App ID ==> {Config.TarAppID}\nTarget Recipient ID ==> {Config.TarRecipientID}\nTarget Shadow Token ==> {Config.TarShadowToken}\nAmount to Send ==> {Config.AmountToSend}\nY/N: ")
    if ConfigCorrectYN == "y" or "Y": 
        print("Starting...")
    elif ConfigCorrectYN == "n" or "N": 
        print("Exiting...")
        exit(0)
    else: print("Invalid Option")

    try:
        Sendit.send_snap_message(Config.TarLinkID, Config.TarAppID, Config.TarRecipientID, Config.TarShadowToken, Config.SingleMessage)   
    except: print(Fore.RED + "Error Sending Message. Try Again Later Please.")
    time.sleep(0.4)
        
    print(Fore.GREEN + f"Done!")
    time.sleep(5)

"""
  ______           _    _____                        _           _     ______                _   _                 
 |  ____|         | |  / ____|                      | |         | |   |  ____|              | | (_)                
 | |__   _ __   __| | | (___  _ __   __ _ _ __   ___| |__   __ _| |_  | |__ _   _ _ __   ___| |_ _  ___  _ __  ___ 
 |  __| | '_ \ / _` |  \___ \| '_ \ / _` | '_ \ / __| '_ \ / _` | __| |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 | |____| | | | (_| |  ____) | | | | (_| | |_) | (__| | | | (_| | |_  | |  | |_| | | | | (__| |_| | (_) | | | \__ \
 |______|_| |_|\__,_| |_____/|_| |_|\__,_| .__/ \___|_| |_|\__,_|\__| |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
                                         | |                                                                       
                                         |_|                                                                       
"""
# ======================================================================================================================
# ======================================================================================================================
"""
  _____           _                                    ______                _   _                 
 |_   _|         | |                                  |  ____|              | | (_)                
   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |__ _   _ _ __   ___| |_ _  ___  _ __  ___ 
   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
  _| |_| | | \__ \ || (_| | (_| | | | (_| | | | | | | | |  | |_| | | | | (__| |_| | (_) | | | \__ \
 |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
                            __/ |                                                                  
                           |___/                                                                   
"""



def InstagramBombSenditRotatingMessageTime():
    ConfigCorrectYN = input(Fore.RED + f"\n\nIs this config correct?\nTarget Link ID ==> {Config.TarLinkID}\nTarget App ID ==> {Config.TarAppID}\nTarget Recipient ID ==> {Config.TarRecipientID}\nTarget Shadow Token ==> {Config.TarShadowToken}\nY/N: ")
    if ConfigCorrectYN == "y" or "Y": 
        print("Starting...")
    elif ConfigCorrectYN == "n" or "N": 
        print("Exiting...")
        exit(0)
    else: print("Invalid Option")

    for gg in range(Config.TimeToRun):
        MessageToSend = random.choice(open("Messages.txt").read().splitlines())
        
        try:
            Sendit.send_insta_message(Config.TarLinkID, Config.TarAppID, Config.TarRecipientID, Config.TarShadowToken, MessageToSend)   
        except: print(Fore.RED + "Error Sending Message. Try Again Later Please.")
        time.sleep(0.4)
        
    print(Fore.GREEN + f"Done!")
    time.sleep(5)

def InstagramBombSenditRotatingMessageAndAmount():
    ConfigCorrectYN = input(Fore.RED + f"\n\nIs this config correct?\nTarget Link ID ==> {Config.TarLinkID}\nTarget App ID ==> {Config.TarAppID}\nTarget Recipient ID ==> {Config.TarRecipientID}\nTarget Shadow Token ==> {Config.TarShadowToken}\nAmount to Send ==> {Config.AmountToSend}\nY/N: ")
    if ConfigCorrectYN == "y" or "Y": 
        print("Starting...")
    elif ConfigCorrectYN == "n" or "N": 
        print("Exiting...")
        exit(0)
    else: print("Invalid Option")

    for gg in range(Config.AmountToSend):
        MessageToSend = random.choice(open("Messages.txt").read().splitlines())
        
        try:
            Sendit.send_insta_message(Config.TarLinkID, Config.TarAppID, Config.TarRecipientID, Config.TarShadowToken, MessageToSend)   
        except: print(Fore.RED + "Error Sending Message. Try Again Later Please.")
        time.sleep(0.4)
        
    print(Fore.GREEN + f"Done!")
    time.sleep(5)

def InstagramBombSenditRotatingMessageUntilExit():
    ConfigCorrectYN = input(Fore.RED + f"\n\nIs this config correct?\nTarget Link ID ==> {Config.TarLinkID}\nTarget App ID ==> {Config.TarAppID}\nTarget Recipient ID ==> {Config.TarRecipientID}\nTarget Shadow Token ==> {Config.TarShadowToken}\nY/N: ")
    if ConfigCorrectYN == "y" or "Y": 
        print("Starting...")
    elif ConfigCorrectYN == "n" or "N": 
        print("Exiting...")
        exit(0)
    else: print("Invalid Option")
    inf = 9999999
    for gg in range(inf):
        MessageToSend = random.choice(open("Messages.txt").read().splitlines())
        try:
            Sendit.send_insta_message(Config.TarLinkID, Config.TarAppID, Config.TarRecipientID, Config.TarShadowToken, MessageToSend)   
        except: print(Fore.RED + "Error Sending Message. Try Again Later Please.")
        time.sleep(0.2)
        
    print(Fore.GREEN + f"Done!")
    time.sleep(5)

def InstagramBombSenditSingleMessage():
    ConfigCorrectYN = input(Fore.RED + f"\n\nIs this config correct?\nTarget Link ID ==> {Config.TarLinkID}\nTarget App ID ==> {Config.TarAppID}\nTarget Recipient ID ==> {Config.TarRecipientID}\nTarget Shadow Token ==> {Config.TarShadowToken}\nY/N: ")
    if ConfigCorrectYN == "y" or "Y": 
        print("Starting...")
    elif ConfigCorrectYN == "n" or "N": 
        print("Exiting...")
        exit(0)
    else: print("Invalid Option")

    try:
        Sendit.send_insta_message(Config.TarLinkID, Config.TarAppID, Config.TarRecipientID, Config.TarShadowToken, Config.SingleMessage)   
    except: print(Fore.RED + "Error Sending Message. Try Again Later Please.")
    time.sleep(0.4)
        
    print(Fore.GREEN + f"Done!")
    time.sleep(5)

def InstagramBombSendit():
    ConfigCorrectYN = input(Fore.RED + f"\n\nIs this config correct?\nTarget Link ID ==> {Config.TarLinkID}\nTarget App ID ==> {Config.TarAppID}\nTarget Recipient ID ==> {Config.TarRecipientID}\nTarget Shadow Token ==> {Config.TarShadowToken}\nAmount to Send ==> {Config.AmountToSend}\nY/N: ")
    if ConfigCorrectYN == "y" or "Y": 
        print("Starting...")
    elif ConfigCorrectYN == "n" or "N": 
        print("Exiting...")
        exit(0)
    else: print("Invalid Option")
    inf = 9999999
    for gg in range(inf):
        try:
            Sendit.send_insta_message(Config.TarLinkID, Config.TarAppID, Config.TarRecipientID, Config.TarShadowToken, Config.SingleMessage)   
        except: print(Fore.RED + "Error Sending Message. Try Again Later Please.")
        time.sleep(0.4)
        
    print(Fore.GREEN + f"Done!")
    time.sleep(5)


"""
  ______           _   _____           _                                    ______                _   _                 
 |  ____|         | | |_   _|         | |                                  |  ____|              | | (_)                
 | |__   _ __   __| |   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |__ _   _ _ __   ___| |_ _  ___  _ __  ___ 
 |  __| | '_ \ / _` |   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 | |____| | | | (_| |  _| |_| | | \__ \ || (_| | (_| | | | (_| | | | | | | | |  | |_| | | | | (__| |_| | (_) | | | \__ \
 |______|_| |_|\__,_| |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
                                                 __/ |                                                                  
                                                |___/                                                                   
"""
# Create the menu
menu = ConsoleMenu(Fore.RED + "Kuro's Sendit Bomber", Fore.RED + "@dev_kuro -- im-kuro")

# SNAPCHAT MENU
SnapchatBombSenditRotatingMessageTime_item = FunctionItem(Fore.YELLOW + "Bomb Snapchat Sendit With Rotating Messages and a Time Limit", function=SnapchatBombSenditRotatingMessageTime)
SnapchatBombSenditRotatingMessageAndAmount_item = FunctionItem(Fore.YELLOW +  "Bomb Snapchat Sendit With Rotating Messages and Amount to Send", function=SnapchatBombSenditRotatingMessageAndAmount)
SnapchatBombSenditRotatingMessageUntilExit_item = FunctionItem(Fore.YELLOW +  "Bomb Snapchat Sendit Until User Exit", function=SnapchatBombSenditRotatingMessageUntilExit)
SnapchatBombSenditSingleMessage_item = FunctionItem(Fore.YELLOW +  "Send a Single Message to Snapchat Sendit User", function=SnapchatBombSenditSingleMessage)
SnapchatBombSendit_item = FunctionItem(Fore.YELLOW +  "Bomb Snapchat Sendit", function=SnapchatBombSendit)

menu.append_item(SnapchatBombSenditRotatingMessageTime_item)
menu.append_item(SnapchatBombSenditRotatingMessageAndAmount_item)
menu.append_item(SnapchatBombSenditRotatingMessageUntilExit_item)
menu.append_item(SnapchatBombSenditSingleMessage_item)
menu.append_item(SnapchatBombSendit_item)

# INSTAGRAM MENU

InstagramSenditRotatingMessageTime_item = FunctionItem(Fore.MAGENTA + "Bomb Instagram Sendit With Rotating Messages and a Time Limit", function=InstagramBombSenditRotatingMessageTime)
InstagramSenditRotatingMessageAndAmount_item = FunctionItem(Fore.MAGENTA +  "Bomb Instagram Sendit With Rotating Messages and Amount to Send", function=InstagramBombSenditRotatingMessageAndAmount)
InstagramSenditRotatingMessageUntilExit_item = FunctionItem(Fore.MAGENTA +  "Bomb Instagram Sendit Until User Exit", function=InstagramBombSenditRotatingMessageUntilExit)
InstagramSenditSingleMessage_item = FunctionItem(Fore.MAGENTA +  "Send a Single Message to Instagram Sendit User", function=InstagramBombSenditSingleMessage)
InstagramSendit_item = FunctionItem(Fore.MAGENTA +  "Bomb Instagram Sendit", function=InstagramBombSendit)

menu.append_item(InstagramSenditRotatingMessageTime_item)
menu.append_item(InstagramSenditRotatingMessageAndAmount_item)
menu.append_item(InstagramSenditRotatingMessageUntilExit_item)
menu.append_item(InstagramSenditSingleMessage_item)
menu.append_item(InstagramSendit_item)
# Finally, we call show to show the menu and allow the user to interact
menu.show()
