// 1. n을 2부터 n-1까지 탐색하며 약수가 1개라도 있으면 합성수
// DP를 사용하는 방법이 있을 듯한데.. 

import Foundation

func solution(_ n:Int) -> Int {
    
    var cnt = 0
    
    if n == 1 {
        return 0
    }
    
    for i in 2...n {
        for j in 2..<i {
            if i % j == 0 {
                cnt += 1
                break
            }
        }
    }
    
    return cnt
}