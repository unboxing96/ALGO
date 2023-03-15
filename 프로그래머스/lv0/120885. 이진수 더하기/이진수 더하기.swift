import Foundation

func solution(_ bin1:String, _ bin2:String) -> String {
    
    var binFirst = 0
    var binSecond = 0
    
    if let x = Int(bin1, radix: 2) {
        binFirst = x
    }

    if let x = Int(bin2, radix: 2) {
        binSecond = x
    }
    
    var ans = String(binFirst + binSecond, radix: 2)
    
    return ans
}