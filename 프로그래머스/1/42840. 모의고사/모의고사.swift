// 문제 접근
// 배열의 크기는 최대 10 ** 4 이므로, O(N^2)까지 괜찮겠다.
// 1. 각각의 패턴 대로 길이 10 ** 4의 배열을 미리 생성해놓고 비교하면 O(N)으로 가능.
    // 단, 메모리 공간이 3 * 0(N)만큼 추가적으로 소모
// 2. 각 패턴의 점화식을 만들어서 비교. O(N)
    // 메모리 공간의 낭비도 거의 없다.
    // 그러나 실제 코테에서는, 완탐으로도 O(N)의 풀이가 가능한데, 굳이 점화식을 만들 필요는 없겠다.

// 문제 접근
// 배열의 크기는 최대 10 ** 4 이므로, O(N^2)까지 괜찮겠다.
// 1. 각각의 패턴 대로 길이 10 ** 4의 배열을 미리 생성해놓고 비교하면 O(N)으로 가능.
    // 단, 메모리 공간이 3 * 0(N)만큼 추가적으로 소모
// 2. 각 패턴의 점화식을 만들어서 비교. O(N)
    // 메모리 공간의 낭비도 거의 없다.
    // 그러나 실제 코테에서는, 완탐으로도 O(N)의 풀이가 가능한데, 굳이 점화식을 만들 필요는 없겠다.

import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let size = answers.count
    let multipleValue = Int(pow(10.0, 3))
    var resultArr = [0, 0, 0]
    let studentOne = Array(repeating: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], count: multipleValue).flatMap { $0 }
    let studentTwo = Array(repeating: [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5], count: multipleValue).flatMap { $0 }
    let studentThree = Array(repeating: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5], count: multipleValue).flatMap { $0 }
    
    for i in 0..<size {
        let currentAnswer = answers[i]
        
        if currentAnswer == studentOne[i] { resultArr[0] += 1 }
        if currentAnswer == studentTwo[i] { resultArr[1] += 1 }
        if currentAnswer == studentThree[i] { resultArr[2] += 1 }
    }
    
    let highestScore = resultArr.max()!

    return resultArr.indices.filter { resultArr[$0] == highestScore }.map { $0 + 1 }
}
