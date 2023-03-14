import Foundation

func solution(_ numbers:[Int], _ num1:Int, _ num2:Int) -> [Int] {
    let answer = numbers[num1...num2]
    return Array(answer)
}