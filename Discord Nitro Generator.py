import random
import string
import requests
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
f=open("Nitro Code.txt", "w", encoding='utf-8')
while True:
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
    if r.status_code == 200:
        print(f"Gyzby#3023 [Succest] Valid Nitro Code > discord.gift/{code}")
        f.write(f"discord.gift/{code}\n")
    else:
        print(f"Gyzby#3023 [Fatal] Invalid Nitro Code > discord.gift/{code}")  
