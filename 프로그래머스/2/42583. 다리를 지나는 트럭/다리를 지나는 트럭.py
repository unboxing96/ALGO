# 문제 분석
# bridge_length 길이의 다리가 있다.
# 다리는 weight 이하의 무게까지 버틸 수 있다.
# 모든 트럭이 다리를 건너는 데에 소요되는 시간을 구하라

# 접근
# bridge_length 길이의 배열을 선언한다.
# currentWeight에 현재 다리 위에 올라간 트럭의 총 무게를 저장한다.
# time을 선언한다.
# 

from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    bridge = deque([0] * bridge_length)
    truck_weights = deque(reversed(truck_weights))
    truckCount = len(truck_weights)
    currentWeight = 0
    time = 0
    done = []
    
    while True:
        time += 1
        now = bridge.popleft()
        
        if now:
            done.append(now)
            currentWeight -= now
            if len(done) == truckCount:
                return time
        
        if truck_weights and currentWeight + truck_weights[-1] <= weight:
            nowTruck = truck_weights.pop()
            currentWeight += nowTruck
            bridge.append(nowTruck)
        else:
            bridge.append(0)





