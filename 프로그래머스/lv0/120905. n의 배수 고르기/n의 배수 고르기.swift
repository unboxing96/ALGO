import Foundation

func solution(_ n:Int, _ numlist:[Int]) -> [Int] {
    
    var newArr = [Int]()
    
    for num in numlist {
        if num % n == 0 {
            newArr.append(num)
        }
    }
    
    return newArr
}