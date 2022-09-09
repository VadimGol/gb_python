# 1
def div(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        print('Деление на ноль невозможно')
    finally:
        return None


# print(div(int(input('Введите числитель: ')), int(input('Введите знаменатель: '))))


# 2
def person_info(name, surname, year, city, email, phone):
    print(f'Имя: {name}; Фамилия: {surname}; Год рождения: {year}; Город: {city}; Почта: {email}; Телефон: {phone}')


# person_info(name=input('Имя: '), surname=input('Фамилия: '), year=input('Год: '), city=input('Город: '),
#            email=input('Почта: '), phone=input('Телефон: '))


# 3
def my_func(a, b, c):
    arr = [a, b, c]
    arr.remove(min(arr))
    return arr[0] + arr[1]


# print(my_func(112, 254, 39))


# 4
def p(x, y):
    res = 1
    while y < 0:
        res = res * (1 / x)
        y = y + 1
    return res


# print(p(3, -1))


# 5
def summary():
    tmp_sum = 0
    while True:
        number = input('')
        try:
            for i in map(int, number.split(' ')):
                tmp_sum += i
        except ValueError:
            break

        print(tmp_sum)


# ИЛИ

def summary_2():
    tmp_sum = 0
    special_symbol = '/'
    while True:
        number = input('')
        if special_symbol in number.split(' '):
            for i in range(len(number.split(' '))):
                if number.split(' ')[i] == '/':
                    print(tmp_sum)
                    return 0
                else:
                    tmp_sum += int(number.split(' ')[i])
        else:
            for i in map(int, number.split(' ')):
                tmp_sum += i

        print(tmp_sum)


# 6
def int_func(word):
    return word.capitalize()


# 7
def sentence_func(words):
    for i in range(len(words.split(' '))):
        print(int_func(words.split(' ')[i]), end=' ')
