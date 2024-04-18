// 이해
// 노란색은 반드시 가운데에서 사각형을 이루어야 한다. 갈색에게 빈틈을 내어줘서는 안 된다.
// 갈색은 반드시 노란색을 둘러싸는 형태로 사각형을 이루어야 한다.
// 사각형의 넓이는 결정되어 있다. 갈색 + 노란색
// 약수...를 활용하는 문제인 듯하다.
// 노란색이 24인 경우를 예로 들어보자.
// (1, 24)의 형태로 배치가 되었다면, 갈색은 그것을 둘러싸기 위해 (24 + 2) * 2 + (1 * 2)가 필요하다.
// (2, 12)의 형태로 배치가 되었다면, 갈색은 (12 + 2) * 2 + (2 * 2)가 필요하다.
// (4, 6)의 형태로 배치가 되었다면, 갈색은 (4 + 2) * 2 + (6 * 2)가 필요하다. 이때 24가 된다.
// 이때 노란색의 가로 길이와 세로 길이에 2씩 더하고 길이가 긴 것 순서로 배치하면 된다.
// n의 제곱수까지만 판단하면 되므로 2,000,000 입력값의 O(logN)의 시간이 소요되는 것이다.

// 의사코드
// for i in 1...int(sqrt(yellow, 2)) {}
    // if yellow % i == 0 {}
        // let y_width = i
        // let y_height = yellow % i
        // if brown == (y_width + 2) * 2 + y_height * 2 {}
            // brown_width = max(y_width, y_height) + 2
            // brown_height = min(y_width, y_height) + 2
            // return [brown_width, brown_height]

import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    
    var brown_width = 0
    var brown_height = 0
    
    for i in 1...Int(sqrt(Double(yellow))) {
        if yellow % i == 0 {
            let y_width = i
            let y_height = yellow / i
            if brown == (y_width + 2) * 2 + y_height * 2 {
                brown_width = max(y_width, y_height) + 2
                brown_height = min(y_width, y_height) + 2
            }
        }
    }
    
    return [brown_width, brown_height]
}