import sys
stack = []

def push(number):
    stack.append(number)

def pop():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack[0])
        del(stack[0])

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print("1")
    else:
        print("0")

def front():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack[0])

def back():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack[-1])

n = int(input())
for i in range(n):
    enter = sys.stdin.readline().rstrip()
    if enter == 'pop':
        pop()
    elif enter == 'size':
        size()
    elif enter == 'empty':
        empty()
    elif enter == 'front':
        front()
    elif enter == 'back':
        back()
    else:
        enter = list(enter.split())
        push(int(enter[1]))