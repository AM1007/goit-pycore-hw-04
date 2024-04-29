import sys
from pathlib import Path
from scan import scan_dir

def main():
    if len(sys.argv) > 1:
        root_dir = Path(sys.argv[1])
        if (not root_dir.exists() or not root_dir.is_dir()):
            print("Not directory or does not exitsts")
            return
        scan_dir(root_dir)

if __name__ == "__main__":
    main()