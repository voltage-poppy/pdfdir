import sys
from src.gui.main import run
from src.pdbm_loader import load_pdbm

if __name__ == "__main__":
    if len(sys.argv) == 2:
        pdbm_file_path = sys.argv[1]
        load_pdbm(pdbm_file_path)
    else:
        run()
