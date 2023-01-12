import sys

def push(x):
    return stack.append(x)


def pop():
    if stack:
        return stack.pop()
    else:
        return -1


def size():
    return len(stack)


def empty():
    if stack:
        return 0
    else:
        return 1


def top():
    if stack:
        return stack[-1]
    else:
        return -1


n = int(input())

stack = []

for _ in range(n):
    inp = sys.stdin.readline().rstrip()
    try:
        com, num = inp.split()
        num = int(num)
    except ValueError:
        com = inp

    # print(f"========={com} & {num}========")

    if com == "push":
        push(num)
    elif com == "pop":
        print(pop())
    elif com == "size":
        print(size())
    elif com == "empty":
        print(empty())
    else:
        print(top())