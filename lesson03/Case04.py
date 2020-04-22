def foo():
    pass

def bar(n):
    if n < 60:
        return  #在末端可以不寫  但在中間會中斷函式的進行
    print("恭喜過關")


foo()
bar(80)