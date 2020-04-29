e1 = {'name': 'John', 'salary': 50000, 'program': ['java', 'python']}
e2 = {'name': 'Mary', 'salary': 60000, 'program': ['VB', 'python']}
e3 = {'name': 'Bob', 'salary': 70000, 'program': ['C#']}
emps = [e1, e2, e3]

#求會 python 的人名

names = []
lan = 'python'
for emp in emps:
    for p in emp['program']:
        if p == lan:
            names.append(emp['name'])
print(names)


