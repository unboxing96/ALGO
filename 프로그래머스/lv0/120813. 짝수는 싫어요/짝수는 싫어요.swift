import Foundation

func solution(_ n:Int) -> [Int] {
    
    var newArr = [Int]()
    
    for i in 1...n {
        if i % 2 == 1 {
            newArr.append(i)
        }
    }
    
    return newArr
}