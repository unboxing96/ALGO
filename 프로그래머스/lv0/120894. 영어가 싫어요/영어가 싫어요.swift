import Foundation

let dic : [String: String] = ["zero": "0", "one" : "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"]

func solution(_ numbers:String) -> Int64 {
    
    var tmp = ""
    var ans = ""
    
    for chr in numbers {
        tmp += String(chr)
        
        if let x = dic[tmp] {
            ans += x
            tmp = ""
        }
    }
    
    
    return Int64(ans)!
}