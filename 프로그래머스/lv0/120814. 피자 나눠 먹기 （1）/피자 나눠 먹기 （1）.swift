import Foundation

func solution(_ n:Int) -> Int {
    
    var cnt = 1
    
    while true {
        if 7 * cnt >= n {
            return cnt
        } else {
            cnt += 1
        }
    }
}