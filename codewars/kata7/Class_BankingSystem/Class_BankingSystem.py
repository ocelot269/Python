class User(object):

    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, money_retired):
        if money_retired > self.balance:
            raise ValueError()
        self.balance -= money_retired
        return self.name + " has " + str(self.balance) + "."


Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)


if __name__ == '__main__':

    assert Jeff.withdraw(2) == 'Jeff has 68.'
#assert Joe.check(Jeff, 50) == 'Joe has 120 and Jeff has 18.'
#assert Jeff.check(Joe, 80) == 'Jeff has 98 and Joe has 40.'
#assert Jeff.add_cash(20) == 'Jeff has 118.'
