// 이해
// 주어진 wires를 모두 연결한 연결 그래프를 만든다
// wires 배열을 탐색하며, 각 원소가 끊어진 경우를 상정한다. wires의 길이는 최대 99이다.
// 끊어진 상태에서 두 전력망의 송전탑 개수의 차이를 업데이트 한다.
    // dfs로 하나의 전력망의 크기를 구한다. 절댓값(n - 크기)로 result를 업데이트 한다.

// 의사코드
// var result = 0
// var graph = [Int](repeating: [], count: n + 1)
// for i in 0..<graph.count {}
    // for j in wires.count {}
        // if i == j { continue }
        // let a = wires[j][0]
        // let b = wire[j][1]
        // graph[a].append(b)
        // graph[b].append(a)
    // var visited = [Bool](repeating: false, count: graph.count)
    // let startNode = graph.first![0]
    // dfs(graph, startNode, visited)
    // let tmpResult = abs(n - (visited.filter { $0 == True }.count * 2))
    // result = max(result, tmpResult)
// return result

// func dfs(_ graph: [[Int]], _ startNode: Int, _ visited: inout [Bool]) {}
// visited[startNode] = true
// for nextNode in graph[startNode] {}
    // if !visited[nextNode] {}
        // dfs(graph, nextNode, &visited)
   

import Foundation

func solution(_ n:Int, _ wires:[[Int]]) -> Int {
    
    var result = Int.max
    
    for i in 0..<wires.count {
        
        var graph: [[Int]] = Array(repeating: [], count: n + 1)
        
        for j in 0..<wires.count {
            if i == j {
                continue
            }
            let a = wires[j][0]
            let b = wires[j][1]
            graph[a].append(b)
            graph[b].append(a)
        }
        
        var visited = [Bool](repeating: false, count: graph.count)

        if let firstArray = graph.first(where: {$0.count > 0}), let startNode = firstArray.first {
            dfs(graph, startNode, &visited)
        }

        let tmpResult = abs(n - (visited.filter { $0 == true }.count * 2))
        result = min(result, tmpResult)
    }
    
    return result
}

func dfs(_ graph: [[Int]], _ startNode: Int, _ visited: inout [Bool]) {
    visited[startNode] = true
    for nextNode in graph[startNode] {
        if !visited[nextNode] {
            dfs(graph, nextNode, &visited)
        }
    }
}