max = lambda x, y : x if x > y else y

print('max=', max(70, 20))



def check_score(score):
    return 'pass' if score >= 60 else 'fail'

print(check_score(max(70, 20)))


bmi = lambda h, w : w / (h / 100)**2
print('bmi=', bmi(170, 67))


myname = lambda : print("Feinasia")
myname()