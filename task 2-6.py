#6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.

import random

secret_number = random.randint(0, 100)
count = 0
print(secret_number)

while count<10:
    print(f'\nНомер попытки {count+1}/10')
    user_guess=int(input("Введите догадку: "))
    if user_guess == secret_number:
        exit("Вы угадали загаданное число!")
    elif user_guess < secret_number:
        print("Загаданное число больше вашей догадки!")
    elif user_guess > secret_number:
        print("Загаданное число меньше вашей догадки!")
    count+=1
print(f'\nВы не угадали! Загаданное число было {secret_number}')