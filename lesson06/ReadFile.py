file = open('Salary.txt', 'r', encoding='UTF-8')
rows = file.readlines()
print(rows)  # ['John, 50000\n', 'Mary, 53000\n', 'Tom, 56000'] 字串資料

#求總薪資
salaries = []
for r in rows:
    row = r.split(', ')
    print(row)
    dict = {'name':row[0], 'salary':row[1].strip('\n')}
    salaries.append(dict)

print(salaries)

sum = 0
for sal in salaries:
    sum = sum + int(sal['salary'])
print(sum)