# 1
array = [1, 1.5, 'word', (5, 's'), [1, 2, 3]]
for i in range(len(array)):
    print(type(array[i]))

# 2
size = int(input('Введите размер списка: '))
a = []
for i in range(size):
    a.append(input(f'Введите элемент {i + 1}: '))
for i in range(int(size / 2)):
    (a[i * 2], a[(i * 2) + 1]) = (a[(i * 2) + 1], a[i * 2])
print(a)

# 3
date = {
    'winter': [1, 2, 12],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11],
}
month = int(input('Введите номер месяца от 1 до 12: '))
for key in date:
    if month in date[key]:
        print(key)
# 4
sentence = input('Введите строку: ')
words = sentence.split(' ', )
for i in range(len(words)):
    print(f'Слово {i + 1}:', end=' ')
    print(words[i][:10])
# 5
rating = [7, 5, 4, 2]
print(rating)
number = int(input('Введите рейтинг: '))
for i in range(len(rating)):
    if rating[i] < number:
        rating.insert(i, number)
        break
    else:
        rating.append(number)
        break
print(rating)

# 6
product_list = []

storage = int(input('Введите кол-во товаров'))
for i in range(storage):
    name = input('Введите наименование товара: ')
    cost = int(input('Введите цену товара: '))
    amount = int(input('Введите кол-во товара: '))
    measure = input('Введите измерение товара: ')
    product_dict = {
        'название': name,
        'цена': cost,
        'кол-во': amount,
        'ед': measure
    }
    product_list.append((i + 1, product_dict.items()))
print(product_list)
# Или можно без словаря, просто вручную присваивать значения переменным и изменять строку
# Судя по фигурным скобкам в условии, так и надо было
