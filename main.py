import os
from core.ui import header, menu
from modules.phone_osint import scan as phone_scan
from modules.username_osint import scan as username_scan
from modules.telegram_osint import telegram_lookup
from external.run_maigret import run as maigret_run
from external.run_holehe import run as holehe_run
from core.reporter import save as save_report

while True:
    os.system("clear")
    header("OSINT V5 ULTIMATE PRO")
    menu()

    c = input("Select: ").strip()

    if c == "1":
        phone = input("Phone: ")
        result = phone_scan(phone)
        if result:
            save_report(result, "Phone Intelligence")

    elif c == "2":
        username = input("Username: ")
        result = username_scan(username)
        if result:
            save_report(result, "Username Scan")

    elif c == "3":
        phone = input("Phone Telegram (+62xxx): ")
        result = telegram_lookup(phone)
        if result:
            save_report(result, "Telegram Lookup")

    elif c == "4":
        username = input("Username: ")
        maigret_run(username)

    elif c == "5":
        email = input("Email: ")
        holehe_run(email)

    elif c == "6":
        import webbrowser
        webbrowser.open("reports/index.html")
        print("Opening dashboard...")

    elif c == "0":
        print("Exit...")
        break

    else:
        print("Menu tidak tersedia")

    input("\nTekan ENTER untuk kembali ke menu...")
