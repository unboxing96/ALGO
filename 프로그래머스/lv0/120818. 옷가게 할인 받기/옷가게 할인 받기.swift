import Foundation

func solution(_ price:Int) -> Int {
    
    switch price {
        case let x where x >= 500000:
            return Int(Double(price) * 0.8)
        case let x where x >= 300000:
            return Int(Double(price) * 0.9)
        case let x where x >= 100000:
            return Int(Double(price) * 0.95)
        default:
            return price
    }
    
    return 0
}