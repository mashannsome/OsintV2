import requests
from datetime import datetime

target = input("Masukkan IP / Domain: ")

url = f"http://ip-api.com/json/{target}"
data = requests.get(url).json()

for k,v in data.items():
    print(f"{k} : {v}")

filename = f"reports/inspector_{target}.txt"
with open(filename,"w") as f:
    for k,v in data.items():
        f.write(f"{k} : {v}\n")

print("\nReport saved:", filename)
