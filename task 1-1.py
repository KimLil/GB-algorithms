#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
#Блок-схема https://drive.google.com/file/d/1882dumVhGy7YQLvULwaOXFJw5mw7dHuN/view?usp=sharing

number = int(input("Введите трехзначное число: "))
#a, b, c - значения в разрядах числа number (соотв. сотни, десятки и единицы)

a = (number//100)%10
b = (number//10)%10
c = (number//1)%10

sum = a + b + c
mult = a * b * c

print("Цифры, из которых составлено ваше число: ", a, b, c)
print("Cумма цифр вашего числа: ", sum)
print("Произведение цифр вашего числа: ", mult)