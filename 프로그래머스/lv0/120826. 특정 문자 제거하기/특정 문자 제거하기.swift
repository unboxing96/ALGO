import Foundation

func solution(_ my_string:String, _ letter:String) -> String {
    
    var ans = ""
    
    for m in my_string {
        if letter == String(m) {
            continue
        } else {
            ans += String(m)
        }
    }
    
    return ans
}