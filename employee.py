import sqlite3
from prettytable import PrettyTable
data = sqlite3.connect("employee.db")
# table1 = data.execute("select name from sqlite3_master where type ='table' and name = 'details'").fetchall()
# if table1 !=[]:
#     print("Table already created")
# else:
data.execute('''create table details(
                            id integer primary key autoincrement,
                            empcode integer,
                            name text,
                            salary integer,
                            designation text); ''')
print("Table created")
while True:
    print("1.Add data")
    print("2.View all data")
    print("3.Exit")
    a = int(input("Enter the choice"))
    if a==1:
        getCode = input("Enter the employee code")
        getName = input("Enter the employee name")
        getSal = input("Enter teh salary")
        getDes = input("Enter their designation")
        data.execute("insert into details(empcode,name,salary,designation) values("+getCode+",'"+getName+"',"+getSal+",'"+getDes+"')")
        data.commit()
        print("Data added!!")
    elif a ==2:
        result = data.execute("select * from details")
        table = PrettyTable(["Id","Emp_code","Name","Salary","Designation"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(table)
    elif a==3:
        data.commit()
        break
    else:
        print("Invalid choice")