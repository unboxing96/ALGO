import Foundation

func solution(_ n:Int, _ t:Int) -> Int {
    
    var ans = n
    
    for _ in 1...t {
        ans *= 2
    }
    
    return ans
}