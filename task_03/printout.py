from colorama import Fore

print_colors = {
    "dir": Fore.BLUE,
    "file": Fore.GREEN,
    "": Fore.WHITE,
}

def print_out(type: str, line: str):
    print(f"{print_colors.get(type)}{line}{Fore.RESET}")