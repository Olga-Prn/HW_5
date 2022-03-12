# - создать папку
# после выбора пользователь вводит название папки, создаем её в рабочей директории;
# - удалить (файл/папку)
# после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть;
# - копировать (файл/папку)
# после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;
# - просмотр содержимого рабочей директории
# вывод всех объектов в рабочей папке;

# 1. встроенные модули
import random
import os
import sys
import shutil
import platform
import time
# 2. наши модули
# import famous_persons
# 3. сторонние модули
import django
import numpy

print(os.listdir())
print('__________')
# 3 Меню
def menu():
    while True:
        print('1. создать папку')
        print('2. удалить (файл/папку)')
        print('3. копировать (файл/папку)')
        print('4. просмотр содержимого рабочей директории')
        print('5. посмотреть только папки')
        print('6. посмотреть только файлы')
        print('7. просмотр информации об операционной системе')
        print('8. создатель программы')
        print('9. играть в викторину')
        print('10. мой банковский счет')
        print('11. смена рабочей директории')
        print('12. выход')

        choice = int(input('Выберите пункт меню '))
        if choice in range(1,12,1):
            pass
        elif choice == 12:
            break
        else:
            print('Неверный пункт меню')
        return choice

new_choice = menu()
while True:
    if new_choice == 1: # создать папку
        account = (input('Введите имя новой папки '))
        if not os.path.exists(f'{account}'):
            # сздать папку передаем путь
            os.mkdir(f'{account}')
        else:
            print('такая папка уже есть')
        new_choice = menu()
    elif new_choice == 2: #удалить (файл/папку)
        account = (input('Введите имя папки/файла для удаления '))
        if not os.path.exists(f'{account}'):
            os.mkdir(f'{account}')
        else:
            print('такого объекта нет')
    elif new_choice == 3: #копировать (файл/папку)
        account_1 = (input('Введите имя папки/файла, которую нужно копировать '))
        account_2 = (input('Введите новое имя папки/файла '))
        if os.path.exists(f'{account_1}'):
            path_1 = os.path.join(os.getcwd(), f'{account_1}')
            path_2 = os.path.join(os.getcwd(), f'{account_2}')
            print(path_1)
            if account_1.find('.') == -1: # если папки
                shutil.copytree(path_1, path_2)
            else:
                shutil.copy(path_1,path_2)
        else:
            print('Копировать нечего, такого файла/папки нет')
        time.sleep(3)
        new_choice = menu()
    elif new_choice == 4 : #просмотр содержимого рабочей директории
        print('____________')
        print('просмотр содержимого рабочей директории')
        print(os.listdir())
        print('____________')
        time.sleep(3)
        new_choice = menu()
    elif new_choice == 5: # посмотреть только папки
        for dirpath, dirnames, filenames in os.walk("."):
            # перебрать каталоги
            for dirname in dirnames:
                print("Каталог:", os.path.join(dirpath, dirname))
        time.sleep(3)
        new_choice = menu()
    elif new_choice == 6:  # посмотреть только файлы
        # распечатать все файлы и папки рекурсивно
        for dirpath, dirnames, filenames in os.walk("."):
            for filename in filenames:
                print("Файл:", os.path.join(dirpath, filename))
        time.sleep(3)
        new_choice = menu()
    elif new_choice == 7:  #просмотр информации об операционной системе
        print('____________')
        print('информация об операционной системе')
        print(platform.uname())
        print('____________')
        time.sleep(3)
        new_choice = menu()
    elif new_choice == 8:  #создатель программы
        print('____________')
        print('Создратель программы: Проневич О.Б.')
        print(platform.uname())
        print('____________')
        time.sleep(3)
        new_choice = menu()
    elif new_choice == 9:  #играть в викторину
        print('____________')
        import victory
        # victory
        print('____________')
        time.sleep(3)
        new_choice = menu()
    elif new_choice == 10:  # мой банковский счет
        print('____________')
        import use_functions
        print('____________')
        time.sleep(3)
        new_choice = menu()
    elif new_choice == 11:  # смена рабочей директории
        print('____________')
        new_dir = input('Введите новую директорию ')
        os.chdir(new_dir)
        print('____________')
        time.sleep(3)
        new_choice = menu()
    elif new_choice == 12:  # выход
        break





# # 3 Создание папок и просмотр директории
# for i in range(5):
#     # проверка на существование
#     if not os.path.exists(f'new{i}'):
#         # сздать папку передаем путь
#         os.mkdir(f'new{i}')