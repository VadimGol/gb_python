# Первое задание
number = 10
prompt = 'Hello!'
print(number)
print(prompt)

number = int(input("Enter the number "))
prompt = input('Enter the string ')
print(number)
print(prompt)

# Второе задание
time = int(input('Enter the seconds '))
hours = int(time / 3600)
minutes = int((time - hours * 3600) / 60)
seconds = int(time - hours * 3600 - minutes * 60)
print(f'{hours}:{minutes}:{seconds}')

# Третье задание
n = input('Enter the number: ')
nnn = int(f'{n}{n}{n}')
nn = int(f'{n}{n}')
n = int(n)
summary = nnn + nn + n
print(summary)

# Четвертое задание
maximum = 0
counter = 0
number = int(input('Enter the number: '))
while number > 0:
    temp = int(number % 10)
    if temp > maximum:
        maximum = temp
    number = int(number / 10)
print(maximum)

# Пятое и шестое задание
income = int(input('Enter th income of your company: '))
cost = int(input('Enter the cost of your company: '))
profit = income - cost
if income > cost:
    print('Прибыль')
    profitability = profit / income
    print(f'Рентабельность выручки - {profitability}')
    number_of_employers = int(input('Введите кол-во сотрудников'))
    print(f'Прибыль на одного сотрудника = {profit / number_of_employers}')
else:
    if cost > income:
        print('Убыток')
    else:
        if cost == income:
            print('Вы работаете в ноль')

# Седьмое задание
counter_days = 0
a = int(input('Первый день (км): '))
b = int(input('Нужно км: '))
while a < b:
    counter_days += 1
    a *= 1.1
print(f'Нужно {counter_days} дней')
#Hello
