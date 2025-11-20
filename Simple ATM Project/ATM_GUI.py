from tkinter import *;
import pymysql
from tkinter import ttk
import ttkthemes
from tkinter import messagebox
import database
from database import change



#root = Tk()
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1080x800+10+10')
root.title('Welcome To ATM')

# rootbg = PhotoImage(file='rootbg.png')
# lblRootbg = Label(root,image = rootbg)
# lblRootbg.place(x=0,y=0)

# adding a title label
lblTitle = Label(root,text='Simple ATM System',font=('Bahnschrift',18,'italic','bold'),bg='slate gray',fg='yellow')
lblTitle.place(x=380,y=20)


# making function for buttons

    # function for creating account
def createAccount():
    
    def createAccountSubmit():
        pin = pinEntry.get()
        username = usernameEntry.get()
        
        
        database.createAccount(pin,username)
        messagebox.showinfo('Success!','Account created.')
        newAccountWindow.destroy()
        
        
    
    try:
        database.connectDB()
    except Exception as e:
        messagebox.showerror('Error',f'{e}')
    newAccountWindow = Toplevel()
    newAccountWindow.geometry('400x400+400+200')
    newAccountWindow.title('Create New Account')
    
    usernameLbl = Label(newAccountWindow,text='Username : ',font=('arial',12,'italic','bold'))
    usernameLbl.grid(row=0,column=0, pady = 10)
    usernameEntry = Entry(newAccountWindow,font=('arial',12,'italic','bold'),bd=3)
    usernameEntry.grid(row=0,column=1, padx = 10, pady=10 )
    
    pinLbl = Label(newAccountWindow,text='PIN : ',font=('arial',12,'italic','bold'))
    pinLbl.grid(row=1,column=0, pady=10)
    pinEntry = Entry(newAccountWindow,font=('arial',12,'italic','bold'),bd=3)
    pinEntry.grid(row=1,column=1,padx = 10, pady = 10)
    
    submitNewAcc = Button(newAccountWindow,text = 'SUBMIT',cursor='hand2',command=createAccountSubmit)
    submitNewAcc.grid(row=2,column=0,columnspan=2,pady=10)
    
    
        
    # function for login
def login():
    def loginSubmit():
        global pin, username
        pin = pinEntry.get()
        username = usernameEntry.get()
        res = database.login(pin,username)
        if res == True:
            messagebox.showinfo('Success','Login successful')
            balanceBtn.config(state=NORMAL)
            withdrawBtn.config(state=NORMAL)
            depositBtn.config(state=NORMAL)
            changeBtn.config(state=NORMAL)
            logoutBtn.config(state=NORMAL)
            loginBtn.config(state='disable')
        elif res == False:
            messagebox.showerror('Error','Wrong Username')
        elif res == 'no account with such pin':
            messagebox.showerror('Error',f'{res}')
        else:
            messagebox.showerror('Error',f'Query not executed\n{res}')
        loginWindow.destroy()
    
    loginWindow = Toplevel()
    loginWindow.geometry('400x400+400+200')
    loginWindow.title('Login')
    
    usernamelbl = Label(loginWindow,text = 'Username : ',font=('arial',12,'italic','bold'))
    usernamelbl.grid(row=0,column=0,pady=10)
    usernameEntry = Entry(loginWindow,font=('arial',12,'italic','bold'),bd=3)
    usernameEntry.grid(row=0,column=1,padx=10,pady=10)
    
    pinlbl = Label(loginWindow,text = 'PIN : ',font=('arial',12,'italic','bold'))
    pinlbl.grid(row=1,column=0,pady=10)
    pinEntry = Entry(loginWindow,font=('arial',12,'italic','bold'),bd=3)
    pinEntry.grid(row=1,column=1,padx=10,pady=10)
    
    submitLogin = ttk.Button(loginWindow,text = 'Login',cursor='hand2',command=loginSubmit)
    submitLogin.grid(row=2,column=0,columnspan=2,pady=10)
    

def showBalance():
    bal = database.balance(pin)
    messagebox.showinfo('Balance',f'your balance is {bal}')
    
def deposit():
    
    def depositSubmit():
        amount = int(amountEntry.get())
        depositToplevel.destroy()
        global pin , username
        res = database.deposit(pin, amount)
        if res == None:
            messagebox.showinfo('Success','Deposit Successful')
        else:
            messagebox.showerror('Error',f'{res}')

    depositToplevel = Toplevel(root)
    depositToplevel.geometry('370x80+400+400')
    depositToplevel.title('Deposit Window')
    
    amountLbl = Label(depositToplevel, text = 'Amount : ')
    amountLbl.grid(row=0, column=0)
    amountEntry = Entry(depositToplevel)
    amountEntry.grid(row=0, column=1, padx=10)
    
    submitDeposit = ttk.Button(depositToplevel,text='Submit',command=depositSubmit)
    submitDeposit.grid(row= 1, column=0, pady=10 ,columnspan=2)
def withdraw():
    def withdrawSubmit():
        amount = int(amountEntry.get())
        withdrawToplevel.destroy()
        global pin 
        res = database.withdraw(pin, amount)
        if res == None:
            messagebox.showinfo('Success','Withdraw Successful')
        else:
            messagebox.showerror('Error',f'{res}')

    withdrawToplevel = Toplevel(root)
    withdrawToplevel.geometry('370x80+400+400')
    withdrawToplevel.title('Withdraw Window')
    
    amountLbl = Label(withdrawToplevel, text = 'Amount : ')
    amountLbl.grid(row=0, column=0)
    amountEntry = Entry(withdrawToplevel)
    amountEntry.grid(row=0, column=1, padx=10)
    
    submitWithdraw = ttk.Button(withdrawToplevel,text='Submit',command=withdrawSubmit)
    submitWithdraw.grid(row= 1, column=0, pady=10 ,columnspan=2)

def changeCredentials():
    messagebox.showinfo('Message','Enter Username and PIN\nIf you dont want to change the Username or PIN\nEnter old Username or PIN')
    def changeCredentialsSubmit():
        global pin
        newUsername = newUsernameEntry.get()
        newpin = int(newPINEntry.get())
        res = change(pin,newUsername,newpin)
        if res == None:
            messagebox.showinfo('Success','Credentials Changed')
        else:
            messagebox.showerror('Error',f'{res}')
        changeCredentialsToplevel.destroy()
    
    changeCredentialsToplevel = Toplevel(root)
    changeCredentialsToplevel.geometry('400x110+400+400')
    changeCredentialsToplevel.title('Change Credentils')
    
    newUsernameLbl = Label(changeCredentialsToplevel, text = 'New Username : ')
    newUsernameLbl.grid(row=0, column=0)
    newUsernameEntry = Entry(changeCredentialsToplevel)
    newUsernameEntry.grid(row=0, column=1, padx=10)
    
    newPINLbl = Label(changeCredentialsToplevel, text = 'New PIN : ')
    newPINLbl.grid(row=1, column=0)
    newPINEntry = Entry(changeCredentialsToplevel)
    newPINEntry.grid(row=1, column=1, padx=10)
    
    submitChangeCredentials = ttk.Button(changeCredentialsToplevel,text='Submit',command=changeCredentialsSubmit)
    submitChangeCredentials.grid(row= 2, column=0, pady=10 ,columnspan=2)

def logout():
    global pin, username
    messagebox.showinfo('Success','Logged Out successfully')
    print(f'pin is {pin} and username is {username}')
    pin = None
    username = None
    balanceBtn.config(state='disable')
    withdrawBtn.config(state='disable')
    depositBtn.config(state='disable')
    changeBtn.config(state='disable')
    logoutBtn.config(state='disable')
    loginBtn.config(state=NORMAL)


def exit():
    messagebox.showinfo('EXITED','Thanks For Using Our Services!')
    root.destroy()
    

    
#making left frame
leftFrame = Frame(root)
leftFrame.place(x=0,y=80,height=500,width=300)

# making options buttons
createAccountBtn = ttk.Button(leftFrame,text='Create New Account',cursor='hand2',command=createAccount)
createAccountBtn.grid(row=0,column=0,pady=20)

loginBtn = ttk.Button(leftFrame,text='Login',cursor='hand2',command=login)
loginBtn.grid(row=1,column=0,pady=10)


balanceBtn = ttk.Button(leftFrame,text='SHOW BALANCE',cursor='hand2',state='disable',command=showBalance)
balanceBtn.grid(row=2, column=0,pady=10)

depositBtn = ttk.Button(leftFrame,text='DEPOSIT',cursor='hand2',state='disable',command=deposit)
depositBtn.grid(row=3, column=0,pady=10)

withdrawBtn = ttk.Button(leftFrame,text='WITHDRAW',cursor='hand2',state='disable',command=withdraw)
withdrawBtn.grid(row=4, column=0,pady=10)

changeBtn = ttk.Button(leftFrame,text='CHANGE LOGIN CREDENTIALS',cursor='hand2',state='disable',command=changeCredentials)
changeBtn.grid(row=5, column=0,pady=10)

logoutBtn = ttk.Button(leftFrame,text='LOGOUT',cursor='hand2',state='disable',command=logout)
logoutBtn.grid(row=6, column=0,pady=10)

exitBtn = ttk.Button(leftFrame,text='Exit',cursor='hand2',command=exit)
exitBtn.grid(row=7,column=0,pady=10)
    



root.mainloop()
