import Foundation

func solution(_ my_string:String, _ num1:Int, _ num2:Int) -> String {
    
    var ans = ""
    
    for i in 0..<my_string.count {
        if i == num1 {
            let idx = my_string.index(my_string.startIndex, offsetBy: num2)
            ans += String(my_string[idx])
        } else if i == num2 {
            let idx = my_string.index(my_string.startIndex, offsetBy: num1)
            ans += String(my_string[idx])
        } else {
            let idx = my_string.index(my_string.startIndex, offsetBy: i)
            ans += String(my_string[idx])
        }
    }
    
    return ans
}