# 이해
# bridge_length는 다리에 올라갈 수 있는 트럭 수. 동시에 트럭이 이동해야 하는 길이.
# weight는 다리가 버틸 수 있는 무게. 트럭의 개수가 bridge_length보다 적어도, 무게 기준을 만족해야 한다.
# 모든 트럭이 다리를 건너는 데까지 걸리는 시간을 return

# 풀이
# 정석적인 원형 큐로 풀이해보자
# bridge = deque([])
# bridge.append(truck_weights[0])
# bridge_sum += truck_weights[0]
# time = 0

# while True:
    # time += 1
    # out_truck = bridge.popleft()
    # bridge_sum -= out_truck
    # if out_truckt > 0 and len(truck_weights) == 0:
        # return time
    
    # if bridge_sum + truck_weights[0] < weight:
        # in_truck = truck_weights.popleft()
        # bridge.append(in_truck)
        # bridge_sum += in_truck
        
    # else:
        # bridge.append(out_truck)

from collections import deque
        
def solution(bridge_length, weight, truck_weights):
    
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    bridge_sum = 0
    time = 0

    while truck_weights or bridge_sum > 0:
        time += 1
        out_truck = bridge.popleft()
        bridge_sum -= out_truck

        if truck_weights and bridge_sum + truck_weights[0] <= weight:
            in_truck = truck_weights.popleft()
            bridge.append(in_truck)
            bridge_sum += in_truck
        else:
            bridge.append(0)
    
    return time