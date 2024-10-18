# Нахождение данных для диаграммы Тьюки

# Функция для взаимодействия с пользователем
def user_input():
    print('Введите набор чисел, разделенных пробелами: ')
    user_input=input()
    return [float(x) for x in user_input.split()]

# Функция для сортировки списка данных (используем метод quick_sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    tochka = arr[0]
    #массив чисел делится на три части: больше(greater) значения tochka, меньше(less), равный(equal)
    greater = [x for x in arr[1:] if x > tochka]
    less = [x for x in arr[1:] if x < tochka]
    equal = [x for x in arr if x == tochka]
    return quick_sort(less) + equal + quick_sort(greater)

# Функция для расчета медианы
def median(arr):
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]

# Функция для расчета мат. ожидания
def mu(arr):
    n = len(arr)
    return sum(arr) / n

# Функция для расчета дисперсии
def d(arr,mu):
    n = len(arr)
    dlst = [(x-mu) ** 2 for x in arr]
    return sum(dlst)/n

# Функция для расчета квартилей
def quarts(arr):
    sort_arr = quick_sort(arr)
    n = len(sort_arr)
    q1 = median(sort_arr[:n//2])
    if n % 2 == 0:
        q3 = median(sort_arr[n//2:])
    else:
        q3 = median(sort_arr[n//2 + 1:])
    return q1, q3

data = user_input()
n = len(data)
if n <= 1:
    print('Недостаточное количество переменных, введите большее количество')
else:
    sort_data = quick_sort(data)
    n = len(sort_data)
    minim = sort_data[0]
    maxim = sort_data[n - 1]
    q1, q3 = quarts(data)
    mean = mu(data)
    deviation = d(data, mean)
    med = median(sort_data)

    print(f'Минимум: {minim}')
    print(f'Максимум: {maxim}')
    print(f'Квартили: {q1}, {q3}')
    print(f'Медиана: {med}')
    print(f'Мат. ожидание: {mean}')
    print(f'Дисперсия: {deviation}')
