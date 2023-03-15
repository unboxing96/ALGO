import Foundation

func solution(_ n:Int) -> Int {
    
    var tot = 0
    
    for num in 1...n {
        var tmp = 0
        for i in 1...num {
            if num % i == 0 {
                tmp += 1
            }
            
            if tmp >= 3 {
                tot += 1
                break
            }
        }
    }
    
    return tot
}