import Foundation

func solution(_ order:Int) -> Int {
    
    var cnt = 0
    
    for o in String(order) {
        switch o {
            case "3", "6", "9":
                cnt += 1
            default:
                continue
        }
    }
    
    return cnt
}