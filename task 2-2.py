# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

evens = 0
odds = 0
i = 0

user_number=int(input("Введите число: "))

number_len = len(str(user_number))
for i in range(number_len):
    digit=((user_number // (10 ** i)) % 10)
#оказывается 0 - это четное число.
#    if digit==0:
#       pass
    if digit % 2 == 0:
        evens += 1
    else:
        odds += 1
    i += 1
print(f'Количество четных цифр: {evens} количество нечетных: {odds}')