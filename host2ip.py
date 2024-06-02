import socket
import colorama
from colorama import Fore, Style
print(Fore.MAGENTA + Style.BRIGHT)
print("\n" * 100)
print("""

   / /    //   ) )  //   / / 
     / /    //        //___     
    / /    //        / ___      
   / /    //        //          
__/ /___ ((____/ / //           
               alpha v0.2

""")

print(Fore.BLUE + Style.BRIGHT)
ip = " "

ip = input("Enter Host: " + Fore.MAGENTA)

x = socket.gethostbyname(ip)
print("ip: " + Fore.BLUE, x)
