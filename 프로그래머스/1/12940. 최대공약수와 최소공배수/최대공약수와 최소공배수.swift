// 최대공약수: 1. 두 수의 약수를 구해서 최댓값을 구함. 2. 유클리드 호제법
// 최소공배수: 두 수의 곱을 최대공약수로 나눈다

// 1. a, b를 비교한다. 큰 것이 a 작은 것이 b
// 2. a % b의 나머지를 구한다. r이 나머지
// 3. r == 0 이면 종료. 구해지지 않았으면 (b, r)을 호출한다 재귀적으로.

func solution(_ n:Int, _ m:Int) -> [Int] {
    
    let gcdNum = gcd(n, m)
    let lcmNum = n * m / gcdNum
    
    return [gcdNum, lcmNum]
}

func gcd(_ a: Int, _ b: Int) -> Int {
    
    var (aa, bb) = a >= b ? (a, b) : (b, a)
    let rr = aa % bb
    print(aa, bb, rr)
    
    if rr == 0 {
        return bb
    } else {
        return gcd(bb, rr)
    }
}