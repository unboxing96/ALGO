import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    
    var result = [Int]()
    
    for num in numbers {
        result.append(num * 2)
    }
    
    return result
}