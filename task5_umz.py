# mohammadreza mohammadi


import sqlite3

conn = sqlite3.connect('Expenses.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Expenses
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              date TEXT,
              category TEXT,
              cost REAL,
              description TEXT)''')

conn.commit()
conn.close()



def add_cost():

    with sqlite3.connect('Expenses.db') as conn:
        cur = conn.cursor()

        date = input('Enter date: ')
        category = input('Enter category: ')
        amount = float(input('Enter amount: '))
        description = input('Enter description: ')

        cur.execute('INSERT INTO Expenses(date,category,cost,description) VALUES (?,?,?,?)', (date, category, amount, description))

        conn.commit()


def view():
    try:
        with sqlite3.connect('Expenses.db') as conn:
            cur = conn.cursor()
            cur.execute('SELECT * from Expenses')
            rows = cur.fetchall()
            for row in rows:
                print(f'date:{row[1]} .... category:{row[2]}  ....  cost:{row[3]}  ....  description:{row[4]}')
    except sqlite3.Error as e:
        print(e)


def update():
    with sqlite3.connect('Expenses.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * from Expenses')
        rows = cur.fetchall()
        for row in rows:
            print(f'id:{row[0]}  ....  date:{row[1]} .... category:{row[2]}  ....  cost:{row[3]}  ....  description:{row[4]}')
        print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
        id = input('enter the id of cost that you want to change: ')

        date = input('Enter new date: ')
        category = input('Enter new category: ')
        amount = float(input('Enter new amount: '))
        description = input('Enter new description: ')        

        cur.execute('UPDATE Expenses SET date= ? , category=? , cost=? , description=?  WHERE id= ? ' , (date,category,amount,description,id))
        conn.commit


def remove():
    with sqlite3.connect('Expenses.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * from Expenses')
        rows = cur.fetchall()
        for row in rows:
            print(f'id:{row[0]}  ....  date:{row[1]} .... category:{row[2]}  ....  cost:{row[3]}  ....  description:{row[4]}')
        print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
        id = input('enter the id of cost that you want to remove: ')
        cur.execute("DELETE FROM Expenses WHERE id = ?", (id,))
        conn.commit


while True :
    n = input ("""
    1.add cost
    2.view cost
    3.update cost
    4.remove cost
    5.quit

     """)
    if n == "1":
        print("\n===============\n")
        add_cost()
        print("\n===============\n")
    if n == "2":
        print("\n===============\n")
        view()
        print("\n===============\n")
    if n == "3":
        print("\n===============\n")
        update()
        print("\n===============\n")
    if n == "4":
        print("\n===============\n")
        remove()
        print("\n===============\n")
    if n == "5":
        break



