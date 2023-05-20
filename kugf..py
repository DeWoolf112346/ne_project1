lamp_list = ['Красный', 'Синий', 'Жёлтый', 'Зелёный']
e = 0
d = int(input('Введите число больше 0 '))
if d <= 0:
    e = d
    print('Ведите число больше 0!')
while e != d:
    e = e + 1
    print(e, lamp_list[0])
    if e == d:
        break
    e = e + 1
    print(e, lamp_list[1])
    if e == d:
        break
    e = e + 1
    print(e, lamp_list[2])
    if e == d:
        break
    e = e + 1
    print(e, lamp_list[3])
    if e == d:
        break