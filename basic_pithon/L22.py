# Метод join
"""s1 = "PYTHON"
print(s1)
print(s1.lower())
s2 = 'omg'
s2.upper()
print(s2)
print(s2.upper())"""
list_1 = ['a', 'b', 'c', 'd']
list_1_j = '_'.join(list_1)
print(list_1_j)

sentence = ['Привет', ',', 'как', 'дела', '?']
sentence_h = ' '.join(sentence)
print(sentence_h)
'split'
s1_l = 'Привет , как дела ?'
print(s1_l.split())

with open('teast_game.txt', 'w') as file:
    file.write('Доброго!')

my_sring_2 = 'Привет! Какие новости? Хлеб, колбаса, масло'
list_2 = my_sring_2.split('?')
print(list_2)