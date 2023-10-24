error = 'Перезапуск программы.'

# Функция для определения цифр в строке
def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

# Проверка соответствия указанному в условии ввода данных.
while True:
    array = input('Введите целые числа через пробел: ')
    if " " not in array:
        print("\nВ вводе отсутствуют пробелы (введите числа, согласно условиям ввода.)")
        continue
    elif not is_int(array):
        print('\nВ вводе содержаться не целые числа (введите числа, согласно условиям ввода.)\n')
        print(error)
        continue
    else:
        array = array.split()
        break

while True:
    element = input('Введите любое число: ')
    if " " in element:
        print('\nВ вводе любого числа содержаться пробелы (введите целое число.)\n')
        print(error)
        continue
    elif not is_int(element):
        print('\nВ вводе любого числа содержиться не целое число (введите целое число.)\n')
        print(error)
        continue
    else:
        element = int(element)
        break

# Конвертация строки в числа
list_array = [int(item) for item in array]

# Сортировка списока по возростанию
def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


# Сортировка по возростанию с помощью встроенной функции
list_array = merge_sort(list_array)

# Поиск позиции элемента
def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

# Устанавливаем номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
print(f'Упорядоченный список: {list_array}')
max = len(list_array) - 1
if element > list_array[max]:
    print(f'''Введенный элемент находится за списком
В списке нет большего элемента
Ближайший меньший элемент: {list_array[max]}, его индекс: {max}''')
elif element < list_array[0]:
    print(f'''В списке нет введенного элемента
В списке нет меньшего элемента
Ближайший больший элемент: {list_array[0]}, его индекс: {0}''')
else:

    index = binary_search(list_array, element, 0, len(list_array))

    if not binary_search(list_array, element, 0, len(list_array)):
        rI = min(list_array, key=lambda x: (abs(x - element), x))
        ind = list_array.index(rI)
        max_ind = ind + 1
        min_ind = ind - 1
        if rI < element:
            print(f'''В списке нет введенного элемента
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {list_array[max_ind]} его индекс: {max_ind}''')
        else:
            print(
                f'''Индекс введенного элемента: {binary_search(list_array, element, 0, len(list_array))}
В списке нет меньшего элемента
Ближайший больший элемент: {list_array[max_ind]} его индекс: {max_ind}''')
    else:
        if index == max:
            print(f'''Индекс введенного элемента: {index}
Ближайший меньший элемент: {list_array[max - 1]}, его индекс: {max - 1}
В списке нет большего элемента''')
        else:
            print(f'''Индекс введенного элемента: {index}
Ближайший меньший элемент: {list_array[index - 1]}, его индекс: {index - 1}
Ближайший больший элемент: {list_array[index + 1]}, его индекс: {index + 1}''')