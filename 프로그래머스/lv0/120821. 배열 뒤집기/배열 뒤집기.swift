import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    
    var newArray = [Int]()
    
    for i in stride(from: num_list.count-1, to: -1, by: -1) {
        newArray.append(num_list[i])
    }
    
    
    return newArray
}