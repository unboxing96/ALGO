import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var lastReleaseDate: Int = 0
    var numOfReleases: [Int] = []
    for i in 0..<progresses.count {
        let progress = Double(progresses[i])
        let speed = Double(speeds[i])
        let day = Int(ceil((100 - progress) / speed))
        if day > lastReleaseDate {
            lastReleaseDate = day
            numOfReleases.append(1)
        } else {
            numOfReleases[numOfReleases.count - 1] += 1
        }
    }
    return numOfReleases
}