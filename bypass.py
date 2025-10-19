from subprocess import check_output
from getpass import getpass
import requests
import os

os.chdir('C:\\Windows\\Panther')

# Download Unattended.xml
url = 'https://github.com/blusewill/oobe-bypass/releases/download/0.0.1/autounattend.xml'

r = requests.get(url, allow_redirects=True)

open('unattend.xml', 'wb').write(r.content)

while True:
    # Setup the Offline Account
    UserAccount = input("Please input your User Account Name: ")
    UserPassword = getpass("Please Input Your Account Password: ")
    UserPasswordConfirm = getpass("Please confirm your Password: ")

    if not UserAccount:
        UserAccount = "Owner"
        print("Account Name not detected... Defaulting to Owner")

    if not UserPassword:
        print(f"Account Name : {UserAccount}")
        print("Password Set? : False")
    elif UserPassword == UserPasswordConfirm:
        print(f"Account Name : {UserAccount}")
        print("Password Set? : True")
    else:
        print("Password is not identical, restarting...")
        continue

    # Confirm The User Information
    while True:
        confirm_input = input("Is the following information Correct? (yes/no)")

        if confirm_input.lower() in ["y", "yes"]:
            break
        elif confirm_input.lower() in ["n", "no"]:
            break
        else:
            continue

    if confirm_input.lower() in ["y", "yes"]:
        break
    else:
        continue

# Editing Unattend.xml

with open("unattend.xml", "r") as file:
    data = file.read()
    data = data.replace("ReplaceThisUsername", UserAccount)
    data = data.replace("ReplaceThisPassword", UserPassword)

with open("unattend.xml", "w") as file:
    file.write(data)

# Running the unattend.xml patch
check_output(
    "C:\\Windows\\System32\\Sysprep\\sysprep.exe /oobe /unattend:C:\\Windows\\Panther\\unattend.xml /reboot", shell=True)
