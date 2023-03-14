import Foundation

func solution(_ sides:[Int]) -> Int {
    
    var newArr = sides.sorted()
    
    if newArr[0] + newArr[1] > newArr[2] {
        return 1
    } else {
        return 2
    }
}