import Foundation

func solution(_ n:Int) -> Int {
    
    var cnt = 1
    
    while true {
        if (cnt * 6) % n == 0 {
            return cnt
        }
        
        cnt += 1
    }
}