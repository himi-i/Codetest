import sys 
input = sys.stdin.readline

while True:
    line = input().strip()
    if not line:
        break

    s, t = line.split()
    i = 0

    for char in t:
        if i < len(s) and char == s[i]:
            i += 1
    
    if i == len(s):
        print("Yes")
    else:
        print("No")






