MINUSNUMBER = 2 #подстроки, которые не учитываем - строка целиком и пустая подстрока

def func(word):
    word_len = len(word)
    sub_set = set()
    sub_number = 0
    z = 0
    while z<word_len:
        for i in range(word_len):
            sub_set.add(word[z:word_len - i])
        z+=1
    print(sub_set)
    sub_number = len(sub_set)-MINUSNUMBER
    print(f'Найдено подстрок в введеном слове: {sub_number}')


word = str(input('введите слово:'))
func(word)