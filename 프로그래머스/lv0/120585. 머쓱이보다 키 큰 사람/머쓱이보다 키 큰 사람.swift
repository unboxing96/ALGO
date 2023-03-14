import Foundation

func solution(_ array:[Int], _ height:Int) -> Int {
    
    var newArr = array.sorted()
    var cnt = 0
    
    for a in array {
        if a > height {
            cnt += 1
        }
    }
    
    return cnt
}