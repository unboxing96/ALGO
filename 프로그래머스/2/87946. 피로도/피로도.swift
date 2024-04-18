// 이해
// 유저의 현재 피로도: k
// 2차원 배열이 주어지고, 배열의 원소는 [최소 필요 피로도, 소모되는 피로도]로 구성
// 원소를 하나 통과할 때마다 "소모되는 피로도"만큼 감소, result += 1
// k < "최소 필요 피로도"인 경우 반복을 종료하고 result를 return
// 순서대로 탐색하는 것이 아닌, 최선의 결과를 만드는 순서로 탐색해야 함.
// 최대 8개 던전의 선택하는 순열의 개수는 8P8 ~= 40,000
// 각 순열을 선형 탐색해야 한다. 순열의 최대 길이는 8이므로, 시간 복잡도는 대략 320,000.

// 의사코드
// let candidateArray = permutation(dungeons, len(dungeons))
// for candidate in candidateArray {}
    // var life = k
    // var tmpResult = 0
    // for element in candidate {}
        // if life >= element[0] {}
            // life -= element[1]
            // tmpResult += 1
        // else { break }
    // result = max(result, tmpResult)
// return result
        
import Foundation

func solution(_ k:Int, _ dungeons:[[Int]]) -> Int {
    
    let candidateArray = permutation(dungeons, dungeons.count)
    var result = 0
    
    for candidate in candidateArray {
        var life = k
        var tmpResult = 0
        for element in candidate {
            if life >= element[0] {
                life -= element[1]
                tmpResult += 1
            } else {
                break
            }
            
        result = max(result, tmpResult)
            
        }
    }
    
    return result
}

func permutation<T>(_ array: [T], _ n: Int) -> [[T]] {
    var result = [[T]]()
    if array.count < n { return result }
    
    var visited = Array(repeating: false, count: array.count)
    
    func cycle(_ now: [T]) {
        if now.count == n {
            result.append(now)
            return
        }
        
        for i in 0..<array.count {
            if visited[i] {
                continue
            } else {
                visited[i] = true
                cycle(now + [array[i]])
                visited[i] = false
            }
        }
    }
    
    cycle([])
    
    return result
}





