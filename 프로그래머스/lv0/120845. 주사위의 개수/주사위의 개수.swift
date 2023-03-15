import Foundation

func solution(_ box:[Int], _ n:Int) -> Int {
    
    var ans = 1
    
    for b in box {
        if let b = Int(String(b)) {
            ans *= b / n   
        }
    }
    
    return ans
}