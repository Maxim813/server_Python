line_1 = 'attribute'
line_2 = 'класс'
line_3 = 'функция'
line_4 = 'type'

LIST = [line_1, line_2, line_3, line_4]

for el in LIST:
    try:
        print(bytes(el, 'ascii'))
    except UnicodeEncodeError:
        print(f'Слово "{el}" невозможно записать в виде байтовой строки')
