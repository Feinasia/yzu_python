class Human:
    name = ''
    sex = ''
    age = 0

    def __str__(self):  # 後面只需要 print(h)
        return self.name + ", " + self.sex + ", " + str(self.age)


class Student(Human):  # 繼承 from Human 並在另加
    number = 0
    grade = ''

    def __str__(self):
        return self.name + ", " + self.sex + ", " + str(self.age) + ', ' + str(self.number) + ', ' + self.grade
#print(__name__)  # __main__   內建 keyname

if __name__ == "__main__":   # 用於表示 在此PY執行才會執行，從其他呼叫 class 就不會執行以下
    h = Human()
    h.name = 'CJ'
    h.sex = "F"
    h.age = 18
    print(h.name, h.sex, h.age)
    print(h)

    s = Student()
    s.name ='John'
    s.sex = 'M'
    s.age = 14
    s.number = 900180
    s.grade = '七年級'
    print (s)