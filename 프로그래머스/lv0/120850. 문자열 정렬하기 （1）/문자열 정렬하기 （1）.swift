import Foundation

func solution(_ my_string:String) -> [Int] {
    
    var ans = [Int]()
    
    for m in my_string {
        if let x = Int(String(m)) {
            ans.append(x)
        }
    }
    
    return ans.sorted()
}