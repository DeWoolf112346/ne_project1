# def <Имя функции (обычно глагол)> (аргументы функции):
#     <тело функции>

def say_hello(name):
    print('Привет,', name)

say_hello('DeWoolf')

def count_to_10(a=0):
    for i in range(a, 11):
        print(i, end=' ')
    print()

count_to_10(5)
count_to_10()

def count_to_1(a):
    a = a * 10
    for i in range(a):
        print(i/10, end=' ')
    print()

count_to_1(1)

def set_shedole(day):
    print('Распорядок дня на:', day)
    if day == 'ПН' or day == 'ВТ' or day == 'СР' or day == 'ЧТ' or day == 'ПТ':
        print('Подъём')
        print('Завтрак')
        print('Школа')
        print('Обед')
        print('Уроки')
        print('Комп')
        print('Ужин')
        print('Отбой')
    elif day == 'ВС' or day == 'СБ':
        print('Подъём')
        print('Завтрак')
        print('Релакс')
        print('Обед')
        print('Комп')
        print('Ужин')
        print('Отбой')
    else:
        print("Я такого дня не знаю:C")

set_shedole("ПН")

