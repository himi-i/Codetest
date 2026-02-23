import sys
input = sys.stdin.readline

N = int(input())

board = [list(input().strip()) for _ in range(N)]


def check():
    max_cnt = 1

    for i in range(N):
        count = 1
        for j in range(N - 1):
            if board[i][j] == board[i][j+1]:
                count += 1
            else:
                count = 1
            max_cnt = max(max_cnt, count)

    for j in range(N):
        count = 1
        for i in range(N - 1):
            if board[i][j] == board[i+1][j]:
                count += 1
            else:
                count = 1
            max_cnt = max(max_cnt, count)
    
    return max_cnt


answer = 0
for i in range(N):
    for j in range(N):
        if j < N - 1 and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer, check())
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if i < N - 1 and board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer, check())
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)


            



