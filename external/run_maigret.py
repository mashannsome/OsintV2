import subprocess

def run():
    username = input("Username: ")
    subprocess.run(["python3", "external/maigret/maigret.py", username])
