import pymysql


try:
    dbcon = pymysql.connect(host='localhost', user='root', password='',database='studinfo')
    cr = dbcon.cursor()
    print("Database Connected !")
except Exception as e :
    print(e)


def create_table():
    tbl_create = "create table studinfo(id integer primary key auto_increment,name text,sub text)"

    try:
        cr.execute(tbl_create)
        print("Table Created !")
    except Exception as e:
        print(e)

def insert_data():
    a = int(input("Enter to how many student you want to store info:- "))

    for m in range(a):
        nm = input("Enter Your Name: ")
        sub = input("Enter Your Subject: ")
        ins_data = f"INSERT INTO studinfo (name,sub) VALUES ('{nm}', '{sub}')"
        try:
            cr.execute(ins_data)
            dbcon.commit()
            print("Data Insert succesfuly..")
        except Exception as e:
            print(e)


def update_data():
    stud_id = input("Enter the student id to upadet: ")
    new_nm = input("Enter the new name: ")
    new_sub = input("Enter the new subject: ")

    update_data = f"UPDATE studinfo SET name = '{new_nm}' , sub = '{new_sub}'  WHERE id = '{stud_id}'"

    try:
        cr.execute(update_data)
        dbcon.commit()
        print("Data Updated Successfully!")
    except Exception as e:
        print(e)

def delete_data():
    delete_id = input("Enter the id of the student to delete: ")

    delete_data = f"DELETE FROM studinfo WHERE id = '{delete_id}'"

    try:
        cr.execute(delete_data)
        dbcon.commit()
        print("Data Deleted Successfully!")
    except Exception as e:
        print(e)

def show_data():
    show_data = "SELECT * FROM studinfo"
    try:
        cr.execute(show_data)
        s = cr.fetchall()
        
        print("============Student Information==============")
        print("ID Name  Subject")
        for a in s:
            print(f"{a[0]} {a[1]} {a[2]}")
            
    except Exception as e:
        print(e)


while True:
    print("\n===================Options===================")
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Show Data")
    print("5. Exit")
    print("=============================================")
    print("===============Enter your choice=============")
    choice = input("==> ")
    if choice == '1':
        insert_data()
    elif choice == '2':
        update_data()
    elif choice == '3':
        delete_data()
    elif choice == '4':
        show_data()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
    





