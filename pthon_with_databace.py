# TRY BLACK
try:
# import sql database package
    import sqlite3
    from tabulate import tabulate

    """ 
    __init__ function used to create table
     __init__ function is a general function
    """


    class Database:

        def __init__(self, db):
            self.con = sqlite3.connect(db)
            self.c = self.con.cursor()
            self.c.execute("""
                CREATE TABLE IF NOT EXISTS datas(
                    pid INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    gender TEXT NOT NULL,
                    address TEXT NOT NULL,
                    contact TEXT NOT NULL,
                    mail TEXT NOT NULL
                    )
                    """)
            self.con.commit()

# Insert data function

        def insert(self, name, age, gender, address, contact, mail):
            sql = """
                    INSERT INTO datas VALUES(NULL,?,?,?,?,?,?)
                """
            self.c.execute(sql, (name, age, gender, address, contact, mail))
            self.con.commit()
            print("")
            print("Insert sucssfully")

# Show all data, Function

        def fetch_record(self):
            self.c.execute("SELECT * FROM datas")
            data = self.c.fetchall()
            print(tabulate(data,headers=["ID","NAME","AGE","GENDER","ADDRESS","CONTACT","MAIL"]))

# Update record

        def update_record(self, pid):
            msg1 = ("""
                1.Name
                2.age
                3.Gender
                4.Address
                5.contact
                6.mail
            """)
            print(msg1)
            ch1 = int(input("Enter a choice : "))

# NAME UPDATE
            if ch1 == 1:
                sql = """
                        UPDATE datas set name=? where pid=?
                    """
                name1 = input("Enter a Name : ")
                self.c.execute(sql, (name1, pid))
                self.con.commit()
                print("")
                print("Name update sucssfully")
                print("")
                print("Show all datas")
                print("")
                self.c.execute("SELECT * FROM datas")
                data = self.c.fetchall()
                print(tabulate(data, headers=["ID", "NAME", "AGE", "GENDER", "ADDRESS", "CONTACT", "MAIL"]))


# AGE UPDATE
            elif ch1 == 2:
                sql = """
                        UPDATE datas set age=? where pid=?
                     """
                age1 = int(input("Enter a Age : "))
                self.c.execute(sql, (age1, pid))
                self.con.commit()
                print("")
                print("Age update sucssfully")
                print("")
                print("Show all datas")
                print("")
                self.c.execute("SELECT * FROM datas")
                datas = self.c.fetchall()
                print(tabulate(datas, headers=["ID", "NAME", "AGE", "GENDER", "ADDRESS", "CONTACT", "MAIL"]))

# GENDER UPDATE
            elif ch1 == 3:
                sql = """
                        UPDATE datas set gender=? where pid=?
                     """
                gender1 = input("Enter a Gender : ")
                self.c.execute(sql, (gender1, pid))
                self.con.commit()
                print("")
                print("Gender update sucssfully")
                print("")
                print("Show all datas")
                print("")
                self.c.execute("SELECT * FROM datas")
                data = self.c.fetchall()
                print(tabulate(data, headers=["ID", "NAME", "AGE", "GENDER", "ADDRESS", "CONTACT", "MAIL"]))

# ADDRESS UPDATE
            elif ch1 == 4:
                sql = """
                        UPDATE datas set address=? where pid=?
                     """
                address1 = input("Enter a address : ")
                self.c.execute(sql, (address1, pid))
                self.con.commit()
                print("")
                print("Address update sucssfully")
                print("")
                print("Show all datas")
                print("")
                self.c.execute("SELECT * FROM datas")
                data = self.c.fetchall()
                print(tabulate(data, headers=["ID", "NAME", "AGE", "GENDER", "ADDRESS", "CONTACT", "MAIL"]))

# CONTACT UPDATE
            elif ch1 == 5:
                sql = """
                        UPDATE datas set contact=? where pid=?
                     """
                contact1 = input("Enter a contact : ")
                self.c.execute(sql, (contact1, pid))
                self.con.commit()
                print("")
                print("Contact update sucssfully")
                print("")
                print("Show all datas")
                print("")
                self.c.execute("SELECT * FROM datas")
                data = self.c.fetchall()
                print(tabulate(data, headers=["ID", "NAME", "AGE", "GENDER", "ADDRESS", "CONTACT", "MAIL"]))

# MAIL UPDATE
            elif ch1 == 6:
                sql = """
                        UPDATE datas set mail=? where pid=?
                     """
                mail1 = input("Enter a mail : ")
                self.c.execute(sql, (mail1, pid))
                self.con.commit()
                print("")
                print("Mail update sucssfully")
                print("")
                print("Show all datas")
                print("")
                self.c.execute("SELECT * FROM datas")
                data = self.c.fetchall()
                print(tabulate(data, headers=["ID", "NAME", "AGE", "GENDER", "ADDRESS", "CONTACT", "MAIL"]))

# ANY NUMBER PRESS ACTION
            else:
                print("Sorry your select not found !")

# ID REMOVE FUNCTION
        def remove_record(self, pid):
            sql = "DELETE FROM datas WHERE pid=?"
            self.c.execute(sql, (pid,))
            self.con.commit()

    """
        CLASS OBJECT AND DATABASE CREATE FILE
    """
    obj = Database('registration.db')

# ERROR CATION BLACK
except Exception as e:
    print("Error :",e)

"""----------------------------------------------------------------------------------- """
try:
# POP MESSAGE AND WHILE TIME PROGRAM RUNNING
    ch = 1
    while ch == 1:
        msg = ("""
                1.Insert data
                2.show all data
                3.Update data
                4.Delete data
                5 (or) any key press to exact
            """)
        print(msg)

        c = int(input("Enter a choice : "))
        """
            INPUT OF FUNCTION RUNNING
            EXAMPLE : 
                    PRESS 1 TO INSERT FUNCTION RUNNING
                    PRESS 2, SHOW ALL DATA FUNCTION RUNNING
                    PRESS 3, UPDATE FUNCTION RUNNING  
                    PRESS 4, DELETE FUNCTION RUNNING
                    PRESS 5 OR ANY NUMBER (OR) ANY KEY ELSE STATEMENT RUNNING
        """

    # INPUTS OF INSERT DATA
        if c == 1:
            print("Insert users")
            name = input("Enter a Name : ")
            age = int(input("Enter a Age : "))
            gender = input("Enter a Gender : ")
            address = input("Enter a Address : ")
            contact = input("Enter a Mobile No : ")
            mail = input("Enter a Mail : ")
            obj.insert(name, age, gender, address, contact, mail)

    # SHOW ALL DELAIS
        elif c == 2:
            print("Show all datals")
            obj.fetch_record()

    # INPUT OF UPDATE ID
        elif c == 3:
            print("")
            obj.fetch_record()
            print("")
            pid = int(input("Enter a Updated id Number : "))
            obj.update_record(pid)

    # INPUT OF DELETE ID
        elif c == 4:
            print("")
            obj.fetch_record()
            print("")
            pid = int(input("Enter a deleted id Number : "))
            print("Delete success fully")
            obj.remove_record(pid)

    # QUIT PROGRAM STATEMENT
        else:
            print("")
            print("Thank you !")
            quit()
except Exception as e:
    print("Error :", e)