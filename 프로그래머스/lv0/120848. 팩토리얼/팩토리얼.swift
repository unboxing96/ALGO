import Foundation

func solution(_ n:Int) -> Int {
    
    var tot = 1
    var cnt = 1
    
    while true {
        tot *= cnt
        
        if tot > n {
            return cnt - 1
        }
        
        cnt += 1
    }
}