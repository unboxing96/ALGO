import Foundation

func solution(_ array:[Int]) -> [Int] {
    
    var most = 0
    var most_idx = 0
    
    for i in 0..<array.count {
        if most < array[i] {
            most = array[i]
            most_idx = i
        }
    }
    
    return [most, most_idx]
}