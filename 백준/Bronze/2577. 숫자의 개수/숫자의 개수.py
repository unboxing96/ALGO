li_st = []
for i in range(3):
    A = int(input())
    li_st.append(A)

sum = li_st[0] * li_st[1] * li_st[2]
sum_2 = str(sum)

for j in range(10):
    j = str(j)
    print(sum_2.count(j))