// 문제 분석
// 완전탐색으로 풀이하면 2 ** 20 ~= 1,000,000 정도여서 사실 가능하다. 그러나 그래프 탐색으로 풀어보자.
// 모든 경우의 수를 따지려면 DFS가 적합하겠다
// 방향이 두 가지(+, -)가 있는 그래프를 탐색한다고 생각하면 쉽다
// dfs 함수가 재귀적으로 + / - 의 경우를 각각 호출하고, 
// 깊이가 numbers와 같아지면, target과 비교하여 cnt하는 방식으로 풀어보자

// 의사 코드
// func dfs(depth:int, sum:Int) -> Int
    // depth == numbers.size && sum == target인 경우 cnt += 1
    // depth + 1이 범위(numbers.size) 벗어나면 return
    // 두 가지 방향 재귀적으로 탐색
    // dfs(depth + 1, sum + numbers[depth + 1])
    // dfs(depth + 1, sum - numbers[depth + 1])
// func solution()
// dfs(-1, 0) 호출
// return cnt

import Foundation

func solution(_ numbers:[Int], _ target:Int) -> Int {
    var cnt = 0
    
    func dfs(_ depth: Int, _ sum: Int) {
        // depth == numbers.count - 1 && sum == target인 경우 cnt += 1
        if depth == numbers.count - 1 && sum == target {
            cnt += 1
            return // 재귀 탐색 종료
        }
        // depth + 1이 범위(numbers.count)보다 작으면 진행, 벗어나면 return
        guard depth + 1 < numbers.count else { return }
        // 두 가지 방향 재귀적으로 탐색
        // dfs(depth + 1, sum + numbers[depth + 1])
        dfs(depth + 1, sum + numbers[depth + 1])
        // dfs(depth + 1, sum - numbers[depth + 1])
        dfs(depth + 1, sum - numbers[depth + 1])
    }
    
    // dfs(-1, 0) 호출
    dfs(-1, 0) // 첫 번째 인덱스부터 방향이 갈리므로
    
    // return cnt
    return cnt
}