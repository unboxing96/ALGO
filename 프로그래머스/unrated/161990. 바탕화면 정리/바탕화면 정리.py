def solution(wallpaper):

    idx_list = []

    for i in range(len(wallpaper)): # 세로 길이, x
        for j in range(len(wallpaper[0])): # 가로 길이, y
            
            # 파일("#")을 발견하면, index를 저장
            if wallpaper[i][j] == "#":
                idx_list.append((i, j))

    min_x = sorted(idx_list, key = lambda x : x[0])[0][0]
    min_y = sorted(idx_list, key = lambda x : x[1])[0][1]
    max_x = sorted(idx_list, key = lambda x : -x[0])[0][0]
    max_y = sorted(idx_list, key = lambda x : -x[1])[0][1]

    return [min_x, min_y, max_x + 1, max_y + 1]