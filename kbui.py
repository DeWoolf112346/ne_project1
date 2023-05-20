import time

while True:
    k = 0
    bk = 0
    timer = int(input('Введите кол-во секунд: '))
    for i in range(timer):
        time.sleep(1)
        k += 1
        print('Прошло секунд:', k)
        if k % 60 == 0:
            bk += 1
            print('Прошло минут:', bk)
    break
print('Время окончено!')