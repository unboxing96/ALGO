import Foundation

func solution(_ numbers:[Int]) -> Int {
    
    var newNum = numbers.sorted()
    return max(newNum[0] * newNum[1], newNum[newNum.count - 1] * newNum[newNum.count - 2])
}