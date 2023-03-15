import Foundation

func solution(_ array:[Int], _ n:Int) -> Int {
    
    var tot = 100
    var ans = 0
    
    var newArr = array.sorted(by: >)
    
    for a in newArr {
        if abs(a - n) <= tot {
            tot = abs(a - n)
            ans = a
        }
    }
    
    return ans
}