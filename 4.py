from functools import reduce
from itertools import count, cycle

# 2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[i] for i in range(len(my_list)) if my_list[i] > my_list[i - 1] and i != 0]
print(new_list)

# 3
arr = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(arr)

# 4
arr1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_arr1 = [i for i in arr1 if arr1.count(i) == 1]
print(new_arr1)

# 5
arr2 = [i for i in range(100, 1001) if i % 2 == 0]


def multiply(a, b):
    return a * b


print(reduce(multiply, arr2))


# 6
def numbers(a):
    return count(a, 1)


# for el in numbers(3):
#    print(el)
#    if el > 100:
#        break


def cycles(cycle_list):
    return cycle(cycle_list)


cycled_list = [8, 800, 555, 35, 35]
counter = 0
for el in cycles(cycled_list):
    print(el)
    counter += 1
    if counter > 20:
        break


# 7
def factorial(n):
    for i in range(n):
        res = 1
        if i == 0:
            res = 1
            yield res
            continue
        else:
            for j in range(1, i + 1):
                res *= j
        yield res


for i in factorial(6):
    print(i)
