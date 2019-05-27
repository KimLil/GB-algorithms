#Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

#Блок-схема https://drive.google.com/file/d/1882dumVhGy7YQLvULwaOXFJw5mw7dHuN/view?usp=sharing

a = int(input("Введите 1ое число: "))
b = int(input("Введите 2ое число: "))
c = int(input("Введите 3ое число: "))

if a<b:
    if b<c:
        print("Среднее число: ", b)
    else:
        if a<c:
            print("Среднее число: ", c)
        else:
            print("Среднее число: ", a)
else:
    if a<c:
        print("Среднее число: ", a)
    else:
        if b<c:
            print("Среднее число: ", c)
        else:
            print("Среднее число: ", b)

