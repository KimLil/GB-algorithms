#Определить, является ли год, который ввел пользователь, високосным или не високосным.

#Блок-схема https://drive.google.com/file/d/1882dumVhGy7YQLvULwaOXFJw5mw7dHuN/view?usp=sharing

year = int(input("Введите год в формате YYYY: "))

if year%400==0:
    print("Этот год - високосный")
else:
    if year%100==0:
        print("Этот год - НЕ високосный")
    else:
        if year % 4 == 0:
            print("Этот год - високосный")
        else:
            print("Этот год - НЕ високосный")
