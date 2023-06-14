'''Задача:
Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y, которая будет возвращать True, если остаток от деления y на x равен mod, и False иначе.

Пример использования:
mod_3 = mod_checker(3)
print(mod_3(3)) # True
print(mod_3(4)) # False
mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True

Решение:'''
def mod_checker(x, mod=0):
    return lambda y : y % x == mod
-----------------------------------------------------------------------------------------------------------------------
'''Задача:
Вам дана в архиве (https://stepik.org/media/attachments/lesson/24465/main.zip) файловая структура, состоящая из директорий и файлов.
Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py". 
Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
Решение:'''
import os
import os.path

way = []
for curent_dir, dirs, files in os.walk('main'):
    way += curent_dir, files

way_dict = {}
for i in range(way.count([])):
    way.remove([])

a = "    "
for i in range(len(way)):
    try:
        if a[0:4] == 'main' and way[i][0:4] == 'main':
            way.pop(i-1)
        a = str(way[i])
    except IndexError:
        break

preanswer = []
for i in range(len(way)):
    v = str(way[i])
    if '.py' in v:
        preanswer.append(way[i-1])
preanswer.sort()

with open ('searching_py_answer', 'w') as w:
    for i in preanswer:
        w.write(i+'\n')
-----------------------------------------------------------------------------------------------------------------------
'''Задача:
Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.

Пример использования:
print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

Решение:'''
def primes():
    count = 2
    yield count
    while True:
        count += 1
        variables = [i for i in range(1, count+1)]
        variables = map(lambda x: count % x, variables)
        if list(variables).count(0) == 2:
            yield count
-----------------------------------------------------------------------------------------------------------------------
'''Задача:
В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию, что и стандартный класс filter, но будет использовать не одну функцию, а несколько.
Решение о допуске элемента будет приниматься на основании того, сколько функций допускают этот элемент, и сколько не допускают. Обозначим эти количества за pos и neg.
Введем понятие решающей функции – это функция, которая принимает два аргумента – количества pos и neg, и возвращает True, если элемент допущен, и False иначе.

Класс должен обладать следующей структурой:
class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        # возвращает итератор по результирующей последовательности

Пример использования:
def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5))) 
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 
# [0, 30]

Решение:'''
class multifilter:

    def judge_half(self, pos=0, neg=0):
        if pos >= neg:
            return True
        else:
            return False

    def judge_any(self, pos=0, neg=0):
        if pos >= 1:
            return True
        else:
            return False

    def judge_all(self, pos=0, neg=0):
        if neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        self.iterable = iterable
        # funcs - допускающие функции
        self.funcs = list(funcs)
        # judge - решающая функция
        self.judge = judge

        answer = []
        for i in self.iterable:
            pos1 = 0
            neg1 = 0
            for k in self.funcs:
                if k(i):
                    pos1 += 1
                else:
                    neg1 += 1
            if self.judge(self, pos1, neg1):
                answer.append(i)
        self.answer = answer

    def __iter__(self):
        return iter(self.answer)
-----------------------------------------------------------------------------------------------------------------------
'''Задача:
Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:
class Error1(Error2, Error3 ... ErrorK):
    pass

Антон написал код, который выглядит следующим образом.
try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...
Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого положения и напишите программу, которая будет определять обработку каких исключений можно удалить из кода.

Важное примечание:
В отличие от предыдущей задачи, типы исключений не созданы.
Создавать классы исключений также не требуется
Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее где-то поймали их предка.

Формат входных данных
В первой строке входных данных содержится целое число n - число классов исключений.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.

Формат выходных данных
Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.

Sample Input:
4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError

Sample Output:
FileNotFoundError

Решение:'''
def got(classes, cached, value):
    global result
    result = False

    for k, v in classes.items():
        for i in v:
            if result:
                break
            else:
                if i == value:
                    if k in cached:
                        result = True
                        break
                    elif k not in cached:
                      got(classes, cached, k)
    return result



a = int(input())
classes = {}
names = []
cached = []
result = False
for i in range(a):
    names = input().strip(" ").split()
    if len(names) == 1:
        if names[0] not in classes.keys():
            classes[names[0]] = []
    elif len(names) > 1:
        for i in range(2, len(names)):
            if names[i] not in classes.keys():
                classes[names[i]] = [names[0]]
            elif names[i] in classes.keys():
                classes[names[i]] += [names[0]]

a = int(input())

for i in range(a):
    ask = input()
    cached.append(ask)
    answer = got(classes, cached, ask)
    if answer:
        print(ask)
