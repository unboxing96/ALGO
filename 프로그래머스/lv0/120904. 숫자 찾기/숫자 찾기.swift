import Foundation

func solution(_ num:Int, _ k:Int) -> Int {
    
    var idx = -1
    
    let strNum = String(num)
    
    for i in 0..<strNum.count {
        let nthIdx = strNum.index(strNum.startIndex, offsetBy: i)
        
        if String(k) == String(strNum[nthIdx]) {
            idx = i
            break
        }
    }
    
    if idx == -1 {
        return idx
    } else {
        return idx + 1
    }
}