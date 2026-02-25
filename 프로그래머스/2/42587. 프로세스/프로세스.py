from collections import deque

def solution(priorities, location):
    
    q = deque()
    
    for i, p in enumerate(priorities):
        q.append((p, i))
        
    count = 0
    
    while q:
        p, i = q.popleft()
        
        is_high = False
        
        for nx_p, nx_i in q:
            if p < nx_p:
                q.append((p, i))
                is_high = True
                break
                
        if not is_high:
            count += 1
            if i == location:
                return count
            
                
        
    
    
        
    
    

    
    
    answer = 0
    return answer