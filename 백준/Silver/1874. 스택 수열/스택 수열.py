import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]
stack = []
num = 1
result = []

for x in arr:
    while num <= x:
        stack.append(num)
        result.append("+")
        num += 1

    if stack and stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit()

for r in result:
    print(r)