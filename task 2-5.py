#. Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


#def print_in_lines(what, symbols_per_line):
#    z=0
#    print(what, end="")
#    z+=1
#    while z==symbols_per_line:
#        print("\n")

row_item = 0

for i in range (32, 127):
    print(f'{i}-{chr(i)} ',end = "")
    row_item +=1
    while row_item==10:
        print("\n")
        row_item=0
    pass