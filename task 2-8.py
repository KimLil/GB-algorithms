#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


user_number = int(input("Введите число: "))
user_digit = int(input("Какую цифру нужно искать в числе?"))
user_digits_sum = 0

number_len = len(str(user_number))
for i in range(number_len):
    digit=((user_number//(10**i))%10)
    if digit == user_digit:
        user_digits_sum +=1
    else:
        pass

print(f'В числе {user_number} встречается {user_digits_sum} цифр {user_digit}')