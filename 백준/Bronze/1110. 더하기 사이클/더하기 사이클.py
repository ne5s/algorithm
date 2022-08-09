from sys import stdin

a = int(stdin.readline())
time = 0
next = a
while True:
    first , second = divmod(next, 10)
    new = first + second
    newOne = (second*10) + (new % 10)
    next = newOne
    time += 1
    if(a == newOne):
        print(time)
        break
