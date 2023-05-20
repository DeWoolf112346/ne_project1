import random
import time

game_naame = 'Название игры'
WIDTH = 100

len_left = 40
gap_len = 20

running = True

while running:
    len_right = WIDTH - gap_len - len_left
    print('#'*len_left, ' '*gap_len, '#'*len_right)
    r = random.randint(0, 3)
    n = random.randint(15, 20)
    gap_len = n
    if len_left > 1 and r == 1:
        len_left -= 1
    elif len_left + gap_len < WIDTH - 1 and r == 2:
        len_left += 1
    time.sleep(0.2)