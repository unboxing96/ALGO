import Foundation

func solution(_ emergency:[Int]) -> [Int] {
    
    // search i in emergency, 
    // search j in emergency
    // if face bigger value, cnt += 1, 
    // else if face smaller value, cnt -= 1
    // else if face same value, continue
    
    var newArr = [Int]()
    
    for i in 0..<emergency.count {
        var cnt = 1
        for j in 0..<emergency.count {
            if emergency[i] < emergency[j] {
                cnt += 1
            } 
        }
        
        newArr.append(cnt)
    }
    
    return newArr
}