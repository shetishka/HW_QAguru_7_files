import os

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, "tmp")
ARCHIVE = os.path.join(TMP_DIR, "ARCH.zip")
# FILES_DIR = os.path.join(CURRENT_DIR +'\\files_for_zip', 'files')
FILES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files_for_zip')

files = ['CSV_file.csv', 'file_example_XLSX_50.xlsx', 'Polozhenie_Pesni_Dlya_Vsekh_2024.pdf']



