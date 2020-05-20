class Account:
    name= '' #公有變數
    __balance = 100  #私有變數 不公開

    def __init__(self, name, money):
        self.name = name
        self.__balance = self.__balance + money

    def addBalance(self, money): #self 指物件自己
        self.__balance = self.__balance + money

    def __str__(self):
        return self.name + ' has $' + str(self.__balance)

if __name__ == '__main__':
    Account.bank = 'CTB' # 靜態/類別變數

    acc = Account('CJ', 200)  # 加上 上面 __init__ 可取代下面3行
    #acc=Account()
    #acc.name = 'CJ'
    #acc.addBalance(200)
    print(Account.bank, acc)

    acc2 = Account('Mary', 500)
    #acc2=Account()
    #acc2.name = 'Mary'
    #acc2.addBalance(500)
    print(Account.bank, acc2)