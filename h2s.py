import colorama
from colorama import Fore, Style

print("\n" * 100)

print(Fore.MAGENTA + Style.BRIGHT)
print("""
   / /    //   ) )  //   / / 
     / /    //        //___     
    / /    //        / ___      
   / /    //        //          
__/ /___ ((____/ / //           
               alpha v0.2
""")
print(Fore.BLUE + Style.BRIGHT)
hours = float(input("[+]  Enter hours:"))
seconds = hours * 60 * 60
print(Fore.MAGENTA)
print("[+]  Seconds:", seconds)
print("")
print(Fore.BLUE + "[+]  Bye!")
