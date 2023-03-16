func solution(_ array: [Int]) -> Int {
    var freq = [Int: Int]()
    for num in array {
        freq[num, default: 0] += 1
    }
    let maxFreq = freq.values.max() ?? 0
    let modes = freq.filter { $0.value == maxFreq }.keys
    return modes.count == 1 ? modes.first! : -1
}
