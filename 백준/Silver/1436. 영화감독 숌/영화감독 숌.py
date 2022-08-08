N = int(input())

devil_num = 0
cnt = 0 # N번째

while True:
    # devil_num에 666이 있으면 카운트
    if '666' in str(devil_num):
        cnt += 1

    # N번째 devil_num을 찾았으면 출력
    if cnt == N:
        print(devil_num)
        break

    devil_num += 1
