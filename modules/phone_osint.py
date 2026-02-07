import requests

api_key = input("b82a9f21278d466c5251a0f384ce432b")
phone = input("Nomor HP: ")

url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone}"

data = requests.get(url).json()

for k,v in data.items():
    print(f"{k} : {v}")
