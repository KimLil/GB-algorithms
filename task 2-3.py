#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

def reverse_digits_in_number(m):
    number_len = len(str(m))
    for i in range(number_len):
        print((m // (10 ** i)) % 10, end="")
        i += 1
    print('\nyour number is reversed')


user_number=int(input("Введите число: "))
reverse_digits_in_number(user_number)