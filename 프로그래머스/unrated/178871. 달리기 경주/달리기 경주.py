def solution(players, callings):
    player_dic = {p : i for i , p in enumerate(players)}
    idx_dic = {i : p for i , p in enumerate(players)}

    
    for call in callings:
        now = player_dic[call]
        front_idx = now - 1
        
        now_player = call
        front_player = idx_dic[front_idx]
        
        player_dic[now_player], player_dic[front_player] = front_idx, now
        idx_dic[now], idx_dic[front_idx] = front_player, now_player
        
    return list(idx_dic.values())