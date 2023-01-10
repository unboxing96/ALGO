# records 해석하기
# records 반복하며
# time, car, IO = map(input().split())
# # time은 분으로 전환
# # h, m = time.split(":")
# # min_time = int(h) * 60 + int(m)
# if IO == "IN": dic[car] = min_time
# elif IO == "OUT": dic[car] -= min_time
# fees 계산하기
# if dic[car] <= fees[0]:
#   result.append(fees[1])
# else: # dic[car] > fees[0]:
#   result.append(fees[1] + math.ceil(max(0, (time - fees[0])) / fees[2]) * fees[3])
import math

# fees: [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
def get_fee(time, fees):
    return fees[1] + math.ceil(max(0, (time - fees[0])) / fees[2]) * fees[3]


def solution(fees, records):

    get_in = {}
    get_out = {}

    for r in records:
        time, car, IO = r.split()
        # time을 분으로 전환
        h, m = time.split(":")
        time = int(h) * 60 + int(m)

        if IO == "IN":
            get_in[car] = time
        if IO == "OUT":
            try:
                get_out[car] += time - get_in[car]
            except:
                get_out[car] = time - get_in[car]
            del get_in[car]

    for car, time in get_in.items():
        try:
            get_out[car] += 23 * 60 + 59 - time
        except:
            get_out[car] = 23 * 60 + 59 - time

    return [
        get_fee(time, fees)
        for car, time in sorted(list(get_out.items()), key=lambda x: x[0])
    ]


# 기본 시간 / 기본 가격 / 추가 단위 시간 / 추가 가격
fees = [180, 5000, 10, 600]

records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]


print(solution(fees, records))
