import Foundation

func solution(_ array:[Int]) -> Int {
    
    var newArr = array.sorted()
    
    return newArr[array.count / 2]
}