# AutoLOL-login
A Python script designed to streamline the Riot Games login process. It automates opening the Riot Client and provides a quick way to log in to one of three different accounts. Account credentials are kept safe within a password-protected, encrypted archive. This tool is perfect for players who frequently switch between accounts and want to avoid manually entering their login details every time.

<b>Beta version<b>
Key Features
Secure Credential Storage: Your login details for up to three accounts are stored securely within a password-protected 7z archive containing an encrypted JSON file.

Simple GUI: A user-friendly graphical interface (GUI) built with customtkinter allows you to select which account you want to log into.

Automated Login: The script automatically opens the Riot Client, waits for the login screen, and inputs your credentials, saving you from manual entry.

<b>How It Works<b>
Password Prompt: When you run the script, a GUI window will appear, asking for the password to your secure archive.

Account Selection: After a successful password entry, the GUI displays the names of your three accounts.

Client Launch: When you click "Log in" for a chosen account, the script launches the Riot Client.

Credential Entry: The script then uses pyautogui to simulate keyboard presses, entering your username and password into the login fields.

<b>Getting Started<b>
Prerequisites
To run this script, you'll need to have the following installed:

Python 3.x

The required Python libraries. You can install them using pip:
