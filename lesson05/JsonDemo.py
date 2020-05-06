import json

score = '{"國文":100, "數學":90}'
stu = '[{"name":"Elle", "age":18}, {"name":"Mary", "age":17}]'

obj = json.loads(score)   # 將 json 字串 轉成 json 物件
print(type(obj))
print(obj.get('國文'))

obj2 = json.loads(stu)
print(type(obj2))
for st in obj2:
    print(st.get('name'), st.get('age'))
