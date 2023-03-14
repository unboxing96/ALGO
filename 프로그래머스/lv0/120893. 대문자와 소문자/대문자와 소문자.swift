import Foundation

func solution(_ my_string:String) -> String {
    
    var ans = ""
    
    if my_string.lowercased() == my_string {
        return my_string.uppercased()
    } else if my_string.uppercased() == my_string {
        return my_string.lowercased()
    }
    
    for m in my_string {
        var mm = String(m)
        if mm.lowercased() == mm {
            ans += mm.uppercased()
        } else {
            ans += mm.lowercased()
        }
    }
    
    return ans
}