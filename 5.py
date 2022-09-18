import json
from random import randint
from functools import reduce


def write_in_file(path):
    with open(path, 'a', encoding='utf-8') as f:
        while True:
            text = input()
            f.writelines([text + '\n'])
            if text == '':
                break


def count_string(path):
    with open(path, 'r', encoding='utf-8') as f:
        str_list = f.readlines()
        print(f'Кол-во строк: {len(str_list)}')
        f.seek(0)
        for i in range(len(str_list)):
            words = len(str_list[i].split(' '))
            print(f'В {i + 1} строке {words} слов(а)')


def salaries(path):
    with open(path, 'r', encoding='utf-8') as f:
        str_list = f.readlines()
        counter = 0
        sum_salary = 0
        for i in range(len(str_list)):
            counter += 1
            sum_salary += int(str_list[i].split(' ')[1])
            if int(str_list[i].split(' ')[1]) < 20000:
                print(str_list[i].split(' ')[0])
        print(f'Средний доход: {sum_salary / counter}')


# 4
dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}


def translate(path_trans, path, dictionary):
    with open(path_trans, 'w', encoding='utf-8') as f_trans:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                f_trans.writelines([line.replace(line.split()[0], dictionary[line.split()[0]])])


# translate('4_trans.txt', '4.txt', dic)


# 5
def fill(path):
    with open(path, 'w', encoding='utf-8') as f:
        while True:
            number = input()
            if number == '' or not number.isdigit():
                break
            f.write(number + ' ')


def fill_rand(path, count):
    with open(path, 'w', encoding='utf-8') as f:
        for i in range(count):
            f.write(randint(1, 100) + ' ')


def summary(a, b):
    return a + b


def summary_file(path):
    fill(path)
    with open(path, 'r', encoding='utf-8') as f:
        number_list = f.readlines()[0].strip(' ').split(' ')
        res = reduce(summary, list(map(int, number_list)))
        print(res)


# summary_file('5.txt')
# fill('5.txt')
# arr = ['1', '2', '3', '4', '5', '6']
# print(list(map(int, arr)))

# 6

def lessons(path):
    lessons_hours = {}
    with open(path, 'r', encoding='utf-8') as f:
        st = ''
        res = 0
        st_list = f.readlines()
        for i in range(len(st_list)):
            for j in st_list[i]:
                if j.isdigit():
                    st += j
                if not j.isdigit():
                    try:
                        res += int(st)
                        st = ''
                    except ValueError:
                        continue
            key = st_list[i].split(' ')[0].strip(':')
            lessons_hours[key] = res
            res = 0
        print(lessons_hours)


# lessons('lessons.txt')
# 7

def profit_count(path, path_json):
    res_list = []
    profit_dict = {}
    av_profit = {}
    sum_profit = 0
    with open(path, 'r', encoding='utf-8') as f:
        st_list = f.readlines()
        for i in range(len(st_list)):
            profit = int(st_list[i].split(' ')[2]) - int(st_list[i].split(' ')[3])
            profit_dict[st_list[i].split(' ')[0]] = profit
            if profit > 0:
                sum_profit += profit
    av_profit['average_profit'] = sum_profit / i
    res_list.append(profit_dict)
    res_list.append(av_profit)
    with open(path_json, 'w', encoding='utf-8') as f_json:
        json.dump(res_list, f_json)


profit_count('7.txt', '7.json')
