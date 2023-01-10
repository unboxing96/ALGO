# LRU 알고리즘 구현 (stack)
# # if not ref in cache:
# # # if len(cache) < cacheSize: cache.append(ref)
# # # else (( miss )) : cache.pop(0)
# # #       cache.append(ref)
# # #       when miss, time += 5
# # else (( hit )) :
# # #     cache.pop(cache.index(ref)) # 캐시 안에 있으면 해당 위치에서 제거
# # #     cache.append(ref)
# # #     when hit, time += 1


def solution(cacheSize, cities):

    cache = []
    time = 0

    for ref in cities:
        ref = ref.lower()
        # 입력값이 캐시에 없으면
        if not ref in cache:

            if cacheSize == 0:
                return len(cities) * 5

            # 캐시가 비어있으면
            elif len(cache) < cacheSize:
                cache.append(ref)
                time += 5
            # 캐시가 꽉 차있으면
            else:  # miss
                cache.pop(0)
                cache.append(ref)
                time += 5
        # 입력값이 캐시에 있으면
        else:
            cache.pop(cache.index(ref))
            cache.append(ref)
            time += 1

    answer = time
    return answer


cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]

print(solution(cacheSize, cities))
