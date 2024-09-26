import Foundation

let line = readLine()!.split(separator: " ").map{Int(String($0))!}
let N = line[0]
let M = line[1]
let V = line[2]

var graph : [[Int]] = Array(repeating: [], count: N+1)
var visited = Array(repeating: false, count: N+1)
var result = ""

for _ in 0..<M {
    let relation = readLine()!.split(separator: " ").map{Int(String($0))!}
    let a = relation[0]
    let b = relation[1]
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
}

func dfs(now: Int) {
    visited[now] = true
    result += "\(now) "
    
    for next in graph[now] {
        if visited[next] == false {
            dfs(now: next)
        }
    }
}

func bfs(now: Int) {
    var q = [Int]()
    q.append(now)
    visited[now] = false
    
    while !q.isEmpty {
        let x = q.removeFirst()
        result += "\(x) "
        
        for next in graph[x] {
            if visited[next] {
                visited[next] = false
                q.append(next)
            }
        }
    }
}

dfs(now: V)
print(result)

result = ""
bfs(now: V)
print(result)








