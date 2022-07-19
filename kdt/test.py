age = int(input("당신의 나이를 입력해주세요: "))
birth = input("생일이 지났습니까? (Y/N): ")

if birth == "N":
	age -= 1

print(age)