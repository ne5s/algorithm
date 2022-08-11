from sys import stdin

a = stdin.readline().rstrip()
sum = 0
for i in a:
    if "A"<= i and "C" >= i:
        sum += 3
    elif "D" <=i and "F" >= i:
        sum += 4
    elif "G" <= i and "I" >= i:
        sum += 5
    elif "J" <= i and "L" >= i:
        sum += 6
    elif "M" <= i and "O" >= i:
        sum += 7
    elif "P" <= i and "S" >= i:
        sum += 8
    elif "T" <= i and "V" >= i:
        sum += 9
    else:
        sum += 10
print(sum)
