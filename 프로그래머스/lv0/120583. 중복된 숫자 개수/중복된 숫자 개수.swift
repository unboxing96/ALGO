import Foundation

func solution(_ array:[Int], _ n:Int) -> Int {
    
    var cnt = 0
    
    for a in array {
        if a == n {
            cnt += 1
        }
    }
    
    return cnt
}