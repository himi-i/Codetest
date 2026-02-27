import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = [int(input()) for _ in range(n)]

heapq.heapify(arr)
count = 0

for _ in range(n-1):
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)

    s = x + y
    count += s

    heapq.heappush(arr, s)

print(count)



    
