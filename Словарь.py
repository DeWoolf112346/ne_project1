'''''
dict_2 = dict_1.copy()
dict_2.update(person_dict)
print(dict_2)

presents_dict = {"Новый год": 1.1, "Рождество": 7.1}

dict_1.clear() # очищает словарь
dict_1.copy() # возвращает копию словоря
dict_1.get() # возвращает значение ключа, если нет, возвращает None
dict_1.items() # возвращает пары (ключ, значение)
dict_1.pop() # удаляет ключ и возвращает пару
dict_1.popitem() # удаляет и возвращает пару
dict_1.setdefault() # возвращает значение ключа
dict_1.update(other) # обновляет словарь значением из other 
dict_1.values() # возвращает значения в словаре
"""'''
import gc
aboba = 0
dict_1 = {"a": 100, "b": 200}
person_dict = {"Федя": 15, "Костя": 10, "Светлана": 13}
print(dict_1)
# dict_1.clear()
# print(dict_1)
# a = dict_1.copy()
# print(a)
# b = dict_1.get("a")
# print(b)
# c = dict_1.items()
# print(c)
dict_1.pop(aboba)
print(dict_1)
# dict_1.popitem()
# print(dict_1)
# e = dict_1.setdefault("c")
# print(dict_1)
# dict_1.update(list_1)
# print(dict_10)
# a, b = dict_1.values()
# print(a, b)

test_dict = {}
for i in range(1, 11):
    test_dict.update({f"{1}": i})
    print(test_dict)
# F - Строки
# a = 555
# print(f"Какая-то переменная {a}")

dict_3 = {"data1": 21, "data2": 32, "data3": -3, "data4": 5}
result = 1
for key in dict_3:
    result = result * dict_3[key]
print(result)

keys = ["red", "blue", "white"]
values = ["255,0,0", "0,0,255", "255,255,255"]
color_dict = dict(zip(keys, values))
print(color_dict)

for r, v in zip(keys, values):
    print(r, v)