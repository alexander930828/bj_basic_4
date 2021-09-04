#1
from sys import stdin

while True:
    a, b = map(int, stdin.readline().split())
    if a == 0 and b == 0:
        break
    print(a+b)


#2
from sys import stdin

while True:
    try:
        a, b = map(int, stdin.readline().split())
        print(a+b)
    except:
        break


#3
from sys import stdin

n = num = int(stdin.readline())

count = 0

while True:
    ten = n // 10
    one = n % 10
    total = ten + one
    n = (((n % 10) * 10) + (total % 10))
    count += 1
    if n == num:
        break

print(count)