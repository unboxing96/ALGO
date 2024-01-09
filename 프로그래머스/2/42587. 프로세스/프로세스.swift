
// 문제는 location에 위치한 값이 dequeue 되는 순간을 어떻게 측정할 것인가 ?
// 쉽다 cnt 변수를 두면 된다
// dequeue 할 때마다 cnt를 하나씩 올린다
// location 위치만 true이고, priorities와 길이가 같은 Bool 배열을 만들어서, priorities 배열과 똑같이 queue를 돌리고, dequeue 될 때 해당 위치가 true인 경우에 cnt를 출력하도록 한다.

// priorities를 순차적으로 탐색하며, dequeue한 값이 max 값과 일치하면 버린다. cnt += 1
// 일치하지 않으면(더 작으면) 다시 enqueue 한다
// 이것을 Bool 배열에도 똑같이 적용한다
// true인 index가 버려지면 cnt를 return 한다


import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    
    var priorities = priorities
    var location = location
    var result = 0
    
    while priorities.count > 0 {
        location -= 1
        let maxVal = priorities.max()!
        let front = priorities[0]
        if front != maxVal {
            priorities.append(front)
            priorities.removeFirst()
            if location < 0 {
                location = priorities.count - 1
            }
        } else {
            result += 1
            priorities.removeFirst()
            if location < 0 { break }
        }
    }
    
    return result
}
