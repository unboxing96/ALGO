# 문제 분석
# 장르(genres)별로 각 음악의 번호(인덱스)와 재생 횟수(plays)가 주어짐.
# 장르별로 재생 횟수가 높은 상위 2개까지 음악의 고유 번호(인덱스)를 배열에 추가한다.
    # 해당 장르에 음악이 1개면, 1개만 한다.
    # 재생 횟수가 동일하면, 음악의 고유 번호가 낮은 것을 먼저 수록한다.

# 접근
# genres / plays 배열을 탐색하여, genresRanking 딕셔너리에 값을 더한다.
    # 동시에 genresWithIndexAndPlayDict에 [[index, play]] 형태로 저장한다.
# genresRanking의 value의 내림차순으로 genre를 얻는다. -> sortedGenres
    # 해당 genre를 key로 gWIAPDict의 value를 얻는다.
    # 해당 value를 play인 x[1]을 내림차순, index인 x[0]을 오름차순으로 정렬한다. 
    # 정렬한 배열을 [:2]까지 index 만을 answer에 추가한다.
# answer를 return한다.
    
    
def solution(genres, plays):
    answer = []
    genresRanking = {}
    genresWithIndexAndPlayDict = {}
    
    for i in range(len(genres)):
        if genresRanking.get(genres[i], 0):
            genresRanking[genres[i]] += plays[i]
            genresWithIndexAndPlayDict[genres[i]].append([i, plays[i]])
        else:
            genresRanking[genres[i]] = plays[i]
            genresWithIndexAndPlayDict[genres[i]] = []
            genresWithIndexAndPlayDict[genres[i]].append([i, plays[i]])
    
    sortedGenres = [item[0] for item in sorted(genresRanking.items(), key=lambda x: -x[1])]
    print(genresRanking)
    print(genresWithIndexAndPlayDict)
    
    for genre in sortedGenres:
        dict = genresWithIndexAndPlayDict[genre]
        sortedDict = sorted(dict, key = lambda x : (-x[1], x[0]))
        answer.extend([item[0] for item in sortedDict][:2])

    return answer