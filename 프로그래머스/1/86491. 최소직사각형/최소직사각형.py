# 접근
# 배열을 탐색하며 큰 값을 width에, 작은 값을 height에 저장한다.
# width와 height에 저장된 것보다 더 큰 값을 만날 때만 갱신한다.
# width * height를 return 한다.

def solution(sizes):
    
    width = 0
    height = 0
    
    for size in sizes:
        w, h = size
        
        if w < h:
            w, h = h, w
        
        if width < w:
            width = w
        
        if height < h:
            height = h
    
    return width * height