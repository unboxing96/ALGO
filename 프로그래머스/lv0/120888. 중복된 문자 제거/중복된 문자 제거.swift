import Foundation

func solution(_ my_string:String) -> String {
    
    var newStr = ""
    
    for m in my_string {
        if newStr.contains(String(m)) {
            continue
        } else {
            newStr += String(m)
        }
    }
    
    return newStr
}