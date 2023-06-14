'''Задача:
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:
<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.
Ценность цвета равна сумме ценностей всех кубиков этого цвета.
Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

Sample Input:
<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>

Sample Output:
4 3 1

Решение:'''
from xml.etree import ElementTree
import sys

def cubism (x, count=1):
    count += 1
    for child in x:
        res[child.attrib['color']] += count
        cubism(child, count)


tree = ElementTree.parse(sys.stdin)
root = tree.getroot()
res = {'blue': 0, 'red': 0, 'green': 0}
res[root.attrib['color']] += 1
cubism(root)
print(res['red'],res['green'],res['blue'])

-----------------------------------------------------------------------------------------------------------------------
'''Задача:
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. 
У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Эквивалент на Python:
class A:
    pass
class B(A, C):
    pass
class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.
Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
<имя класса> : <количество потомков>
Выводить классы следует в лексикографическом порядке.

Sample Input:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:
A : 3
B : 1
C : 2 

Решение:'''
import json
import sys


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return len(visited)


visited = []
queue = []
all_invert = {}

all = json.load(sys.stdin)
for i in all:
    if i['name'] not in all_invert:
        all_invert[i['name']] = []
    for i2 in i['parents']:
        if i2 not in all_invert:
            all_invert[i2] = []
            all_invert[i2].append(i['name'])
        else:
            all_invert[i2].append(i['name'])
sort = [i for i in all_invert]
sort.sort()
for i in sort:
    visited.clear()
    queue.clear()
    print(i,':',bfs(visited, all_invert, i))
-----------------------------------------------------------------------------------------------------------------------
'''Задача:
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.
Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.
Сайты следует выводить в алфавитном порядке.

Пример HTML файла:
<a href="http://stepik.org/courses">
<a href='https://stepik.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:
mail.ru
neerc.ifmo.ru
stepik.org
www.ya.ru
ya.ru

Решение:'''
import re
import requests

HW = requests.get(input())
pattern = '<a.*?href=[\"\']*(:?\w+:\/\/)?([\w|\-]+(\.[\w|\-]+)+)[\/\:\'\"]'
collection = re.findall(pattern, HW.text)
collection2 = []
for i in collection:
    if i[1] not in collection2:
        collection2.append(i[1])
    else:
        continue
collection2.sort()
for i in collection2:
    print(i)
-----------------------------------------------------------------------------------------------------------------------
'''Задача:
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.
Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input:
https://stepik.org/media/attachments/lesson/24472/sample0.html
https://stepik.org/media/attachments/lesson/24472/sample2.html

Sample Output:
Yes

Решение:'''
import re
import requests


count = 0
urlA = str(input())
urlB = str(input())
collection = requests.get(urlA)
pattern = r'<a.*href="(.*)">.*</a>'
for urlC in re.findall(pattern, collection.text):
    collection2 = requests.get(urlC)
    if urlB in re.findall(pattern, collection2.text):
        count += 1
    else:
        continue
if count > 0:
    print('Yes')
else:
    print('No')
-----------------------------------------------------------------------------------------------------------------------
'''Задача:
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.

Sample Input:
attraction
buzzzz

Sample Output:
atraction
buz

Решение:'''
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\w)\1+'
    find = re.sub(pattern, r'\1', line)
    print(find)
-----------------------------------------------------------------------------------------------------------------------
'''Задача:
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.

Sample Input:
this is a text
"this' !is. ?n1ce,

Sample Output:
htis si a etxt
"htis' !si. ?1nce,

Решение:'''
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\b\w{1})(\w{1})'
    find = re.sub(pattern, r'\2\1', line)
    print(find)
-----------------------------------------------------------------------------------------------------------------------
'''Задача:
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".

Sample Input:
There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA

Sample Output:
There’ll be no more "argh"
argh AaAaAaA

Решение:'''
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\ba+\b'
    change = r'argh'
    sub = re.sub(pattern, change, line, 1, re.IGNORECASE)
    print(sub)
-----------------------------------------------------------------------------------------------------------------------
'''Задача:
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
Выведите одно число – количество вхождений строки t в строку s.

Sample Input 1:
abababa
aba

Sample Output 1:
3

Решение:'''
a = str(input())
b = str(input())
index = 0
count = 0
while index != -1:
    index = a.find(b, index)
    if index == -1:
        break
    else:
        count += 1
    index += 1
print(count)
