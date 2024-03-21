import sys
sys.setrecursionlimit(10 ** 9)

def recursion(i):
    print(f"recusion {i}")
    recursion(i + 1)

recursion(1)