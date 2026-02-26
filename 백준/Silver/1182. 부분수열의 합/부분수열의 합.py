import sys 
input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

count = 0

def dfs(depth, total):
    global count

    if depth == n:
        if total == s:
            count += 1
        return
    
    dfs(depth + 1, total + arr[depth])

    dfs(depth + 1, total)

dfs(0, 0)

if s == 0:
    count -= 1

print(count)

