import Foundation

func solution(_ numbers:[Int], _ direction:String) -> [Int] {
    
    var newArr = numbers
    
    if direction == "right" {
        let x = newArr.remove(at: numbers.count - 1)
        newArr.insert(x, at: 0)
    } else {
        let x = newArr.remove(at: 0)
        newArr.append(x)
    }
    
    return newArr
}