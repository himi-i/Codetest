from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
    return True       
            

def solution(numbers):
    
    arr = set()
    for i in range(1, len(numbers) + 1):
        for x in permutations(numbers, i):
            arr.add(int("".join(x)))
    
    count = 0
    for data in arr:
        if is_prime(data):
            count += 1
        
    return count