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
