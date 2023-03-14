import Foundation

func solution(_ my_string:String) -> Int {
    
    var tot = 0
    
    for m in my_string {
        if let x = Int(String(m)) {
            tot += x
        }
    }
    
    return tot
}