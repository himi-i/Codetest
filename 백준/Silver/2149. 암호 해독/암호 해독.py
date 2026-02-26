import sys
input = sys.stdin.readline

key = input().strip()
cipher = input().strip()

k = len(key)
n = len(cipher) // k

arr = [[""] * k for _ in range(n)]


order = sorted([(key[i], i) for i in range(k)])

idx = 0

for x, col in order:
    for row in range(n):
        arr[row][col] = cipher[idx]
        idx += 1

for row in arr:
    print("".join(row), end="")


        






