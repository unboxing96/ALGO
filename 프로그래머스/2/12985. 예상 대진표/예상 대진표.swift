// 문제에서 주어진 대로 풀어보자
// a와 b가 승리 했을 때 각각 몇 번이 되는지 체크하자
// a == b가 되는 라운드를 출력하자

import Foundation

func solution(_ n:Int, _ a:Int, _ b:Int) -> Int
{
    var round = 0
    var aNum = a
    var bNum = b
    
    while true {
        aNum = (aNum / 2) + (aNum % 2)
        bNum = (bNum / 2) + (bNum % 2)
        round += 1
        if aNum == bNum {
            break
        }
    }

    return round
}