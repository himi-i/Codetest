import sys
input = sys.stdin.readline

N = int(input())

arr = input().strip()
count = 0
for i, ch in enumerate(arr):
    x = ord(ch) - 96
    count += x * (31 ** i)

print(count)