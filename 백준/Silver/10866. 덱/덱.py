import sys
stack = []

def push_front(number):
    stack.insert(0,number)

def push_back(number):
    stack.append(number)

def pop_front():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack[0])
        del(stack[0])

def pop_back():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack[-1])
        del(stack[-1])

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
    if enter == 'pop_front':
        pop_front()
    elif enter == 'pop_back':
        pop_back()
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
        if enter[0] == 'push_front':
            push_front(int(enter[1]))
        elif enter[0] == 'push_back':
            push_back(int(enter[1]))