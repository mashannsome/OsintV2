import subprocess

def run():
    email = input("Email: ")
    subprocess.run(["holehe", email])
