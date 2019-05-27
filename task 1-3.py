# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
#Блок-схема https://drive.google.com/file/d/1882dumVhGy7YQLvULwaOXFJw5mw7dHuN/view?usp=sharing

print("Введите координаты точек")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

print (x1, y1)
print (x2, y2)

if x1 != x2:
    k = (y1-y2)/(x1-x2)
    b = y1 - k*x1
    print("Уравнение исходной прямой: y =",k,"* x +", b )
else:
    print("Точки должны иметь различные значения Х")