import Foundation

func solution(_ cipher:String, _ code:Int) -> String {
    
    var ans = ""
    
    for i in stride(from: code - 1, to: cipher.count, by: code){
        let idx = cipher.index(cipher.startIndex, offsetBy: i)
        ans += String(cipher[idx])
    }
    
    return ans
}