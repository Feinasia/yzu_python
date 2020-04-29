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

# 是否補牌 (True, False)
def draw(PC):
    score = getscore(PC)
    if score >= 9: #不補
        return False
    if score <=6: #強迫補牌
        PC.append(poker.pop(0))
        return True
    if 6 < score < 8: #6.5,7,7.5
        count = poker.count('A') + poker.count(2) + poker.count(3) + poker.count('J')+poker.count('Q')+poker.count('K')
        if count > 12:
            PC.append(poker.pop(0))
            return True
        else:
            return False
    if 8 <= score < 9:  # 8, 8.5
        count = poker.count('A') + poker.count(2) + poker.count('J') + poker.count('Q') + poker.count('K')
        if count > 10:
            PC.append(poker.pop(0))
            return True
        else:
            return False

# 贏家判斷
def getwinner(user, pc):
    user_s=getscore(user)
    pc_s=getscore(PC)
    if user_s > 10.5 and pc_s > 10.5:
        return None
    elif user_s <= 10.5 and pc_s > 10.5:
        return "user"
    elif user_s > 10.5 and pc_s <= 10.5:
        return "PC"
    elif user_s < pc_s:
        return "PC"
    else:
        return "user"

#使用者先拿牌
user = []
user.append(poker.pop(0))
while True:
    print('user: ', user, getscore(user))
    flag = int(input('是否要牌? 0:不要, 1:要'))
    if flag == 0:
        break
    user.append(poker.pop(0))


PC = []
PC.append(poker.pop(0))
while True:
    if draw(PC):
        PC.append(poker.pop(0))
        continue
    break
print('PC: ', PC, getscore(PC))

# who wins?

print(getwinner(user, PC))
