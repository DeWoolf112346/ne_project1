import random


b = ''
l_list = ['A', 'B', 'C', 'D', 'E']
s_list = ['1', '2', '3', '4', '5']
computer_ship = []
for i in range(4):
    l = random.choice(l_list)
    s = random.choice(s_list)
    b = l + s
    computer_ship.append(b)
print(computer_ship)
for i in range(10):
    if computer_ship == []:
        break
    ship = input('Ваш ход: ')
    if ship in computer_ship:
        computer_ship.remove(ship)
        print('Вы попали!')
    else:
        print('Промах')
if computer_ship == []:
    print('Победа!')
else:
    print('ПОРАЖЕНИЕ:C')
