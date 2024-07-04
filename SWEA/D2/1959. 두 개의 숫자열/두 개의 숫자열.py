# 문제 분석
# 두 배열의 길이를 비교한다.
# 짧은 것은 shortArr, 긴 것을 longArr, 두 배열 길이의 차이를 lengthDiff라고 하자
# lengthDiff만큼 반복한다. i
	# shortArr의 길이만큼 반복한다. j
    	# tempSum += shortArr[j] * longArr[j + i]
    # sum = max(sum, tempSum)
# 형식에 맞춰 출력한다.

testCase = int(input())

for tc in range(testCase):
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    result = 0

    lengthDiff = abs(n - m)
    shortArr = arr1 if n < m else arr2
    longArr = arr1 if n >= m else arr2

    for i in range(lengthDiff + 1):
        tempSum = 0
        for j in range(len(shortArr)):
            tempSum += shortArr[j] * longArr[j + i]

        result = max(result, tempSum)
    print(f"#{tc + 1} {result}")