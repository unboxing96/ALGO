import Foundation

func solution(_ rsp:String) -> String {
    
    var ans = ""
    
    for r in rsp {
        if r == "2" {
            ans += "0"
        } else if r == "0" {
            ans += "5"
        } else if r == "5" {
            ans += "2"
        }
    }
    
    return ans
}