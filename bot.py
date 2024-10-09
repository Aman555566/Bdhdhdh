import sys
import time

sys.dont_write_bytecode = True

from orrnob_drops_automation import base
from core.token import get_token
from core.info import get_info
from core.game import process_play_game


class Moonbix:
    def __init__(self):
        # Get file directory
        self.data_file = base.file_path(file_name="data.txt")
        self.config_file = base.file_path(file_name="config.json")
        self.proxy_file = base.file_path(file_name="data.proxy.txt")  # Add proxy file path

        # Initialize line
        self.line = base.create_line(length=50)

    def display_proxy(self):
        # Display active proxy details if found
        try:
            with open(self.proxy_file, "r") as file:
                proxy_data = file.read().strip()
                if proxy_data:
                    base.log(f"\033[92mActive Proxy: \033[97m{proxy_data}")
                else:
                    base.log(f"\033[91mNo active proxy found.")
        except FileNotFoundError:
            base.log(f"\033[91mProxy file not found.")

    def display_custom_banner(self):
        # Unique top banner for "Binance MOONBIX"
        top_banner = f"""
        \033[93m{"="*50}
        \033[91m************ \033[93mBINANCE MOONBIX \033[91m************
        \033[93m{"="*50}\033[0m
        """
        print(top_banner)

        # Custom advertisement banner
        custom_banner = f"""
        \033[96m{"-"*50}
        \033[92mBuy future scripts \033[97m@SPARTEN2009
        \033[92mJoin for update \033[97mhttps://t.me/CrazycryptoYT
        \033[96m{"-"*50}
        \033[0m"""  # \033[0m resets the color
        print(custom_banner)

    def main(self):
        while True:
            base.clear_terminal()
            self.display_custom_banner()

            # Display proxy details
            self.display_proxy()

            data = open(self.data_file, "r").read().splitlines()
            num_acc = len(data)
            base.log(self.line)
            base.log(f"\033[92mNumber of accounts: \033[97m{num_acc}")

            for no, data in enumerate(data):
                base.log(self.line)
                base.log(f"\033[92mAccount number: \033[97m{no+1}/{num_acc}")

                try:
                    token = get_token(data=data)

                    if token:
                        get_info(token=token)
                        process_play_game(token=token)
                        get_info(token=token)
                    else:
                        base.log(f"\033[91mToken Expired! Please get new query id")
                except Exception as e:
                    base.log(f"\033[91mError: \033[97m{e}")

            print()
            wait_time = 30 * 60
            base.log(f"\033[93mWait for {int(wait_time / 60)} minutes!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        moonbix = Moonbix()
        moonbix.main()
    except KeyboardInterrupt:
        sys.exit()
