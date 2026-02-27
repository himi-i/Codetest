import sys
input = sys.stdin.readline
import heapq

T = int(input())

for _ in range(T):

    k = int(input())
    size = list(map(int, input().split())) 
    count = 0

    heapq.heapify(size)
    for _ in range(k-1):
        x = heapq.heappop(size)
        y = heapq.heappop(size)
        num = x + y
        count += num
        heapq.heappush(size, num)
    
    print(count)



    
    




    
