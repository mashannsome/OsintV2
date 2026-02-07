import os
import shutil

def ensure_maigret():
    if shutil.which("maigret") is None:
        print("[+] Maigret belum terinstall, installing...")
        os.system("pip install maigret")

def run(username):
    ensure_maigret()
    os.system(f"maigret {username} --html reports/{username}_maigret.html")
