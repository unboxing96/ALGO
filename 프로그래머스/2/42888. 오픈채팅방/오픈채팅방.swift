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
    let actions = ["Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다."]
    var a = [String:String]()

    record.forEach {
    let separated = $0.components(separatedBy: " ")
    if separated.count > 2 {
        a[separated[1]] = separated[2]
    }
}

return record.filter { !$0.contains("Change") }.map { (value:String) -> String in
        let separated = value.components(separatedBy: " ")
        let newString = a[separated[1]]! + actions[separated[0]]!
        return newString
}
}