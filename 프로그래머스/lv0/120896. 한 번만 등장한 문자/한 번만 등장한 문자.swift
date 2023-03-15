import Foundation

func solution(_ s:String) -> String {
    
    // linear search chr in s
    // if count chr in s == 1 (with filter), add to ans String
    
    var ans = ""
    
    for chr in s {
        if s.filter{$0 == chr}.count == 1 {
            ans += String(chr)
        }
    }
    
    return String(ans.sorted())
}