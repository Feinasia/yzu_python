# 利用 Lambda 製作出 switch  的運行邏輯

sex = 1
{
    1:lambda :print('男'),
    2:lambda :print('女')
}.get(sex, lambda : print('Error'))()

sex_info = {1:lambda x :print('M', x), 2: lambda x :print('W', x)}
sex_info.get(1)(20)