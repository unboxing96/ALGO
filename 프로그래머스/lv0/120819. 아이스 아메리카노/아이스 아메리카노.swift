import Foundation

func solution(_ money:Int) -> [Int] {
    
    var newArr = [0, 0]
    
    newArr[0] = money / 5500
    newArr[1] = money % 5500
    
    return newArr
}