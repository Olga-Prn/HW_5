# Тестируем функцию filter
import math
def test_1_filter():
    num = [1, 2.0, 3.1, 4, 5, 6, 7.9]
    assert list(filter(lambda x: x > 4, num)) == [5, 6, 7.9], 'Ошибка в фильтрации по условию "больше"'
    assert list(filter(lambda x: x > 8, num)) == [], 'Ошибка в фильтрации по условию "больше". Не пустой список'

def test_2_filter():
    num = [1, 2.0, 3.1, 4, 5, 6, 7.9]
    assert list(filter(lambda x: type(x) is int, num)) == [1, 4, 5, 6], 'Ошибка в фильтрации по типу'

def test_3_filter():
    num = list(range(0, 27))
    def ff(x):
        if x > 18 and not x % 2:
            return True
        else:
            return False
    assert list(filter(ff, num)) == [20, 22, 24, 26], 'Ошибка в фильтрации по фунции "больше и четное"'

# Тестируем функцию map
def test_1_map():
    numbers = [-2, -1, 0, 1, 2]
    assert list(map(abs, numbers)) == [2, 1, 0, 1, 2], 'Ошибка в приведении к abc'

def test_2_map():
    numbers = [-2, -1, 0, 1, 2]
    assert list(map(float, numbers)) == [-2.0, -1.0, 0.0, 1.0, 2.0], 'Ошибка в приведении к float'

def test_3_map():
    numbers = [1, 2, 3, 4, 5]
    assert map(lambda num: num ** 2, numbers) == [1, 4, 9, 16, 25], 'Ошибка в возведении в квадрат'

def test_3_map():
    first_it = [1, 2, 3]
    second_it = [4, 5, 6, 7]
    assert list(map(pow, first_it, second_it)) == [1, 32, 729], 'Ошибка в применении pow при итерациях'

def test_1_sorted():
    def funcSort(x):
        return x % 2
    a = [1, 4, 3, 6, 5, 2]
    assert sorted(a, key=funcSort) == [4, 6, 2, 1, 3, 5], 'Сортировке по четности'

def test_2_sorted():
    def funcSort(x):
        if x % 2 == 0:
            return x
        else:
            return x + 100
    a = [1, 4, 3, 6, 5, 2]
    assert sorted(a, key=funcSort) == [2, 4, 6, 1, 3, 5], 'Сортировке по четности и возрастанию'

def test_3_sorted():
    lst = ["Москва", "Тверь", "Смоленск", "Псков", "Рязань"]
    assert sorted(lst, key=lambda x: x[0]) == ['Москва', 'Псков', 'Рязань', 'Смоленск', 'Тверь'], 'Ошибка стортировки строки по первому символу'

def test_math_pi_1():
    assert round(math.pi) == 3, 'Округление до целого неправильно'
def test_math_pi_2():
    assert round(math.pi,4) == 3.1416, 'Округление до 4 знака неправильно'
def test_math_pi_2():
    assert isinstance(math.pi, float) == True, 'Ошибка в типе'

def test_math_sqrt_1():
    num = 25
    assert math.sqrt(num) == 5, 'Ошибка в извлечении квадратного корня из 25'

def test_math_pow_1():
    assert pow(3, 2) == 9
def test_math_pow_2():
    assert pow(10, 3) == 1000
def test_math_pow_3():
    assert pow(5, -3) == 0.008

def test_math_hypot_1():
    assert math.hypot(-2, 0) == 2.0, 'Ошибка в вычислении гипотенузы'

def test_math_hypot_1():
    assert round(math.hypot(4, 1)) == 4, 'Ошибка в вычислении гипотенузы'

