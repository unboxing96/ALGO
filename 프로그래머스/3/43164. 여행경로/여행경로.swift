import Foundation

func solution(_ tickets: [[String]]) -> [String] {
    var routes = [String: [String]]()
    for ticket in tickets {
        routes[ticket[0], default: [String]()].append(ticket[1])
    }
    for (key, _) in routes {
        routes[key]?.sort(by: >) // 알파벳 역순으로 정렬 (스택이므로)
    }
    
    var result = [String]()
    func dfs(_ airport: String) {
        while let next = routes[airport]?.popLast() {
            dfs(next)
        }
        result.append(airport)
    }
    
    dfs("ICN")
    return result.reversed()
}