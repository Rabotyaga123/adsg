import random as ran
import numpy as np

end = 0
while end <= 1:
    result = []
    input_number = 3 # количество переменных (поменять на рандом)
    list_y = []


    def x_generation(number): # функция генерации x
        count_lines = 2**(number)
        max_value = bin(count_lines-1)[2:]
        check_max = [] # список для максимального числа


        max = [max_value]
        for q in max[0]: # перебор каждого значения нулевого элемента максимального двоичного числа для определения длины
            check_max.append(q)
        # print("Число: ", max_value, "Его длина ", len(check_max)) - проверка в консоли максимального числа и его длины
        for i in range(0, count_lines): # добавление двоичного числа в список
            number = bin(i)[2:]
            n = number
            check_in = [] # список для проверки на одинаковое кол-во символов
            for a in n: # перебор каждого значения n-ого элемента двоичного числа для определения длины 
                check_in.append(a)
            if  len(check_in) < len(check_max): # условие для добавления нулей перед числом
                result.append("{}".format(0)*(len(check_max)-len(check_in)) + "{}".format(n)) # добавление нулей перед числом количеством разницы длины максимального и n-ого элемента
            elif len(check_in) >= len(check_max):
                result.append(n)
        # print(result)


    def y_generation(number): # функция генерации y
        y_count = (ran.randint(0, 10))
        count_lines = 2**(number)
        list = [1, 2, 3]
        for i in range(0, count_lines):
            list_y.append("{}".format(ran.randint(0, 1)))

        print(list_y)


    def transformation(test_x, test_y):
        # & - и | - или ~ - не    
        # test_x = ["0110", "1110", "0101", "1111", "0011"]
        # test_y = ["1", "0", "1", "0", "1"]
        spisok = []

        b = 1
        n = 0
        # func = []
        q = 0
        file1 = open("{}F.txt".format(end), "w")
        file1.write("f = ")
        # print(len(test_x))
        while b <= len(test_x):  # СДНФ
            a = 1
            if test_y[q] == '1':
                c = 0
                spisok.append('(')
                for i in test_x[q]:
                    if i == '0':
                        spisok.append("~X{}".format(c))
                        c += 1
                    else:
                        spisok.append("X{}".format(c))
                        c += 1
                    if a < len(test_x[q]):
                        spisok.append("&".format(c))
                    elif a == len(test_x[q]):
                        spisok.append(")".format(c))
                    a += 1
                if b < len(test_x):
                    spisok.append("|")
            elif test_y[q] == "0": # СКНФ
                c = 0
                spisok.append('(')
                for i in test_x[q]:
                    if i == '0':
                        spisok.append("X{}".format(c))
                        c += 1
                    else:
                        spisok.append("~X{}".format(c))
                        c += 1
                    if a < len(test_x[q]):
                        spisok.append("|".format(c))
                    elif a == len(test_x[q]):
                        spisok.append(")".format(c))
                    a += 1
                if b < len(test_x):
                    spisok.append("&")
            # print(b)
            q += 1
            b += 1
            # print(len(test_x))
        # print(spisok)
        for element in spisok:
            # print(element)
            file1 = open("{}F.txt".format(end), "a")
            file1.write(element)
        file1 = open("{}F.txt".format(end), "a")
        file1.close
    x_generation(input_number)
    y_generation(input_number)
    tes1 = result
    tes2 = list_y
    transformation(tes1, tes2)
    end += 1 