
import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='frog',
    database='sql_basics_september2026'
)
cursor=conn.cursor()
#sql="create table employee(id int primary key,name varchar(20),salary int,dept varchar(20))"
#sql="insert into employee values(1,'arun',25000,'dev')"
#sql="insert into employee values(2,'arjun',30000,'dev')"
#sql="insert into employee values(3,'aravind',35000,'HR')"
#sql="insert into employee values(4,'arjun',40000,'HR')"
#sql="insert into employee values(5,'arun',45000,'finance')"
#sql="insert into employee values(6,'arjun',50000,'it')"

sql="select * from employee"
cursor.execute(sql)

#row=cursor.fetchall()
#for i in row:
    #print(i[0],i[1],i[2],i[3])

#row=cursor.fetchmany(1)
#print(row)

row=cursor.fetchone()
print(row)
conn.commit()
conn.close()

