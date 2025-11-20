import pymysql


def connectDB():
    
    global conn 
    conn = pymysql.connect(host='localhost', user='root', password='1234', database='ATM')
    return
    
def createAccount(pin,username):
    global conn
    query = 'INSERT INTO customerInfo (pin, username, balance) VALUES (%s, %s, %s)'
    values = (pin, username, 0)
    mycursor = conn.cursor()
    mycursor.execute(query, values)
    conn.commit()
    return
    
def login(pin , username):
    global conn
    try:
        query = f'select username from customerInfo where pin = {pin}'
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        if result== None:
            return 'no account with such pin'
        else:
            if result[0] == username:
                return True
            else:
                return False
    except Exception as e:
        return str(e)
    
    
def balance(pin):
    try:
        global result
        cursor = conn.cursor()
        query = f'select balance from customerInfo where pin = {pin}'
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]
    except Exception as e:
        return str(e)
    
def deposit(pin,amount):
    amount = amount+result[0]
    try:
        query = f'update customerInfo set balance={amount} where pin = {pin}'
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        return str(e)
    
def withdraw(pin,amount):
    amount = result[0] - amount
    try:
        query = f'update customerInfo set balance={amount} where pin = {pin}'
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        return str(e)
    
def change(pin,newUsername,newPIN):
    query = f"update customerInfo set username='{newUsername}', pin={newPIN} where pin = {pin}"
    try:
        
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print('inside except')
        return str(e)
    

# try:
#     connectDB()
#     print('database connnected')
# except Exception as e:
#     print(f'error\n{e}')
connectDB()
change(211160,'uzair008',3838)
