import Foundation

func solution(_ strlist:[String]) -> [Int] {
    
    var newArr = [Int]()
    
    for s in strlist {
        newArr.append(s.count)
    }
    
    return newArr
}