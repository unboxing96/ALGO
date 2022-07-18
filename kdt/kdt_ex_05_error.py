# ex_05.
# 아래 코드는 숫자의 길이를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# code
# number = 22020718
# print(len(number))

try: 
    number = 22020718
    print(len(number))

except TypeError as err :
     print(f"에러 메시지: {err}")

     print(len(str(number)))