import re


def solution(files):

    temp = [re.split(r"([0-9]+)", f) for f in files]
    temp2 = [re.findall(r"([a-zA-z]+).*([0-9]+).*", f) for f in files]

    print("temp", temp)
    print("============")
    print("temp2", temp2)

    sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))

    return ["".join(s) for s in sort]


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

print(solution(files))
