import sqlite3
#  user 1-----shaktish
# user 2----- shubham
# user 3------manish


conn=sqlite3.connect('travelling.db',timeout=100)
c=conn.cursor()
#c.execute('create table salesman(f_name text,lst_name text,u_name int,pass text)')

c.execute('insert into salesman values("aman","uchhalkud",5,"aman")')
#c.execute('drop table salesman') #****danger****
#c.execute('select * from salesman')

conn.commit()
c.close()
conn.close()
