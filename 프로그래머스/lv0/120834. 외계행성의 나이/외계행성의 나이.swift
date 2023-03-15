import Foundation

func solution(_ age:Int) -> String {
    
    var dic = [Int : Character]()
    
    for i in 97..<107 {
        if let asc = UnicodeScalar(i) {
            dic[i - 97] = Character(asc)
        }
    }
    
    var ans = ""
    
    for a in String(age) {
        if let x = Int(String(a)) {
            ans += String(dic[x]!)
        }
    }

    
    return ans
}