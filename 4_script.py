from sys import argv

if len(argv) != 4:
    print('Wrong amount of the arguments')
else:
    salary = (int(argv[1]) * int(argv[2])) + int(argv[3])
    print(salary)
