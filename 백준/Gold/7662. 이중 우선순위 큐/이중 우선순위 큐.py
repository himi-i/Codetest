import sys 
input = sys.stdin.readline
import heapq

T = int(input())

for _ in range(T):
    k = int(input())

    min_q = []
    max_q = []
    visited = [False] * (k)

    for i in range(k):
        x, num = input().split()
        num = int(num)

        if x == "I":
            heapq.heappush(min_q, (num, i))
            heapq.heappush(max_q, (-num, i))

        elif x == "D" and num == 1:
            while max_q and visited[max_q[0][1]]:
                heapq.heappop(max_q)
            if max_q:
                
                visited[max_q[0][1]] = True
                heapq.heappop(max_q)

        else:
            while min_q and visited[min_q[0][1]]:
                heapq.heappop(min_q)
            if min_q:
                
                visited[min_q[0][1]] = True
                heapq.heappop(min_q)

    while min_q and visited[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and visited[max_q[0][1]]:
        heapq.heappop(max_q)

    if not min_q:
        print("EMPTY")
    else: 
        print(-max_q[0][0], min_q[0][0])



        






