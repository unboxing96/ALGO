import Foundation

let n = readLine()!.components(separatedBy: [" "]).map { Int($0)! }

var num = n[0]

for i in 0..<num{
    let str = String(repeating: "*", count: i + 1)
    print(str)
}