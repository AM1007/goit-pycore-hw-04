from pathlib import Path
from printout import print_out

def scan_dir(directory: Path, tabs: str=""):
    print_out("dir", f"{tabs}{directory.name}\\")
    tabs += "    "
    for path in directory.iterdir():
        if (path.is_dir()):
            scan_dir(path, tabs)
        elif (path.is_file()):
            print_out("file", f"{tabs}{path.name}")
        else:
            print_out("",f"{tabs}Unknown entity")