import Foundation

func solution(_ numbers:[Int]) -> Int {
    let newArr = numbers.sorted(by: >)
    return newArr[0] * newArr[1]
}