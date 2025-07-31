# AutoLOL-login
A Python script designed to streamline the Riot Games login process. It automates opening the Riot Client and provides a quick way to log in to one of three different accounts. Account credentials are kept safe within a password-protected, encrypted archive. This tool is perfect for players who frequently switch between accounts and want to avoid manually entering their login details every time.

## Beta version
* max 3 accounts
* wrong password entry bug(program freezes when u enter the wrong password)
*

## Key Features
### Secure Credential Storage:
Your login details for up to three accounts are stored securely within a password-protected 7z archive containing an encrypted JSON file.

### Simple GUI:
 A user-friendly graphical interface (GUI) built with customtkinter allows you to select which account you want to log into.

### Automated Login:
 The script automatically opens the Riot Client, waits for the login screen, and inputs your credentials, saving you from manual entry.

## How It Works
### Password Prompt:
 When you run the script, a GUI window will appear, asking for the password to your secure archive.

### Account Selection:
 After a successful password entry, the GUI displays the names of your three accounts.
 at the moment wrong password entry just freezes the whole program and not giving you second chance. 

### Client Launch:
 When you click "Log in" for a chosen account, the script launches the Riot Client.

### Credential Entry:
 The script then uses pyautogui to simulate keyboard presses, entering your username and password into the login fields.

## Getting Started
Prerequisites

The required Python libraries. You can install them using pip:
* pip install customTkinter py7zr pyautogui

## Configuration
1.  <b> Create the JSON file:</b>You need a JSON file containing your account credentials. The file should be structured like this, with three accounts:
{
  "account_name_1": {
    "username": "your_username_1",
    "password": "your_password_1"
  },
  "account_name_2": {
    "username": "your_username_2",
    "password": "your_password_2"
  },
  "account_name_3": {
    "username": "your_username_3",
    "password": "your_password_3"
  }
}

2. Create the encrypted archive: Use a program 7-Zip to compress your JSON file into a password-protected 7z archive. The script expects this archive to be named passwords.7z and located at the path specified by the archive_path variable in the script.

3. Run the script: Once your passwords.7z file is ready and the script paths are correct, you can run the program.
