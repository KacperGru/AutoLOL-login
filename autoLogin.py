import json
import getpass
import py7zr
import tempfile
import os
import subprocess
import time
import pyautogui
import tkinter
import customtkinter
from tkinter import messagebox

archive_path = r"C:\Users\kubag\Desktop\skrypt\passwords.7z"
riot_client_path = r"C:\Riot Games\Riot Client\RiotClientServices.exe"


def loginCredentials(archivePath, archivePassword):

    try:
        with py7zr.SevenZipFile(archivePath, mode = "r", password=archivePassword) as archive: #opening a archive that contains a json file 
            archiveJsonFiles = archive.getnames() 
            passwordsFile = archiveJsonFiles[0]
            
            with tempfile.TemporaryDirectory() as td: #creating temp directory
                temp_dir = td
                print(temp_dir)
                archive.extract(targets=[passwordsFile], path=temp_dir) #extracting archive to a temp directory
                extractedJsonFile = os.path.join(temp_dir, passwordsFile) #a path to extracted file 
                with open(extractedJsonFile, "r", encoding="utf-8") as json_file: #opening a file that contains logins and passwords to all accounts 
                    json_string = json_file.read()
                    global accounts
                    accounts = json.loads(json_string)
                    global accounts_names
                    accounts_names = list(accounts.keys()) #all accounts names from the JSON file 
                    #selected account credentials
    except:
        print("Wrong password")
        return False               

def selectingacc(accountName):
    selected_acc = accounts[accountName]
    global acc_login
    global acc_password
    acc_login = selected_acc["username"]
    acc_password = selected_acc["password"]
                        

    

            
        


#enteredPassword = getpass.getpass("Enter password to passwords file...")


def launchLeague():

    # arguments to auto start league of legends
    lol_arguments = ["--launch-product=league_of_legends","--launch-patchline=live"]
    lol_argumentscmd = subprocess.list2cmdline(lol_arguments)
    flags = subprocess.CREATE_NO_WINDOW | subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS
    command = f'start "" "{riot_client_path}" {lol_argumentscmd}'
    print(command)
    process = subprocess.Popen(command, shell=True, creationflags=flags)
    

    print(f"riot client is starting PID: {process.pid}")
    time.sleep(1)
    print("waiting for client fully open...")


def enterCredentials(login, password):
    pyautogui.write(login)
    pyautogui.keyDown("TAB")
    pyautogui.write(password)
    time.sleep(0.1)
    pyautogui.press("ENTER")


def programPassword(password):
    is_pass_right = loginCredentials(archive_path,password)
    while True:

        if  is_pass_right != False:
            loginFrame.destroy()
            firstAccountName = customtkinter.CTkLabel(innerFrame, text=accounts_names[0], font=customtkinter.CTkFont(size=20, weight="bold"), text_color="white", height=100, width=100, fg_color=gray,bg_color=gray)
            firstAccountButton = customtkinter.CTkButton(innerFrame, text="Log in",command=lambda: programStart(accounts_names[0]),font=customtkinter.CTkFont(size=18, weight="bold"),text_color="white", height=20, width=100, fg_color="gray25", bg_color=gray, corner_radius=10)

            secondAccountName = customtkinter.CTkLabel(innerFrame, text=accounts_names[1], font=customtkinter.CTkFont(size=20, weight="bold"), text_color="white",height=100, width=100,fg_color=gray,bg_color=gray)
            secondAccountButton = customtkinter.CTkButton(innerFrame, text="Log in",command=lambda: programStart(accounts_names[1]), font=customtkinter.CTkFont(size=18, weight="bold"),text_color="white", height=20, width=100, fg_color="gray25", bg_color=gray, corner_radius=10)

            thirdAccountName = customtkinter.CTkLabel(innerFrame, text=accounts_names[2], font=customtkinter.CTkFont(size=20, weight="bold"), text_color="white",height=100, width=100,fg_color=gray,bg_color=gray)
            thirdAccountButton = customtkinter.CTkButton(innerFrame, text="Log in",command=lambda: programStart(accounts_names[2]), font=customtkinter.CTkFont(size=18, weight="bold"),text_color="white", height=20, width=100, fg_color="gray25", bg_color=gray, corner_radius=10)

            firstAccountName.grid(row=0, column=0, padx=80)
            firstAccountButton.grid(row=1, column=0, padx=80, pady=100)

            secondAccountName.grid(row=0, column=1, padx=80)
            secondAccountButton.grid(row=1, column=1, padx=80, pady=100)

            thirdAccountName.grid(row=0, column=2, padx=80)
            thirdAccountButton.grid(row=1, column=2, padx=80, pady=100)
            break
        else:
            continue



def programStart(acc_name):
    selectingacc(acc_name)
    launchLeague()
    time.sleep(12)
    enterCredentials(acc_login, acc_password)
    time.sleep(10)
    quit()
    


app = customtkinter.CTk()
app.title("AutoLogin")
app.geometry("800x450")
app.resizable(0,0)

gray = "#63686A"

app._set_appearance_mode("dark")
app.configure(fg_color="gray10")
mainFrame = customtkinter.CTkFrame(app, fg_color="gray10", bg_color="gray10", width=700, height=350)
mainFrame.pack(fill="both", expand=True, padx=0, pady=0)
innerFrame = customtkinter.CTkFrame(mainFrame, fg_color=gray, bg_color="gray10", width=600, height=300)
innerFrame.pack(fill="both",expand=True, padx=20, pady=70)
loginFrame = customtkinter.CTkFrame(innerFrame, fg_color="gray15", bg_color=gray, width=300, height=260, corner_radius=20)
loginFrame.pack(expand=False, padx=50, pady=30)



#title of the app
title = customtkinter.CTkLabel(mainFrame,text="AutoLOL-Login",
                            font=customtkinter.CTkFont(size=24, weight="bold"),
                            text_color="white",
                            fg_color= "gray20",
                            bg_color="gray10",
                            corner_radius=10,
                            pady=5
                            )
title.place(relx=0.5, y=30, anchor="center")



    
def printpass():
    print(passwordInput.get())


passwordInput = customtkinter.CTkEntry(loginFrame,show="*", placeholder_text="password",font=customtkinter.CTkFont(size=20, weight="bold"), text_color="white",height=40, width=200,fg_color=gray,bg_color="gray15")
passwordInput.place(rely= 0.35, relx= 0.5, anchor="center")

passwordInputButton = customtkinter.CTkButton(loginFrame, text="Confirm",command=lambda: programPassword(passwordInput.get()),font=customtkinter.CTkFont(size=18, weight="bold"),text_color="white", height=20, width=100, fg_color="gray40", bg_color="gray15", corner_radius=10)
passwordInputButton.place(rely=0.6, relx=0.5, anchor="center")



app.mainloop()







