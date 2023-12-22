func solution(_ n:Int, _ words:[String]) -> [Int] {
    // 1. 사전 작업
    // return 할 배열 answer = [0, 0]
    var answer = [0, 0]
    
    // 2. 반복하기 전
    // 반복되는 동안 마지막 글자를 저장하는 변수 lastChrOfBeforeWord: String = ""
    // 반복되는 동안 나왔던 단어를 저장하는 배열 existWords: [String]
    var lastChrOfBeforeWord = ""
    var existWords = [String]()
    
    // 3. 반복
    // words의 count 수만큼 반복
    for idx in 0..<words.count {
        let word = words[idx]
        // 1. 끝말잇기가 성립하는지 (lastChrofBeforeWord == word.startIndex ~ 인지)
        // 2. 중복된 단어가 아닌지 (word가 existWords에 없는 단어 인지)
        if (lastChrOfBeforeWord == "" || lastChrOfBeforeWord == word.prefix(1)) && !existWords.contains(word) {
            // 두 가지 조건문을 성공적으로 통과하면
            // lastChrOfBeforeWord를 갱신한다
            // existWords에 추가한다
            lastChrOfBeforeWord = String(word.suffix(1))
            existWords.append(word)
        } else {
            // 통과하지 못 하면
            // answer를 업데이트한 뒤에, return 한다
            // 현재 round를 구한다. i + 1일 것이다.
            let round = idx
            var mod = round / n + 1
            var remainder = round % n + 1
            // round / n의 몫과 나머지를 커스텀해서 구한다
            // (몫은 += 1, 나머지가 0인 경우에는 몫 그대로 || 나머지: n인 것으로)
            // 누구인지: 나머지
            // 그의 몇 번째 차례인지: 몫
            answer = [remainder, mod]
            return answer
        }
    }
    return answer
}