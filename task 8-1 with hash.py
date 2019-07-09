MINUSNUMBER = 2  # подстроки, которые не учитываем - строка целиком и пустая подстрока


def func(word):
    sub_set = set()
    sub_number = 0
    sub_hash = 0
    word_len = len(word)
    z = 0
    while z < word_len:
        for i in range(word_len):
            sub_hash = hash(word[z:word_len - i])
            sub_set.add(sub_hash)
        z += 1

    sub_number = len(sub_set) - MINUSNUMBER
    print(f'Найдено подстрок в введеном слове: {sub_number}')

word = str(input('введите слово:'))
func(word)