from tkinter import *;

class ATM:
    def __init__(self):
        self.accountsInfo = {}
        self.balance = 0
        self.menu()
    def authentication(self):
        i=3
        
        self.id = input('enter your username\n')
        self.pin = input('enter four digit pin\n')
        flag = 0
        while(i>=0):
            
            if self.id in self.accountsInfo.keys() and self.pin ==self.accountsInfo[self.id]:
                print('Success...!\n')
                flag = 1
                break
            elif self.id in self.accountsInfo.keys() and self.pin !=self.accountsInfo[self.id]:
                print(f'You have entered wrong pin\nre-enter the pin\n{i} try/tries left\n')
                pin = input()
                if i ==1 and self.pin !=self.accountsInfo[self.id]:
                    print('You have entered wrong pin four times\n...EXITING...')
                    self.exit()
                    break
            elif self.id not in self.accountsInfo.keys():
                print(f'You have entered wrong username\nre-enter the username\n{i} try/tries left\n')
                self.id = input()
                if i ==1 and self.id not in self.accountsInfo.keys():
                    print('You have entered wrong username four times\n...EXITING...')
                    self.exit()
                    break
            else:
                print(f'Invalid entries\n{i} try/tries left\n')
                self.id = input('Enter the username\n')
                self.pin = input('Enter the pin\n')
                if i ==1 and id not in self.accountsInfo.keys():
                    print('You have entered wrong information four times\n...EXITING...')
                    self.exit()
                    break
            i-=1

        if flag ==1:
            return 1
        else:
            return 0
            
    def optSelection(self):
        opt = int(input('''
        Choose an Option From Following
        1.Goto Menu
        2.Goto Login
        3.Make Deposite
        4.Balance Inquiry
        5.Withraw Money
        6.Change Pin
        or press any other button to Exit
        '''))
        if opt == 1:
            self.menu()
        elif opt == 2:
            self.login()
        elif opt == 3:
            self.deposit()
        elif opt == 4:
            self.balanceInquiry()
        elif opt == 5:
            self.withdraw()
        elif opt == 6:
            self.changePin()
        else:
            self.exit()


    def menu(self):
        print('...MENU...\n')
        userInput =int(input( '''
        choose from following options
        1.Create new Account
        2.Login To Existing Account
        3.Exit
        '''))
        if userInput ==1:
            self.createAccount()
        elif userInput ==2:
            if len(self.accountsInfo)==0:
                print('No account exists\nDo you want to create a new account\npress 1 to create account and 2 to exit the system\n')
                opt = int(input())
                if opt ==1:
                    self.createAccount()
                else:
                    self.exit()
            else:
                self.login()
        else:
            self.exit()
    def createAccount(self):
        print('...NEW ACCOUNT...\n')
        self.username = input('Enter a username\n')
        self.pin = input('enter a four digit pin\n')
        while True:
            if len(self.pin)==4:
                #print('Pin created successfully\n')
                break
            else:
                if len(self.pin)>4:
                    print('length of pin exceeded\nre-enter a four digit pin\n')
                    self.pin = input()
                else:
                    print('length of pin is less than 4\nre-enter a four digit pin\n')
                    self.pin = input()
        self.accountsInfo[self.username] = self.pin 
        print('Congrats! Account Created Sucessfully\n')
        opt = int(input('''
        choose option among following
        1.Goto Login
        2.Goto Menu\n'''))
        while True:
            if opt ==1:
                self.login()
                break
            elif opt == 2:    
                self.menu()
                break
            else:
                print('Wrong Input\nSelect from given options\nre-enter your choice\n1.Goto Login\n2.Goto Menu\n')
                opt = int(input())
    def login(self):
        print('...LOGIN...\n')
        flag = self.authentication()
        if flag ==1:
           self.optSelection()
        else:
            pass
   
    def changePin(self):
        print('...CHANGE PIN...\n')
        print('Enter your old username and pin\nEnter the new pin after successful authentication\n')
        flag = self.authentication()
        if flag == 1:
            pin = input('Enter a new 4 digit pin\n')
            while True:
                if len(pin)==4:
                    print('Pin changed successfully\n')
                    break
                else:
                    if len(pin)>4:
                        print('length of pin exceeded\nre-enter a four digit pin\n')
                        pin = input()
                    else:
                        print('length of pin is less than 4\nre-enter a four digit pin\n')
                        pin = input()
            self.accountsInfo[self.id] = pin
        self.optSelection()
    def balanceInquiry(self):
        print('...BALANCE INQUIRY...\n')
        flag = self.authentication()
        if flag==1:
            print(f'Your current balance is {self.balance}\n')
            self.optSelection()
        else:
            self.exit()
        
    def deposit(self):
        print('...DEPOSITE SECTION...\n')
        flag = self.authentication()
        if flag == 1:
            amount = int(input(f'Your current balance is {self.balance}\nEnter the amount you want to deposit\n'))
            self.balance+=amount
            print(f'Deposite successful\nNew balance is {self.balance}\n')
            self.optSelection()
        else:
            pass
    def withdraw(self):
        print('...WITHDRAW MONEY...\n')
        flag = self.authentication()
        if flag ==1:
            amount = int(input('Enter the amount you want to withdraw\n'))
            while True:
                if amount<self.balance:
                    self.balance-=amount
                    print(f'Withdrawl successful...\nAmount withdrawn:\n{amount}\nRemaining Balance:\n{self.balance}')
                    break
                else:
                    print(f'Insufficient Balance\nYour current balance is {self.balance}\nYour amount must be less than this balance\nEnter the amount again or press 0 to exit system\n')
                    amount = int(input())
                    if amount == 0:
                        self.exit()
                        break
                    else:
                        pass
            self.optSelection()
        else:
            pass

    
    def exit(self):
        print('Program Exited')
        

if __name__ == "__main__":
    atm1 = ATM()


