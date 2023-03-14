import Foundation

func solution(_ n:Int) -> Int {
    
    var tot : Int = 0
    
    for num in String(n) {
        if let x = Int(String(num)) {
            tot += x
        }
    }
    
    return tot
}