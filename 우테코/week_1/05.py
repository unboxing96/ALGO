def wallet(money):

    paper = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
    paper_cnt = [0] * len(paper)

    tmp = 0
    while money > 0:

        money -= paper[tmp]

        if money > 0:
            paper_cnt[tmp] += 1

        elif money == 0:
            paper_cnt[tmp] += 1
            return paper_cnt

        else:
            money += paper[tmp]
            tmp += 1


money = 15000

result = wallet(money)
print(result)
