def solution(babbling):
    answer = 0
    
    word_dict = {
        "aya" : "1",
        "ye" : "2",
        "woo" : "3",
        "ma" : "4"
    }
    
    result = []
    
    for bab in babbling:
        for wd in word_dict:
            if wd in bab:
                bab = bab.replace(wd, word_dict[wd])
        
        result.append(bab)

    for bab in result:
        if bab.isdigit():
            for i in range(len(bab) - 1):
                if bab[i + 1] == bab[i]:
                    break
            else:
                answer += 1
    
    return answer