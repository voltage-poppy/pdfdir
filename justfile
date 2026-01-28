build:
    uv sync
    uv run pyinstaller -D run_gui.py -i "pdf.ico" --exclude config.ini --distpath . -n "pdfdir" --noconfirm --noconsole
