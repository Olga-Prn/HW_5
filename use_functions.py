"""
МОДУЛЬ 3
Программа "Личный счет"
"""
import sys
def menu():
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = int(input('Выберите пункт меню '))
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            print('Неверный пункт меню')
        return choice

account = 0 # счет пользователя
purchases = [] # список покупок
summ_buy = 0 # сумма покупок
new_choice = menu()
while True:
    if new_choice == 1:
        account = int(input('Введите сумму для попаления счета '))
        new_choice = menu()
    elif new_choice == 2:
        buy = int(input('Введите сумму покупки '))
        if buy > account:
            print('недостаточно денег')
        else:
            account = account - buy
            purch_ = input('Введите название покупки ')
            summ_buy += buy
            purchases.append(purch_)
        new_choice = menu()
    elif new_choice == 3:
        print('список покупок: ', purchases)
        print('общая стоимость покупок:', summ_buy)
        new_choice = menu()
    elif new_choice == 4:
        break







