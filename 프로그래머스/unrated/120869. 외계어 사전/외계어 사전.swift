// spell에 담긴 알파벳을 모두 한 번씩만 사용한 단어가 있는지 (순서는 상관X)
// set<spell> == set<dic의 각 원소>

import Foundation

func solution(_ spell:[String], _ dic:[String]) -> Int {
    
    let setSpell = Set(spell.joined())
    
    for elem in dic {
        let setDic = Set(elem)
        if setDic == setSpell {
            return 1
        }
    }
    return 2
}