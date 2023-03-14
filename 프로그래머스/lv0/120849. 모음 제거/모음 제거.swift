import Foundation

func solution(_ my_string:String) -> String {
    
    let vowels = ["a", "e", "i", "o", "u"]
    var ans = ""
    
    for m in my_string {
        if vowels.contains(String(m)) {
            continue
        } else {
            ans += String(m)
        }
    }
    
    return ans
}