import Foundation

func solution(_ n:Int) -> [Int] {
    
    var newArr = [Int]()
    
    for i in 1...n {
        if n % i == 0 {
            newArr.append(i)
        }
    }
    
    return newArr
}