# 랜덤 3자리 설정
# 재시작(1) / 종료(2) 처리
# while로 "랜덤 3자리" 맞출 때까지 반복

from random import sample

# 랜덤 3자리 숫자 생성
def ran_num():
    while True:
        num = sample(range(100, 1000), 1)[0]

        if len(str(num)) == len(set(str(num))):
            return num


isBool = True

def baseball():
    global isBool

    if isBool:
        print("숫자 야구 게임을 시작합니다.")
    
    your_num = ran_num()

    while True:
        
        try:
            my_num = int(input("숫자를 입력해주세요 : "))
            if len(set(str(my_num))) != 3:
                raise ValueError
        except ValueError:
            print("서로 다른 3자리 숫자를 입력하세요.")
            return True
            
        strike = 0
        ball = len(set(str(your_num)) & set(str(my_num)))

        if ball:
            for i in range(3):
                if str(your_num)[i] == str(my_num)[i]:
                    ball -= 1
                    strike += 1
            else:
                if strike == 3:
                    print(f"{strike}스트라이크")
                    print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
                    print("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")
                    new = int(input())
                    if new == 1:
                        isBool = False
                        baseball()
                    else:
                        return True

                elif strike == 2:
                    print(f"{ball}볼 {strike}스트라이크")
                elif strike == 1:
                    print(f"{ball}볼 {strike}스트라이크")
                else: # strike == 0
                    print(f"{ball}볼")
        else:
            print("낫싱")


baseball()