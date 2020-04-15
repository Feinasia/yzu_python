# -*- coding:UTF-8 -*-
score = 75
print("score", score)  #字串以 空格 分開 (預設)
print("score", score, sep="=") #字串以 = 分開
print("score", score, sep=",") #字串以  分開
print("score", score, sep="&") #字串以 & 分開

print("a") # 結束以 \n (換行)(預設)
print("b")
print("a", end="")  # 結束以 空集合 接著印出下一行
print("b")

print("A", end="")
print("B", end="")
print("C", end="\n")

print("a", "b", sep=",",end="#")  # 結束以 # 接著印出下一行
print("c","d", sep=",")
