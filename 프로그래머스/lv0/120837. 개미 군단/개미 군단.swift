import Foundation

func solution(_ hp:Int) -> Int {
    
    let ants = [5, 3, 1]
    var res = 0
    var newHp = hp
    
    for i in 0...2 {
        
        res += newHp / ants[i]
        newHp %= ants[i]
    }
    
    return res
}