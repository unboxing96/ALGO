import Foundation

func recursion(_ n: Int, _ pos: Int64) -> Int {
    if n == 1 {
        return pos <= 2 ? Int(pos) : Int(pos) - 1
    }

    let base = Int64(pow(5.0, Double(n - 1)))
    let a = pos / base
    let b = pos % base
    var cnt = 0

    if a <= 1 {
        cnt = Int(pow(4.0, Double(n - 1))) * Int(a) + recursion(n - 1, b)
    } else if a == 2 {
        cnt = 2 * Int(pow(4.0, Double(n - 1)))
    } else {
        cnt = Int(pow(4.0, Double(n - 1))) * (Int(a) - 1) + recursion(n - 1, b)
    }

    return cnt
}

func solution(_ n: Int, _ l: Int64, _ r: Int64) -> Int {
    return recursion(n, r) - recursion(n, l - 1)
}
