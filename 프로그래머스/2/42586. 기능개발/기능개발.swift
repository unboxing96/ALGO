// 큐로 풀이한다 (취소)
// while 문으로 반복한다
// progresses 배열을 복사하고, speeds 배열의 원소값을 복사한 배열의 원소값에 각각 더해준다
// 가장 왼쪽의 값이 100 이상이 되면
// progresses 배열을 탐색하며 100 이상이 되는 값들을 모두 0으로 바꾼다
// speeds 배열에서도 0으로 바꾼다
// 바뀐 원소의 개수를 return 배열에 append 한다
// progresses 배열이 빈 배열이 될 때까지 반복한다

import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    
    var answer = [Int]()
    var copiedProgresses = progresses
    var copiedSpeeds = speeds
    var pointer = 0
    
    while pointer < speeds.count {
        
        var count = 0
        
        for idx in 0..<speeds.count {
            copiedProgresses[idx] += speeds[idx]
        }
        
        if copiedProgresses[pointer] >= 100 {
            while pointer < speeds.count && copiedProgresses[pointer] >= 100 {
                copiedProgresses[pointer] = 0
                copiedSpeeds[pointer] = 0
                pointer += 1
                count += 1
            }
            
            answer.append(count)
        }
    }
    
    return answer
}