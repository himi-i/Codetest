def solution(array, commands):
    
    answer = []
    for i, j, k in commands:
        arr = []
        for idx in range(i-1, j):
            arr.append(array[idx])
            
        sorted_arr = sorted(arr)
            
        answer.append(sorted_arr[k-1])
   
    return answer 