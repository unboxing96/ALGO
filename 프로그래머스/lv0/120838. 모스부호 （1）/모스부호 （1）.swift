import Foundation

let morse = [".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z"]

func solution(_ letter:String) -> String {
    
    let subString = letter.split(separator: " ")
    var ans = ""
    
    for s in subString {
        ans += morse[String(s)]!
    }
    
    return ans
}