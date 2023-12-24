// 스택으로 푸는 문제
// 입력으로 "("이 들어온 경우 -> stack에 push()
// 입력으로 ")"이 들어온 경우 
    // (top이 "("이 아닌 경우 || stack이 비어있는 경우) -> return false
    // else -> pop()
// 끝까지 반복했으면 return true

import Foundation

struct Stack<T> {
    var elements: [T] = []
    var count: Int {
        return elements.count
    }
    var isEmpty: Bool {
        return elements.isEmpty
    }
    
    func top() -> T? {
        return elements.last
    }
    
    mutating func push(_ element: T) {
        elements.append(element)
    }
    
    mutating func pop() -> T? {
        return elements.popLast()
    }
}

func solution(_ s:String) -> Bool
{
    var ans: Bool = false
    var myStack = Stack<String>()
    
    for now in s {
        // 입력으로 "("이 들어온 경우 -> stack에 push()
        if now == "(" {
            myStack.push("(")
            
        // 입력으로 ")"이 들어온 경우
        } else {
            
            // stack이 비어있는 경우 -> return false
            if myStack.isEmpty {
                return false
            
            // else -> pop()
            } else {
                myStack.pop()
            }
        }
    }
    
    return myStack.isEmpty ? true : false
}