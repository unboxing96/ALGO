import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0], k = input[1]
let degreesArr = readLine()!.split(separator: " ").map { Int($0)! }

var window = degreesArr[0..<k].reduce(0) { $0 + $1 }
var maxValue = window

for i in 0..<n - k {
    window = window - degreesArr[i] + degreesArr[i + k]
    maxValue = maxValue > window ? maxValue : window
}

print(maxValue)