# 곡괭이로 광물을 캐는 피로도
exhaustion_level = [[1,1,1],[5,1,1],[25,5,1]]
# 광물을 캐는 피로도를 표현하는 딕셔너리
mineral_mapping = {"diamond": 0, "iron": 1, "stone": 2}
# 최대 피로도 설정
min_exhaustion = float('inf')

# 광물 채굴 함수
def mine(idx, dia, iron, stone, minerals, exhaustion):
    # 모든 광물을 채굴하거나 모든 곡괭이를 사용한 경우
    if idx >= len(minerals) or (not dia and not iron and not stone):
        global min_exhaustion
        # 최소 피로도를 계산
        min_exhaustion = min(min_exhaustion, exhaustion)
        return
    
    diamond_exhaustion = iron_exhaustion = stone_exhaustion = 0
    # 다음 5개의 광물에 대한 피로도를 계산
    for i in range(idx, min(idx+5, len(minerals))):
        diamond_exhaustion += exhaustion_level[0][mineral_mapping[minerals[i]]]
        iron_exhaustion += exhaustion_level[1][mineral_mapping[minerals[i]]]
        stone_exhaustion += exhaustion_level[2][mineral_mapping[minerals[i]]]
 
    # 다이아몬드 곡괭이를 사용하는 경우
    if dia:
        mine(idx+5, dia-1, iron, stone, minerals, exhaustion+diamond_exhaustion)
    # 철 곡괭이를 사용하는 경우
    if iron:
        mine(idx+5, dia, iron-1, stone, minerals, exhaustion+iron_exhaustion)
    # 돌 곡괭이를 사용하는 경우
    if stone:
        mine(idx+5, dia, iron, stone-1, minerals, exhaustion+stone_exhaustion)

# 문제 해결 함수
def solution(picks, minerals):
    global min_exhaustion
    # 광물 채굴 시작
    mine(0, picks[0], picks[1], picks[2], minerals, 0)
    return min_exhaustion
