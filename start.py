from getpass import getpass
import os

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

    if UserPassword == UserPasswordConfirm:
        print(f"Account Name : {UserAccount}")
        print("Password Set? : True")
    else:
        print("Password is not identical, restarting...")
        continue

    # Confirm The User Information
    while True:
        confirm_input = input("Is the Following information Correct? (yes/no)")

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
