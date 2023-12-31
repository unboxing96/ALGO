// 100 * 100이므로 완전탐색 가능
// 순서대로 탐색하다가 1을 만나면: 범위를 벗어나지 않는, 0을 만나면: 2로 바꾼다 (8방향에 대하여)
// 끝까지 탐색한 이후, 0의 개수를 return 한다

// 바깥쪽 배열의 길이 board.count
// 안쪽 배열의 길이 board[0].count

import Foundation

func solution(_ board:[[Int]]) -> Int {
    
    var newBoard = board
    var result = 0
    
    let dx = [-1, -1, -1, 1, 1, 1, 0, 0]
    let dy = [-1, 0, 1, -1, 0, 1, -1, 1]
    
    for i in 0..<newBoard.count {
        for j in 0..<newBoard[0].count {
            if newBoard[i][j] == 1 {
                for k in 0..<8 {
                    let nx = i + dx[k]
                    let ny = j + dy[k]
                    
                    if nx < 0 || nx >= newBoard.count || ny < 0 || ny >= newBoard[0].count {
                        continue
                    }
                    
                    if newBoard[nx][ny] == 0 {
                        newBoard[nx][ny] = 2
                    }
                }
            }
        }
    }
    
    for i in 0..<newBoard.count {
        let rowZeroCount = newBoard[i].filter { $0 == 0 }.count
        result += rowZeroCount
    }
    
    return result
}