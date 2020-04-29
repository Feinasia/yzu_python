import operator
import random as r
poker1 = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
poker2 = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
print(operator.eq(poker1, poker2))

poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4  # *4 重複4次
print(poker)
print(len(poker))
print(poker.count("A"))

#抽一張牌
card = poker.pop(0)  # pop抽出並從原字串中刪除 0:
print('抽一張牌:', card)
print(poker)
#洗牌
r.shuffle(poker)
print(poker)

#計算前三張的點數 A=1, 2=2, ... J,Q,K=0.5
print(poker[0:3])  #前3位,  指 index = 0,1,2  不含3
def score(po):  #假設 po = [A,9 ,J]
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

print('前三張', poker[0:3], '總合為', score(poker[0:3]))

# 元素是否存在於數組中
print('A' in poker)
print('B' in poker)