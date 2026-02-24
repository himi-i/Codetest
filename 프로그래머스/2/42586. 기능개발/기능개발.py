import math
def solution(progresses, speeds):
    
    days = []
    answer = []
    
    for i in range(len(speeds)):
        x = 100 - progresses[i]
        days.append(math.ceil(x / speeds[i]))
        
    cnt = days[0]
    count = 1
        
    for j in range(1, len(days)):
        if days[j] <= cnt:
            count += 1            
        else:
            answer.append(count)
            cnt = days[j]
            count = 1
            
    answer.append(count)
            
    return answer