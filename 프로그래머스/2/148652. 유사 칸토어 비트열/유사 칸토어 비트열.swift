import Foundation

func solution(_ n:Int, _ l:Int64, _ r:Int64) -> Int {
    return f(n, r) - f(n, l - 1)
}

func f(_ n: Int, _ k: Int64) -> Int {
    
    if n == 1 {
        return Int(k <= 2 ? k : k - 1)
    }
    
    let div = Int(k) / Int(pow(5.0, Double(n - 1)))
    let mod = Int(k) % Int(pow(5.0, Double(n - 1)))
    let mul = Int(pow(4.0, Double(n - 1)))
    
    if div < 2 {
        return mul * div + f(n-1, Int64(mod))
    } else if div == 2 {
        return mul * div
    } else {
        return mul * (div - 1) + f(n-1, Int64(mod))
    }
}