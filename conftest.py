from paths import *
import os.path
from zipfile import ZipFile
import pytest
import shutil


@pytest.fixture(scope='function', autouse=True)
def create_zip_file():
    if not os.path.exists(TMP_DIR):  # проверяем существует ли папка
        os.mkdir(TMP_DIR)  # создаем папку если её нет
    with ZipFile(ARCHIVE, 'w') as zip_file:
        for file in files:
            add_file = os.path.join(FILES_DIR, file)  # склеиваем путь к файлам которые добавляют в архив
            zip_file.write(add_file, os.path.basename(add_file))  # добавляем файл в архив
    yield

    shutil.rmtree(TMP_DIR)  # удаляем папку со всеми файлами и подпапками
