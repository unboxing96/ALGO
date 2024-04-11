# 이해
# 1. 해당 장르의 재생 수
# 2. 동일 장르 내 곡의 재생수
# 3. 고유번호가 낮은 것

# 풀이
# genre_count = { 장르: 총 재생 횟수 }
# genre_dic = { 장르: [고유번호, 재생 횟수] }
# genre_count -> 재생 횟수 -> 고유 번호 순서대로 정렬
# 각 장르마다 2개씩 끊어서 고유 번호 저장

def solution(genres, plays):
    answer = []
    
    genre_count = {}
    genre_dic = {}
    
    # 장르와 재생 횟수를 저장
    for i in range(len(genres)):
        if genres[i] in genre_count:
            genre_count[genres[i]] += plays[i]
        else:
            genre_count[genres[i]] = plays[i]
        
        genre_dic.setdefault(genres[i], []).append([i, plays[i]])
    
    # 장르를 재생 횟수에 따라 내림차순 정렬
    genre_count_sorted = sorted(genre_count.items(), key=lambda x: x[1], reverse=True)
    
    for genre, _ in genre_count_sorted:
        # 각 장르 내의 곡을 먼저 재생 횟수, 그 다음 고유 번호에 따라 정렬
        sorted_songs = sorted(genre_dic[genre], key=lambda x: (-x[1], x[0]))
        # 각 장르에서 상위 2곡의 고유 번호를 추출하여 추가
        answer.extend([song[0] for song in sorted_songs[:2]])
    
    return answer


