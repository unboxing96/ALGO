import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    
    var res = ""
    
    for m in my_string {
        res += String(repeating: m, count: n)
    }
    
    return res
}