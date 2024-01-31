// 문제 분석
// n의 크기는 10 ** 4이므로, O(N^2)까지는 괜찮겠다.
// 2차원 배열을 탐색하며, 가로와 세로 길이를 각각의 배열에 저장한 뒤에, 각 배열의 max를 곱한 것을 return
// 가로 <-> 세로를 바꾸는 것이 가능하므로, 각 배열에 저장하기 전에, 비교를 통해 큰 값 / 작은 값으로 분류하는 것이 낫겠다.

// 의사 코드
// sizes 배열을 forEach로 탐색한다.
    // if $0 > $1인 경우에, 큰 값 배열에 $0을, 작은 값 배열에 $1을 추가한다, else 라면 반대로 한다.
// 큰 값 배열, 작은 값 배열에서 각각 .max() 값을 구해 곱한 값을 return 한다.

import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    
    var biggerArr = [Int]()
    var smallerArr = [Int]()
    var answer = 0
    // sizes 배열을 forEach로 탐색한다.
    sizes.forEach {
        // if $0 > $1인 경우에, 큰 값 배열에 $0을, 작은 값 배열에 $1을 추가한다,
        // else 라면 반대로 한다.
        biggerArr.append( $0[0] > $0[1] ? $0[0] : $0[1] )
        smallerArr.append( $0[0] > $0[1] ? $0[1] : $0[0] )
    }
    // 큰 값 배열, 작은 값 배열에서 각각 .max() 값을 구해 곱한 값을 return 한다.
    answer = biggerArr.max()! * smallerArr.max()!
    return answer
}