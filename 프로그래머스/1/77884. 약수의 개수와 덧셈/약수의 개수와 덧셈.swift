// 약수의 개수가 홀수인 수 == 제곱수
// 제곱수는 빼고 나머지는 더한다
// left, right의 크기가 1000이라 O(n^2)해도 풀이가 가능할 듯

// 제곱수 판별 방법
// 1. n이 제곱수인지 판별하기 위해서 2 ~ n ** 1/2까지 제곱값과 비교
// 2. sqrt(n) == pow(Double(int(sqrt(n))), 2.0) 확인

import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    
    var sum = 0
    for num in left...right {
        var checker = false
        for numForCheck in 1...Int(pow(Double(num), 0.5)) {
            if num == Int(pow(Double(numForCheck), 2)) {
                sum -= num
                checker = true
            }
        }
        if !checker {
            sum += num
        }
    }
    
    return sum
}