'''
自動補牌機制
<=6點 強迫補牌
>=9點 不需補牌
7 or 7.5 看 A, 2, 3, J, Q, K 剩餘>=12 才補
8 or 8.5 看 A, 2, J, Q, K 剩餘>=10 才補
'''
import random as r
poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4
#洗牌
r.shuffle(poker)
#計分公式
def getscore(po):
    sum = 0
    for p in po:
        if p == "A":
            sum = sum + 1
            continue
        if p == "J" or p == "Q" or p == "K":
            sum = sum + 0.5
            continue
        sum = sum + p
    return sum

PC = []
PC.append(poker.pop(0))
# 補排程序
while True:
    score = getscore(PC)
    if score >= 9: #不補
        break
    if score <=6: #強迫補牌
        PC.append(poker.pop(0))
        continue
    if 6 < score < 8: #6.5,7,7.5
        count = poker.count('A')+poker.count(2)+poker.count(3)+poker.count('J')+poker.count('Q')+poker.count('K')
        if count >=12:
            PC.append(poker.pop(0))
            continue
        else:
            break
    if 8 <= score < 9:  # 8, 8.5
        count = poker.count('A') + poker.count(2) + poker.count('J') + poker.count('Q') + poker.count('K')
        if count >= 10:
            PC.append(poker.pop(0))
            continue
        else:
            break
print(PC, getscore(PC))