from scans import REGISTRY as SCANNERS
from utils.ui import banner, print_menu
from colorama import Fore, Style
from utils.logs_config import get_logger
logger = get_logger()


def get_choice():

    raw = input(f" nmap-engine > Select a module [1-{len(SCANNERS) + 1}]: ").strip()

    if not raw.isdigit():
        print(Fore.RED, f"[!] '{raw}' is not a valid number. Please try again.", Style.RESET_ALL)
        return None

    choice = int(raw)

    if not (1 <= choice <= len(SCANNERS) + 1):
        print(Fore.RED, f"[!] Please enter a number between 1 and {len(SCANNERS) + 1}.", Style.RESET_ALL)
        return None

    return choice

def main():
    while True:
        banner()

        print_menu()

        choice = get_choice()

        if choice is None:
            input("\n Press Enter to try again...")
            print("\033[H\033[J", end="")
            continue

        if choice == len(SCANNERS) + 1:
            print(Fore.RED, "\n [+] Exiting toolkit framework gracefully. Goodbye.\n", Style.RESET_ALL)
            logger.info("Exiting NmapEngine framework gracefully.")
            break

        scanner = SCANNERS[choice - 1]
        target = input(f" nmap-engine > Target IP / Domain: ").strip()

        print(Fore.LIGHTMAGENTA_EX, f"\n[*] Running {scanner.name} against '{target}'...\n", Style.RESET_ALL)
        logger.info(f"Running {scanner.name} against '{target}'...")
        output = scanner.run(target)

        if output:
            print(Fore.GREEN, "[+] SCAN COMPLETE - RESULTS RETURNED ↴\n", Style.RESET_ALL)
            logger.info("Scan Completed")
            print(output)
        else:
            print(Fore.RED, "[-] SCAN TERMINATED: No data received or execution failed.", Style.RESET_ALL)
            logger.error("SCAN TERMINATED: No data received or execution failed")
            print("     (Check system log for debug metrics)")


if __name__ == "__main__":
    main()