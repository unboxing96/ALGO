import Foundation

func solution(_ i:Int, _ j:Int, _ k:Int) -> Int {
    
    var tot = 0
    let charToCount = String(k)
    
    for num in i...j {
        let count = String(num).filter { String($0) == charToCount }.count
        tot += count
    }
    
    return tot
}