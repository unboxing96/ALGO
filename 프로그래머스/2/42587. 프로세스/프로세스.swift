// location은 targetIndex로 관리한다.
// cPriorities.count > 0인 동안 반복한다.
// priorities를 탐색하며, front 값보다 더 큰 값이 남아있는지 확인한다
// 더 큰 값이 남아있다면, removeFirst -> append 한다
    // 이때 targetIndex -= 1을 한다. 0보다 작아지면 배열의 크기를 값으로 한다.
// 더 큰 값이 남아있지 않다면, removeFirst 한다
    // 이때 targetIndex가 0이라면, 조건 달성이다. 전체 배열 - 현재 배열 + 1을 return 한다
    // 아니라면 targetIndex -= 1을 한다.


import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    
    // location은 targetIndex로 관리한다.
    var targetIndex = location
    var cPriorities = priorities
    
    // cPriorities.count > 0인 동안 반복한다.
    while cPriorities.count > 0 {
        // priorities를 탐색하며, front 값보다 더 큰 값이 남아있는지 확인한다
        if cPriorities.contains(where: { $0 > cPriorities[0] }) {
            // 더 큰 값이 남아있다면, removeFirst -> append 한다
            let first = cPriorities.removeFirst()
            cPriorities.append(first)
            // 이때 targetIndex -= 1을 한다. 0보다 작아지면 배열의 크기를 값으로 한다.
            targetIndex = targetIndex - 1 < 0 ? cPriorities.count - 1 : targetIndex - 1
        } else {
            // 더 큰 값이 남아있지 않다면,
            // 이때 targetIndex가 0이라면, 조건 달성이다. 전체 배열 - 현재 배열 + 1을 return 한다
            if targetIndex == 0 {
                return priorities.count - cPriorities.count + 1
            }
            // removeFirst 한다
            // 아니라면 targetIndex -= 1을 한다.       
            cPriorities.removeFirst()
            targetIndex -= 1
        }
    }
    return 0
}