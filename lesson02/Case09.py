# -*- coding:UTF-8 -*-

#BMI 資料運算
h = float(input('請輸入身高(cm):'))
w = float(input('請輸入體重(kg):'))
bmi = w / ((h/100)**2)
result = 18<= bmi < 24
print('身高: %.1f cm; 體重: %.1f Kg; BMI: %.2f; Result: %s' % (h, w, bmi, result))