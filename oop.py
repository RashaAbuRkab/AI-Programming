
class Account:
    def __init__(self, id='', holderName='', type=''):
        self.id = id
        self.holderName = holderName
        self.type = type
        self.credit = 0
        self.dept = 0
        self.balance = self.credit - self.dept

    def deposit(self, amount):
        self.credit = self.credit + amount

    def withdrawal(self, amount):
        self.dept = self.dept + amount

    def updateBalace(self):
        self.balance = self.balance + (self.credit - self.dept)

    def displayAccount(self):
        self.updateBalace()
        print(f"The Account Number is {self.id}")
        print(f"The Account Holder Name is {self.holderName}")
        print(f"The Account Balance is {self.balance}")
        print("-----------------------------------------------\n")


class AllAccounts(Account):
    def __init__(self):
        self.allAccountsDict = {}

    def createAccount(self, id='', holderName='', type=''):
        if id in self.allAccountsDict.keys():
            print("Account Already Exist ")
        else:
            self.allAccountsDict[id] = Account(id=id, holderName=holderName,
                                               type=type)

    def displayAccount(self, id):
        if id not in self.allAccountsDict.keys():
            print("Account dose not Exist ")
        else:
            self.allAccountsDict[id].displayAccount()

    def displayAllAccount(self):
        for key, val in self.allAccountsDict.items():
            val.displayAccount()

    def transfer(self, fromID, toID, ammount):
        a=0
        if fromID not in self.allAccountsDict.keys() \
                and toID not in self.allAccountsDict.keys():
            print('One of the Accounts dose note Exist ')
        else:
            if self.allAccountsDict[fromID].balance > ammount:

                self.allAccountsDict[fromID].withdrawal(ammount)
                self.allAccountsDict[toID].deposit(ammount)

            else:
                print("insufficient funds")
    def savetofile(self,path):
        pass


def main():
    allAccounts = AllAccounts()

    allAccounts.createAccount(id='001', holderName='Rasha',
                              type='Saving')
    allAccounts.allAccountsDict['001'].deposit(5000)
    allAccounts.allAccountsDict['001'].deposit(500)
    allAccounts.allAccountsDict['001'].withdrawal(1000)

    allAccounts.createAccount(id='002', holderName='ali',
                              type='Saving')
    allAccounts.allAccountsDict['002'].deposit(1000)
    allAccounts.allAccountsDict['002'].deposit(1000)
    allAccounts.allAccountsDict['002'].withdrawal(2000)
    allAccounts.displayAccount('002')

    allAccounts.displayAllAccount()

    allAccounts.transfer('001', '002', 2000)
    allAccounts.displayAllAccount()


if __name__ == "__main__":
    main()