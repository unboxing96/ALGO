import Foundation

func solution(_ numbers:[Int], _ k:Int) -> Int {
    
    let order = 2 * k - 1
    var idx = 0
    
    if order % numbers.count == 0 {
        idx = numbers.count - 1
    } else {
        idx = order % numbers.count - 1
    }
    
    return numbers[idx]
}