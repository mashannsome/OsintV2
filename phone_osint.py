import requests
from datetime import datetime

api_key = input("b82a9f21278d466c5251a0f384ce432b")
phone = input("Nomor HP: ")

url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone}"

data = requests.get(url).json()

for k,v in data.items():
    print(f"{k} : {v}")

filename = f"reports/phone_{phone}.txt"
with open(filename,"w") as f:
    for k,v in data.items():
        f.write(f"{k} : {v}\n")

print("\nReport saved:", filename)
