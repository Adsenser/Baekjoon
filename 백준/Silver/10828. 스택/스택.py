import sys
stack = []

def push(number):
    stack.append(number)

def pop():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack[-1])
        stack.pop()

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print("1")
    else:
        print("0")

def top():
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
    elif enter == 'top':
        top()
    else:
        enter = list(enter.split())
        push(int(enter[1]))