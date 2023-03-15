func solution(_ keyinput:[String], _ board:[Int]) -> [Int] {
    
    // graph 1 <= x <= n and 1 <= y <= m
    // up = [0, 1]      -> [1, 0]
    // down = [0, -1]   -> [-1, 0]
    // right = [1, 0]   -> [0, 1]
    // left = [-1, 0]   -> [0, -1]
    
    var graph = [[Int]]()
    var x = board[1] / 2
    var y = board[0] / 2
    var start = [x, y]

    
    let dir : [String: [Int]] = ["up" : [1, 0], "down": [-1, 0], "right": [0, 1], "left": [0, -1]]
    
    for i in 0..<board[1] {
        graph.append([Int](repeating: 0, count: board[0]))
    }
    
    for key in keyinput {
        
        let nx = start[0] + dir[key]![0]
        let ny = start[1] + dir[key]![1]
        
        if 0 <= nx && nx < board[1] && 0 <= ny && ny < board[0] {
            start[0] = nx
            start[1] = ny
        }
    }
    
    return [start[1] - y, start[0] - x]
}
