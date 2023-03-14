import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    
    var ans: [Int] = [0, 0]
    
    for num in num_list {
        if num % 2 == 0 {
            ans[0] += 1
        } else {
            ans[1] += 1
        }
    }
    
    return ans
}