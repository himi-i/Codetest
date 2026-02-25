def solution(s):
    answer = True
    stack = []
    
    for x in s:
        if x == "(":
            stack.append(x)
        else:
            if not stack:
                return False
            stack.pop()
    
    if stack:
        answer = False
            
    return answer