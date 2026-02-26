import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()

two_sum = set()

for i in range(n):
    for j in range(n):
        two_sum.add(arr[i] + arr[j])

for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        if arr[i] - arr[j] in two_sum:
            print(arr[i])
            exit()