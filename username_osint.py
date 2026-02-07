import requests
import concurrent.futures
from datetime import datetime

username = input("Masukkan username: ")

sites = {
    "Instagram": f"https://www.instagram.com/{username}",
    "GitHub": f"https://github.com/{username}",
    "TikTok": f"https://www.tiktok.com/@{username}",
    "Twitter": f"https://twitter.com/{username}",
    "Pinterest": f"https://www.pinterest.com/{username}"
}

results = []

def check(site, url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            result = f"[FOUND] {site} -> {url}"
        else:
            result = f"[NOT FOUND] {site}"
    except:
        result = f"[ERROR] {site}"
    print(result)
    results.append(result)

print("\nScanning...\n")

with concurrent.futures.ThreadPoolExecutor() as executor:
    for site, url in sites.items():
        executor.submit(check, site, url)

# save report
filename = f"reports/username_{username}_{datetime.now().strftime('%H%M%S')}.txt"
with open(filename, "w") as f:
    for r in results:
        f.write(r + "\n")

print(f"\nReport saved: {filename}")
