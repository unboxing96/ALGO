// record의 문장은 순서대로 출력 되어야 한다
// "명령어 + id"까지만 저장하면 된다. 닉네임은 가변적이이니까. Change 문장은 저장하지 않는다.
// 딕셔너리를 만들어서 id : 닉네임으로 관리하고, 저장된 명령어를 순서대로 출력하되, 닉네임은 딕셔너리에서 값을 가져오면 될 듯하다.

// 의사 코드
// 반복문으로 record 배열을 탐색한다
// whitespace를 기준으로 명령어 + id + 닉네임으로 분리한다
// switch로 케이스를 나눠, 
    // "Enter", "Leave" 문장은 
        // "명령어 + id" 형태로 Stack에 순서대로 저장한다.
        // 새로운 id가 들어오면, 딕셔너리에 추가해준다. (딕셔너리에 추가 혹은 수정은 모두 O(1)이기 때문에 케이스를 나눌 필요 없을 듯)
    // "Change" 문장은 딕셔너리를 수정해준다.
// 반복문이 종료되면 Stack에 저장된 문장을, 딕셔너리를 참조해서 순서대로 출력한다.


import Foundation

func solution(_ record:[String]) -> [String] {
    
    var result = [String]()
    var sentenceStack = [[String]]()
    var nicknameDict = [String : String]()
    
    // 반복문으로 record 배열을 탐색한다
    for nowSentence in record {
        
        // 문장을 구성하는 변수를 미리 선언한다
        var order: String = ""
        var id: String = ""
        var nickname: String?
        
        // whitespace를 기준으로 명령어 + id + 닉네임으로 분리한다
        let components = nowSentence.split(separator: " ").map { String($0) }
        
        order = components[0]
        id = components[1]
        if components.count == 3 {
            nickname = components[2]
        }
        
        // switch로 케이스를 나눠,
        switch order {
            // "Enter", "Leave" 문장은
                // "명령어 + id" 형태로 Stack에 순서대로 저장한다.
                // 새로운 id가 들어오면, 딕셔너리에 추가해준다. (추가 혹은 수정은 모두 O(1)이기 때문에 케이스를 나눌 필요 없을 듯)
            case "Enter":
                sentenceStack.append([order, id])
                if let nickname = nickname {
                    nicknameDict.updateValue(nickname, forKey: id)
                }
            case "Leave":
                sentenceStack.append([order, id])
            // "Change" 문장은 딕셔너리를 수정해준다.
            case "Change":
                if let nickname = nickname {
                    nicknameDict.updateValue(nickname, forKey: id)
                }
            default:
                print("default")
        }
    }
    
    // 반복문이 종료되면 Stack에 저장된 문장을, 딕셔너리를 참조해서 순서대로 출력한다.
    for sentence in sentenceStack {
        let sentenceOrder = sentence[0]
        let sentenceId = sentence[1]
        result.append("\(nicknameDict[sentenceId, default: "non-nickname"])님이 \(sentenceOrder == "Enter" ? "들어왔습니다" : "나갔습니다").")
    }
    
    return result
}
