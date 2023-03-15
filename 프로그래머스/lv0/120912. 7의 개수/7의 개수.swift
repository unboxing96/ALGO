import Foundation

func solution(_ array:[Int]) -> Int {
    
    let seven : Character = "7"
    var res = 0
    
    for ar in array {
        res += String(ar).filter{$0 == seven}.count
    }
    
    return res
}