import re

data = input()

zero = re.compile("0+")
one = re.compile("1+")

zero_list = zero.findall(data)
one_list = one.findall(data)

print(min(len(zero_list), len(one_list)))
