import Foundation

func solution(_ angle:Int) -> Int {
    switch angle {
        case let x where x < 90:
            return 1
        case let x where x == 90:
            return 2
        case let x where x < 180:
            return 3
        default:
            return 4
    }
}