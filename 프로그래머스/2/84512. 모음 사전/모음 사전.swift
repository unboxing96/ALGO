// 이해
// 1글자부터 5글자까지 모든 조합을 만든다.
    // 5P1, 5P2, 5P3, 5P4, 5P5 모두 구해서 차례대로 추가한다. # 연산 회수는 20,000 미만
    // 아니었다. 중복으로 구해야한다.
    // 중복 조합으로 모든 경우의 수를 구한 뒤에, 정렬한다.
// 주어진 단어가 몇 번째인지 return한다.

// 의사코드
// word_array = []
// for i in 1...5 {}
    // word_array.append(contentsOf: permutation(word, i))
// return Int(word_array.firstIndex(where: {$0 == word}))!

import Foundation

func solution(_ word: String) -> Int {
    var wordArray = [String]()
    for i in 1...5 {
        wordArray.append(contentsOf: permutation("AEIOU", i))
    }
    
    wordArray.sort()
    
    if let index = wordArray.firstIndex(where: {$0 == word}) {
        return index + 1
    }
    return 0
}

func permutation(_ str: String, _ n: Int) -> [String] {
    var result = [String]()
    if str.count < n { return result }
    
    let characters = Array(str)
    
    func cycle(_ now: String) {
        if now.count == n {
            result.append(now)
            return
        }
        
        for i in 0..<characters.count {
            cycle(now + String(characters[i]))
        }
    }
    
    cycle("")
    
    return result
}