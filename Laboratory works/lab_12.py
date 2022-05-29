from collections import Counter
from functools import reduce

# 1
print('#1')
dictionary_1 = {'a': 300, 'b': 400}
print('dictionary_1: ', dictionary_1)
dictionary_2 = {'c': 500, 'd': 600}
print('dictionary_2: ', dictionary_2)
dictionary_1.update(dictionary_2)
print('Ответ:', dictionary_1)
print()

# 2
print('#2')
d = {1: '1', 2: '8', 3: '27', 4: '64', 5: '125', 6: '216', 7: '343', 8: '512', 9: '729', 10: '1000'}
print('Ответ:', d)
print()

# 3
print('#3')
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
print('my_dict:', my_dict)
keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print('Ответ:', keys)
print()


# 4
print('#4')
def swap(d):
    d2 = {}
    for key, value in d:
        d2[value] = key
    return d2

d = {1: 'one', 2: 'two', 3: 'three'}
print('d:', d)
d = d.items()
d = swap(d)
print('Ответ:', d)
print()

# 5
print('#5')
n = int(input('Введите количество элементов:'))
a = list(map(int, input('Введите элементы : ').strip().split()))[:n]
print('Список ключей', a)
b = list(map(str, input('Введите элементы : ').strip().split()))[:n]
print('Список значений', b)
d = dict(zip(a, b))
print('Oтвет:', d)
print()

# 6
print('#6')
word = 'pythonist'
dict_1 = dict([(c, word.count(c)) for c in set(word)])
print('Ответ:', dict_1)
print()

# 7
print('#7')
word = input("Введите строку:")
dict_1 = dict([(c, word.count(c)) for c in set(word)])
print('Ответ:', dict_1)
print()

# 8
print('#8')
dict_1 = {0: "Москва", 1: ["Санкт-Петербург", "Новосибирск", "Екатеринбург"], 2: ["Казань", "Нижний Новгород"],
          3: ["Челябинск", "Самара"]}
val_list = list(dict_1.values())
# a
city = input('Введите город:')
for i in val_list:
    if i == city:
        print('Удалённость от столицы:', 0)
        print('Города на том же росстоянии:', dict_1[0])
    else:
        for k in i:
            if city == k:
                print('Удалённость от столицы:', val_list.index(i))
                print('Города на том же росстоянии:', dict_1[val_list.index(i)])


# б
def road(city_1, city_2):
    for i in val_list:
        if i == city_1 or i == city_2:
            if i == city_1:
                c1 = 0
            else:
                c2 = 0
        else:
            for k in i:
                if city_1 == k or city_2 == k:
                    if city_1 == k:
                        c1 = val_list.index(i)
                    else:
                        c2 = val_list.index(i)
    if c2 - c1 == 1 or c1 - c2 == 1:
        return "Можно"
    else:
        return "Нельзя"


city_1 = input('Введите город:')
city_2 = input('Введите город:')
a = road(city_1, city_2)
print(a)

# 9
print('#9')
country = []
cities = []
n = int(input('Введите количество стран/городов:'))
for i in range(n):
    country.append(input('Введите страну:'))
    cities.append(input('Введите город:'))
a = dict(zip(cities, country))
print(a)
n = int(input('Введите количество городов для поиска соответствия:'))
for i in range(0,n):
    city = input('Введите название города:')
    print('Ответ:', a[city])
print()

# 10
print('#10')
text = 'в строке записан текст подсчитать сколько раз текст встречалось ранее в тексте '
word = []
word = text.split()
print(word)
dict_1 = dict([(c, word.count(c)) for c in set(word)])
print('Ответ:', dict_1)
print()

# 11
print('#11')
a_dict = {1: 'one', 2: 'two'}
print(str(a_dict))
redict = {v: k for k, v in a_dict.items()}
print('Ответ:', redict)
print()

# 12
print('#12')
school = {'1a': 24, '2a': 11, '2б': 13, '3a': 21, '4a': 19, '4б': 20, '4в': 18}
print('Изначально:', school)
# a
school['1a'] = 25
print('а)', school)
# б
school['1б'] = 8
print('б)', school)
# с
del school['2б']
print('с)', school)
print('Всего учатся', sum(school.values()))
print()

# 13
print('#13')
dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
print('Первый словарь:', dict_1)
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
print('Второй словарь:', dict_2)
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
print('Третий словарь:', dict_3)
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}
print('Четвёртый словарь:', dict_4)
def max_dct(*dicts):
    return dict(reduce(lambda a, b: Counter(a) | Counter(b), dicts))
print('Новый словарь')
print(max_dct(dict_1, dict_2, dict_3, dict_4))
print()

# 14
print('#14')
#                      ФИО                         Адрес               Номер
firstGroup = {"Иванов Себастьян Сидорович": ["Кипарисова 5", "8(495)715-7964"],
              "Герасимова Ирина Борисовна": ["Ленина 101", "8(495)207-2055"],
              "Лукин Гюльбек Викторович": ["Мира 12", "8(495)069-7578"],
              "Герасимов Абдулла Данилович": ["Комсомольская 15", "8(495)095-7463"]}

secondGroup = {"Степанова Мира Геннадиевна": ["Крымская 2", "8(495)889-7543"],
               "Киселёв Шамиль Филатович": ["Московская 89", "8(495)510-5659"],
               "Мамонтов Адольф Гитлерович": ["Комышевича 159", "8(495)184-7527"],
               "Герасимов Мартын Максимович": ["Заречная 78", "8(495)234-6079"]}

scoreFirstGroup = {"Иванов Себастьян Сидорович": [[4, 5, 4, 4], [4, 5, 4, 4], [2, 4, 4, 3]],
                   "Герасимова Ирина Борисовна": [[5, 5, 5, 4], [4, 5, 4, 4], [2, 4, 4, 2]],
                   "Лукин Гюльбек Викторович": [[5, 3, 5, 5], [5, 5, 5, 4], [5, 5, 4, 5]],
                   "Герасимов Абдулла Данилович": [[2, 4, 4, 3], [4, 5, 4, 4], [4, 4, 4, 4]]}

scoreSecondGroup = {"Степанова Мира Геннадиевна": [[5, 4, 4, 2], [4, 5, 2, 4], [2, 2, 4, 5]],
                    "Киселёв Шамиль Филатович": [[2, 5, 5, 3], [5, 5, 5, 4], [3, 5, 3, 4]],
                    "Мамонтов Адольф Гитлерович": [[3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]],
                    "Герасимов Мартын Максимович": [[4, 4, 4, 4], [3, 5, 4, 4], [5, 4, 2, 4]]}


def show_table(table):
    line = "-" * 126

    print(line)
    print("|{:>30}|{:>35}|{:>15}|{:>15}|{:>15}|".format("ФИО", "Алгоритмизация и программирование", "Информатика",
                                                        "Физкультура", "Средняя оценка"))
    print(line)
    fullAvgScore = 0
    for student, score in table.items():
        avg = round(sum([sum(n) for n in score]) / 12, 1)
        fullAvgScore += avg
        print("|{:>30}|{:>35}|{:>15}|{:>15}|{:>15}|".format(student, ' '.join([str(n) for n in score[0]]),' '.join([str(n) for n in score[1]]),' '.join([str(n) for n in score[2]]), avg))
        print(line)
    fullAvgScore = round(fullAvgScore / len(table), 1)
    print(f"Общая средняя оценка = {fullAvgScore}")


print("Первая группа")
show_table(scoreFirstGroup)
print("\nВторая группа")
show_table(scoreSecondGroup)
print()

# 15
print('#15')
a = set('12345')
b = set('126789')
print('Множество a:', a)
print('Множесвто b:', b)
c = a | b
print('Объединение множеств:', c)
c = a & b
print('Пересечение множеств:', c)
c = a - b
print('Разность множеств:', c)
c = a in b
print('Принадлежность a к b:', c)
print()

