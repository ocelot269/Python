class User(object):

    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def setWithdraw(self, money_retired):
        if money_retired > self.balance:
            raise ValueError()
        self.balance -= money_retired
        return self.name + " has " + str(self.balance) + "."

    def setCheck(self, otherName, money):
        if not otherName.checking_account:
            raise ValueError()
        self.balance += money
        otherName.balance -= money
        return self.name + " has " + str(self.balance) + " and " + otherName.name + " has " + str(otherName.balance) + "."

    def setAdd_cash(self, money):
        self.balance += money
        return self.name + " has " + str(self.balance) + "."


Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)


if __name__ == '__main__':

    assert Jeff.setWithdraw(2) == 'Jeff has 68.'
    assert Joe.setCheck(Jeff, 50) == 'Joe has 120 and Jeff has 18.'
    assert Jeff.setCheck(Joe, 80) == 'Jeff has 98 and Joe has 40.'
    assert Jeff.setAdd_cash(20) == 'Jeff has 118.'
