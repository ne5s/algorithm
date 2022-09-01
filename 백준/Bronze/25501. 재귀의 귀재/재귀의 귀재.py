from sys import stdin

def recursion(s, l, r):
    global i
    i += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global i
    i = 0
    return recursion(s, 0, len(s)-1)

i = 0
n = int(stdin.readline())
for i in range(n):
    a = stdin.readline().rstrip()
    print(isPalindrome(a), i)