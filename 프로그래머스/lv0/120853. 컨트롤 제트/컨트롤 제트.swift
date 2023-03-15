import Foundation

func solution(_ s:String) -> Int {
    
    // optional int append
    // face "Z", pop to array
    
    var newArr = [Int]()
    var inputArr = s.split(separator: " ")
    
    for elem in inputArr {
        guard let x = Int(elem) else {
            if !newArr.isEmpty {
                newArr.popLast()
            }
            continue
        }
        newArr.append(x)
    }

    
    let ans = newArr.reduce(0, +)
    
    return ans
}