def solution(arr):
    
    if len(arr) == 1:
        return [-1]

    num = sorted(arr, reverse=True).pop()
    arr.remove(num)
    
    return arr