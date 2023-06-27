def solution(cards1, cards2, goal):
    idx1 = 0  # cards1의 현재 index
    idx2 = 0  # cards2의 현재 index
    for word in goal:
        # 카드 뭉치에서 다음 카드를 사용할 수 있는지 확인
        can_use1 = idx1 < len(cards1) and cards1[idx1] == word
        can_use2 = idx2 < len(cards2) and cards2[idx2] == word

        # 두 카드 뭉치에서 모두 사용할 수 없는 경우, "No"를 return
        if not can_use1 and not can_use2:
            return "No"
        
        # 둘 중 하나만 사용할 수 있는 경우, 해당 카드 뭉치에서 카드를 사용
        elif can_use1 and not can_use2:
            idx1 += 1
        elif can_use2 and not can_use1:
            idx2 += 1
        # 두 카드 뭉치에서 모두 사용할 수 있는 경우, 첫 번째 카드 뭉치에서 카드를 사용
        else:
            idx1 += 1
    
    return "Yes"
