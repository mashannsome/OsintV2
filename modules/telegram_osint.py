from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest, DeleteContactsRequest
from telethon.tl.types import InputPhoneContact
from colorama import Fore, Style

api_id = 30687090          # isi
api_hash = "88b84f6d22ef565ba8615a6f4d1cb504"    # isi

def telegram_lookup(phone):
    print(Fore.CYAN + "\n[+] Checking Telegram account..." + Style.RESET_ALL)

    with TelegramClient("session", api_id, api_hash) as client:

        contact = InputPhoneContact(
            client_id=0,
            phone=phone,
            first_name="Temp",
            last_name="OSINT"
        )

        result = client(ImportContactsRequest([contact]))

        if result.users:
            user = result.users[0]

            print(Fore.GREEN + "\n===== TELEGRAM FOUND =====")
            print("ID        :", user.id)
            print("Name      :", user.first_name)
            print("Username  :", user.username)
            print("Phone     :", phone)
            print("Bot       :", user.bot)
            print("==========================\n")

            # hapus kontak setelah lookup
            client(DeleteContactsRequest(id=[user.id]))

        else:
            print(Fore.RED + "\nTidak ditemukan akun Telegram atau privasi disembunyikan\n")
