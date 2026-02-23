import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
answer = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y, depth, total):
    global answer

    if depth == 4:
        answer = max(answer, total)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            DFS(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False

def check(x, y):
    global answer
    center = board[x][y]
    wings = []

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            wings.append(board[nx][ny])

    if len(wings) >= 3:
        wings.sort(reverse=True)
        answer = max(answer, center + wings[0] + wings[1] + wings[2])           


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i, j, 1, board[i][j])
        visited[i][j] = False

        check(i, j)

print(answer)