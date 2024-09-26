// 자르고 [i - 1 ... j - 1]
// 정렬하고
// k번째 [k - 1]

import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    
    var result = [Int]()

    for command in commands {
        let (left, right, k_idx) = (command[0], command[1], command[2])
        result.append(Array(array[left - 1 ... right - 1]).sorted()[k_idx - 1])
    }
    
    return result
}