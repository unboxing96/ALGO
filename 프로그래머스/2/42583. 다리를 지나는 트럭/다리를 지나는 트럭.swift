// 내리는 데에는 1초가 소요된다
// 1번 칸으로 올라가는 데에는 1초가 소요된다
// 내려가고 올라오기는 비동기적으로 가능하다 (동시에)
// 1. 문제대로 구현해서 풀이하는 방법
// 2. 점화식을 도출해서 풀이하는 방법

// 1.번으로 해보자
// 커스텀 큐를 구현할 필요는 없는 듯하다. sum() 있으니까 10,000^2
// 2가지 큐가 필요하다. 다리 큐, 대기 큐
// 1가지 배열이 필요하다. 다리를 지난 배열
// while 문의 종료 조건은 다리를 지난 배열이 truck_weights의 길이와 같아지는 것
    // 반복을 시작한다 (1초)
    // 다리 큐를 dequeue 한다
        // 이때 dequeue가 0이 아니면 다리를 지난 배열에 append 한다
        // if 이때 다리 큐의 합이 weight 이하이고, 대기 큐가 비어있지 않으면,
            // 대기 큐를 dequeue 해서, 다리 큐에 enqueue 한다
                // 이때 다리 큐의 합이 weight 보다 작아야 한다
        // else 다리 큐에 0을 enqueue 한다

import Foundation

func solution(_ bridge_length:Int, _ weight:Int, _ truck_weights:[Int]) -> Int {
    
    // 2가지 큐가 필요하다. 다리 큐, 대기 큐
    var bridge = Array(repeating: 0, count: bridge_length)
    var qTruck_weights = Queue<Int>()
    // 1가지 배열이 필요하다. 다리를 지난 배열
    var afterBridge = [Int]()
    var time = 0
    var bridgeSum = 0
    
    for i in 0..<truck_weights.count {
        qTruck_weights.enqueue(truck_weights[i])
    }
    
    // while 문의 종료 조건은 다리를 지난 배열이 truck_weights의 길이와 같아지는 것
    while afterBridge.count < truck_weights.count {
        // 반복을 시작한다 (1초)
        time += 1
        
        // 다리 큐를 dequeue 한다
        let frontOfBridge = bridge.removeFirst()
        
        // 이때 dequeue가 0이 아니면 다리를 지난 배열에 append 한다
        if frontOfBridge != 0 {
            afterBridge.append(frontOfBridge)
            bridgeSum -= frontOfBridge
        }
        
        // if 다리 큐의 합이 weight 이하이고, 대기 큐가 비어있지 않으면,
        if !qTruck_weights.isEmpty {
            // 대기 큐를 dequeue 해서,
            let frontOfcTruck_weights = qTruck_weights.first!
            
            // 이때 다리 큐의 합이 weight 보다 작아야 한다
            if frontOfcTruck_weights + bridgeSum <= weight {
                // 다리 큐에 enqueue 한다
                bridgeSum += frontOfcTruck_weights
                bridge.append(qTruck_weights.dequeue()!)
            } else {
                // else 다리 큐에 0을 enqueue 한다
                bridge.append(0)
            }
        } else {
            // else 다리 큐에 0을 enqueue 한다
            bridge.append(0)
        }
    }
    
    return time
}

struct Queue<T> {
    private var data: [T] = []
    
    public var first: T? {
        return data.first
    }
    
    public var count: Int {
        return data.count
    }
    
    public var isEmpty: Bool {
        return data.isEmpty
    }
    
    public mutating func enqueue(_ element: T) {
        data.append(element)
    }
    
    public mutating func dequeue() -> T? {
        return self.isEmpty ? nil : data.removeFirst()
    }
}