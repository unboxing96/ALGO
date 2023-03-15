import Foundation

func solution(_ n:Int) -> [Int] {
    
    var newN = n
    var i = 2
    var newSet = Set<Int>()
    
    while true {
        if newN % i == 0 {
            newSet.insert(i)
            newN /= i
        } else {
            i += 1
        }
        
        if newN == 1 {
            return Array(newSet).sorted()
        }
    }
}