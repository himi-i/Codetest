import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]
state = False

for shift in range(26):
    decoded = ""

    for c in s:
        new_c = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        decoded += new_c

    for w in words:
        if w in decoded:
            state = True
            break
    
    if state:
        print(decoded)
        break



        






