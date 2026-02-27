import sys
input = sys.stdin.readline
n = int(input())

arr = [input() for _ in range(n)]

def quad(x, y, size):
    first = arr[x][y]
    same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != first:
                same = False
                break
        if not same:
            break

    if same:
        print(first, end="")
        return

    half = size // 2
    print("(", end="")
    quad(x, y, half)                 
    quad(x, y + half, half)          
    quad(x + half, y, half)          
    quad(x + half, y + half, half)   
    print(")", end="")

quad(0, 0, n)


    
    




    
