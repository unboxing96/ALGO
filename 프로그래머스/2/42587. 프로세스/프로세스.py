# 이해
# priorities 배열을 우선순위에 따라 pop() 할 때, 
# location 위치에 있는 원소가 몇 번째로 pop() 되는지 return

# 풀이
# max_value = max(priorities)
# priorities_with_hash = [[i, hash(i)] for i in priorities]
# max_value_hash = priorities_with_hash[location][1]
# order = 0
# while len(priorities_with_hash) >= 0:
    # current = popleft()
    # current[0] >= max_value, 
        # if current[1] == max_value_hash:
            # return order
        # order += 1
    # current[0] < max_value:
        # priorities_with_hash.append(current)

from collections import deque
import random

def solution(priorities, location):
    order = 1
    priorities_with_hash = deque([[i, random.random()] for i in priorities])
    max_value = max(priorities)
    target_hash = priorities_with_hash[location][1]
    print(priorities_with_hash)
    
    while len(priorities_with_hash) >= 0:
        current = priorities_with_hash.popleft()
        
        if current[0] >= max_value: 
            if current[1] == target_hash:
                return order
            max_value = max([elem[0] for elem in priorities_with_hash])
            print(max_value)
            order += 1
            
        else: # current[0] < max_value
            priorities_with_hash.append(current)
            
    return order