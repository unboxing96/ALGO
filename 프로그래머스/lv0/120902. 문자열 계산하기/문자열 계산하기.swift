func solution(_ my_string: String) -> Int {
    let components = my_string.components(separatedBy: " ")
    var result = Int(components[0])!
    
    for i in stride(from: 1, to: components.count, by: 2) {
        let operatorString = components[i]
        let operand = Int(components[i+1])!
        
        switch operatorString {
        case "+":
            result += operand
        case "-":
            result -= operand
        default:
            break
        }
    }
    
    return result
}
