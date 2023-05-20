palindrom = ['ш', 'а', 'л', 'а', 'ш']
ch = 0
if palindrom[0] == palindrom[4]:
    ch += 1
if palindrom[1] == palindrom[3]:
    ch += 1
if palindrom[2] == palindrom[2]:
    ch += 1
if ch == 3:
    print('палендром')
else:
    print('не палендром')