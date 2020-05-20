#多重繼承

class Engine:
    power = 0

class Wheel:
    count = 0

class Car(Engine, Wheel):
    def __init__(self, price, power, count):
         self.price = price  #可以突然加入分類
         self.power = power
         self.count = count
    def __str__(self):
         return 'Price is ' + str(self.price) + ', and Power is ' + str(self.power) + ', but Wheel has only ' +str(self.count) + ', '

if __name__ == '__main__':
     car = Car(100000, 150, 4)
     print(car)
