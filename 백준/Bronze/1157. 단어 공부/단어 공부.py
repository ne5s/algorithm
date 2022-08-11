from sys import stdin

a = stdin.readline().rstrip()
a = a.upper()
li = [0]*26
for i in a:
    li[(ord(i)-65)] += 1
m = max(li)
max_index = [i for i,v in enumerate(li) if v == m]
if len(max_index) >= 2:
    print("?")
else:
    print(chr(li.index(m)+65))