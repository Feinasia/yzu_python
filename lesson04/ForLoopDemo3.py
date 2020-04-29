# 複合數組
e1 = {'name':'John', 'salary': 50000}
e2 = {'name':'Mary', 'salary': 60000}
e3 = {'name':'Bob', 'salary': 70000}
emps = [e1, e2, e3]
print(emps)
print(emps[0])
print(e1['salary'])
print(emps[0]['salary'])

#求薪資總和
sum=0
for emp in emps:
    sum =sum + emp['salary']
print(sum)

salary=[]
for emp in emps:
    salary.append(emp['salary']) # 將 salary 提出放入數組
print(salary)
print(max(salary)) #最大值
print(min(salary)) #最小值
