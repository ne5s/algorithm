from sys import stdin

N = int(stdin.readline())
front = rear = 0
queue = [0 for _ in range(N+1)]
MAX_SIZE = len(queue)

def isEmpty():
    global front, rear
    return front == rear

def isFull():
    global front, rear, MAX_SIZE
    return front == (rear + 1) % MAX_SIZE

def enqueue(item):
    global front, rear, MAX_SIZE
    if not isFull():
        rear = (rear + 1) % MAX_SIZE
        queue[rear] = item

def dequeue():
    global front, MAX_SIZE
    if not isEmpty():
        front = (front + 1) % MAX_SIZE
        return queue[front]

for i in range(1, N+1):
    enqueue(i)

# print(queue)
while not isEmpty():
    print(dequeue(), end=' ')
    a = dequeue()
    if a:
        enqueue(a)
