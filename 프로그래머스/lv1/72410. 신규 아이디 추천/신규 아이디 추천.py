import re

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\{\}\[\]\<\>`\'…》]','', new_id)
    for i in reversed(range(2, len(new_id)+1)):
        if '.' * i in new_id:
            new_id = new_id.replace('.'*i, '.')

    if new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    while len(new_id) <= 2:
        new_id += new_id[-1]
    answer = new_id
    return answer