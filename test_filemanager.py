from Console_file_manager import start_menu, menu
from unittest.mock import patch, call
import random
import os
import sys
import shutil
import platform
import time

# Тестирование копирования папки
def test_copy():
    print('тестирование п. 3')
    if 'folder_mk' in os.listdir():
        assert start_menu(3) == 'folder_mk_2', 'Копирование папки/файла идет не верно'
    else:
        os.mkdir('folder_mk')
        assert start_menu(3) == 'folder_mk_2', 'Копирование папки/файла идет не верно'
test_copy()

# Тестирование просмотра директории
def test_directory():
    print('тестирование п. 4')
    if 'folder_mk' in os.listdir():
        assert 'folder_mk' in start_menu(4), 'просмотр содержимого рабочей директории не нашел папку'
    else:
        os.mkdir('folder_mk')
        assert 'folder_mk' in start_menu(4), 'просмотр содержимого рабочей директории не нашел папку'
test_directory()

#Тестирование просмотра создателя программы
print('тестирование п. 8')
assert start_menu(8) == 'Создратель программы: Проневич О.Б.', 'Создатель программы выведен неверно'
# assert start_menu(7) == namedtuple(system='Windows', node='NB0294', release='10', version='10.0.18363', machine='AMD64'), 'Информация об операционной системе выведена неверно'



