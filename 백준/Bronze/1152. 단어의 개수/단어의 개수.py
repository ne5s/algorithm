from sys import stdin

a = stdin.readline().strip()
if a =="":
  print(0)
else:
  print(a.count(" ")+1)