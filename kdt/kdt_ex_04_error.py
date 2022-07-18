# 04
# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# code
# words = list(map(int, input().split()))
# print(words)



try :
    words = list(map(int, input().split()))
    print(words)

except ValueError as err :
    print(f"에러 메세지: {err}")

    words = input("다시 한 번 입력해 주세요: ").split()
    print(words)

