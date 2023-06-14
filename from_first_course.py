'''Задача:
Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):

Sample Input:
5

Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

Решение:'''
a = int(input())
m = [[int(0) for x in range (a)] for y in range (a)]
x = int(0)
y = int(0)
n = int(0)
while n != a**2:
  while 0 <= x <= a-1:
    if m[y][x] != 0:
      break
    n += 1
    m[y][x] = n
    x += 1
  x -= 1
  y += 1
  while 0 <= y <= a-1:
    if m[y][x] != 0:
      break
    n += 1
    m[y][x] = n
    y += 1
  y -= 1
  x -= 1
  while 0 <= x <= a-1:
    if m[y][x] != 0:
      break
    n += 1
    m[y][x] = n
    x -= 1
  x += 1
  y -= 1
  while 0 <= y <= a-1:
    if m[y][x] != 0:
      break
    n += 1
    m[y][x] = n
    y -= 1
  y += 1
  x += 1

for i in range (a):
  for j in range (a):
    print(m[i][j], end=' ')
  print()
-----------------------------------------------------------------------------------------------------------------------
'''Задача:
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end

Sample Output 1:
3 21 22
10 6 19
20 16 -1

Sample Input 2:
1
end

Sample Output 2:
4

Решение:'''
matrix_in = []

while True:
  a = input()
  if a == 'end':
    break
  else:
    matrix_in.append([int(i) for i in a.split()])

row = len(matrix_in)
col = len(matrix_in[0])
matrix_out = [[0 for i in range (col)] for j in range (row)]

for i in range (row):
  for j in range (col):
    if i == row - 1 and j != col - 1:
      matrix_out[i][j] = matrix_in[i-1][j]  + matrix_in[0][j] + matrix_in[i][j-1] + matrix_in[i][j+1]
    elif i == row - 1 and j == col - 1:
      matrix_out[i][j] = matrix_in[i-1][j]  + matrix_in[0][j] + matrix_in[i][j-1] + matrix_in[i][0]
    elif i != row - 1 and j == col - 1:
      matrix_out[i][j] = matrix_in[i-1][j]  + matrix_in[i+1][j] + matrix_in[i][j-1] + matrix_in[i][0]
    elif i < row - 1 and j < col - 1:
      matrix_out[i][j] = matrix_in[i-1][j]  + matrix_in[i+1][j] + matrix_in[i][j-1] + matrix_in[i][j+1]
    else:
      break

for i in range (row):
  for j in range (col):
    print(matrix_out[i][j], end=' ')
  print()
-----------------------------------------------------------------------------------------------------------------------
'''Задача:
Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d].
Числа a, b, c и d являются натуральными и не превосходят 10, ≤a≤b, ≤c≤d.
Следуйте формату вывода из примера. Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.

Sample Input:
1
3
2
4

Sample Output:
	2	3	4
1	2	3	4
2	4	6	8
3	6	9	12

Решение:'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(c, d+1):
  print ('\t', i, end = '')
print()
for s in range(a, b+1):
  print(s, end = '')
  for i in range(c, d+1):
      print('\t', s*i, end = '')
  print()
