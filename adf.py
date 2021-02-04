# VK = "https://vk.com/your.are.a.loser"

import requests
import time
import sys
import os

os.system('color 6 && clear')

print("")
print("++++++++++++++++++++++++++++++++++++++++++")
print("+              ADMIN                     +")
print("+              PANEL                     +")
print("+              FINDER                    +")
print("+              by  z5mv1                 +")
print("+ VK = https://vk.com/your.are.a.loser   +")
print("++++++++++++++++++++++++++++++++++++++++++")


def usage():
    print("")
    print(" Use | python apf.py https://site.com")


if len(sys.argv) >= 2:
    print("\n[+] Script is running...\n")
    adm_list = ["admin.php", "admin.html", "adm", "index.php", "login.php",
                "administrator", "admin", "adminpanel", "cpanel", "admins",
                "logins", "admin.asp", "login.asp", "adm/", "admin/account.html"
        , "admin/login.html", "admin/login.htm", "admin/controlpanel.html", "admin/controlpanel.htm",
                "admin/adminLogin.html", "admin/adminLogin.htm", "admin.htm"]
    try:
        for i in adm_list:
            url = sys.argv[1] + 1
            r = requests.get(url)
            sys.stdout.flush()
            if r.status_code == 200:
                print(" [+] page found : " + url)
            else:
                print("[-] page not found : " + url)
                print("\n[-] End time: %s" % time.strftime('%H:%M%S'))
    except KeyboardInterrupt:
        print("[x] Script off")
        pass
    except:
        print("\n[x] An error has occurred")
        print(
            "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\n[-] Disclaimer : The site may contain some protection, may be unavailable, or enter this")
        print(
            "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
else:
    usage()
