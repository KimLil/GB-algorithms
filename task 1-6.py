#Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
#Блок-схема https://drive.google.com/file/d/1882dumVhGy7YQLvULwaOXFJw5mw7dHuN/view?usp=sharing


user_input = int(input('Введите номер буквы латинского алфавита от 1 до 26: '))
letter_number = user_input+96

#96 - добавленное зн-е для перехода к ASCII значениям строчных букв алфавита, т.к. первая буква "а" имеет номер 97

print(chr(letter_number))


