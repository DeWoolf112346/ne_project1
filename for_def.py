def first_count(i, l):
    u = 0
    if i > l:
        while i != l:
            u = u + i
            i = i - 1
        u = u + l
        print(u)

def second_count(i, l):
    u = 0
    if i < l:
        while l != i:
            u = u + l
            l = l - 1
        u = u + i
        print(u)