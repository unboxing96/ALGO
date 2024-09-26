import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    
    var left = 0
    var right = 0
    
    for size in sizes {
        let (a, b) = (size[0], size[1])
        left = max(left, max(a, b))
        right = max(right, min(a, b))
    }

    return left * right
}