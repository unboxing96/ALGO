#1.
# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.


#code
# numbers = input().split()
# print(sum(numbers))

#error
# TypeError: unsupported operand type(s) for +: 'int' and 'str'



try:
    numbers = input().split()
    print(sum(numbers))

except TypeError as err:
    print(f"에러 메세지: {err}")
    
    numbers = map(int, numbers)
    print(sum(numbers))


