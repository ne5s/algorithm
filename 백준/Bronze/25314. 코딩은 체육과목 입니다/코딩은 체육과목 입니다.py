from sys import stdin

def p(N):
    str_list = []
    for i in range(int(N/4)):
        str_list.append('long')
    for i in range(len(str_list)):
        if i == 0:
            print(str_list[i], end='')
        else:
            print(' ' + str_list[i], end='')
    print(' int')

if __name__ == "__main__":
    N = int(stdin.readline())
    p(N)