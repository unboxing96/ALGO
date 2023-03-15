import Foundation
func solution(_ my_string: String) -> Int {
    var answer = 0
    var tmp = ""
    
    for ms in my_string {
        if let x = Int(String(ms)) {
            tmp += String(x)
        } else {
            if let x = Int(tmp) {
                answer += x
                tmp = ""
            }
        }
    }
    
    if let x = Int(tmp) {
        answer += x
    }
    
    return answer
}
