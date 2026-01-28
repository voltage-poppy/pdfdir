import os
import sys



from .convert import convert_dir_text
from .pdf.bookmark import add_bookmark

def read_pdbm_file(pdbm_file_path: str) -> tuple[str, int]:
    offset = 0
    with open(pdbm_file_path, "r", encoding='utf-8') as f:
        first_line = f.readline()
        if first_line.rstrip() == "---":
            while True:
                line = f.readline()
                if line.rstrip() == "---":
                    break
                if line.startswith("offset:"):
                    offset = int(line.split(":")[1].strip())
        dir_text = f.read()
    return dir_text, offset

def load_pdbm(pdbm_file_path):
    # if len(sys.argv) != 2:
    #     print("Usage: pdbm_loader.py <pdbm_file>")
    #     sys.exit(1)
    # pdbm_file_path = sys.argv[1]
    pdf_path = pdbm_file_path[:-5] + ".pdf" if pdbm_file_path.endswith(".pdbm") else pdbm_file_path + ".pdf"

    # Ensure the PDF file exists
    if not os.path.exists(pdf_path):
        print(f"[Error] No such PDF file: {pdf_path}", file=sys.stderr)
        sys.exit(1)


    dir_text, offset = read_pdbm_file(pdbm_file_path)

    index_dict = convert_dir_text(
        dir_text,
        offset=offset,
        level0=None,
        level1=None,
        level2=None,
        level3=None,
        level4=None,
        level5=None,
        other=0,
        level_by_space=True,
    )
    return add_bookmark(pdf_path, index_dict)



if __name__ == "__main__":
    main()
