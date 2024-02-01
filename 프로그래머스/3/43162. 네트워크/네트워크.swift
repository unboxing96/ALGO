import Foundation

func find(_ x: Int, _ rootArr: inout [Int]) -> Int {
    if rootArr[x] != x {
        rootArr[x] = find(rootArr[x], &rootArr)
    }
    return rootArr[x]
}

func union(_ x: Int, _ y: Int, _ rootArr: inout [Int]) {
    let rootX = find(x, &rootArr)
    let rootY = find(y, &rootArr)
    if rootX < rootY {
        rootArr[rootY] = rootX
    } else {
        rootArr[rootX] = rootY
    }
}

func solution(_ n: Int, _ computers: [[Int]]) -> Int {
    var rootArr = Array(0..<n)

    for i in 0..<n {
        for j in 0..<n {
            if computers[i][j] == 1 && i != j {
                union(i, j, &rootArr)
            }
        }
    }

    let uniqueNetworks = Set(rootArr.map { find($0, &rootArr) })
    return uniqueNetworks.count
}