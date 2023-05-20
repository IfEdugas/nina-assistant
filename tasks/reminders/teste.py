import pymysql

db = pymysql.connect(host='ninadb-1.cwoklfo1flby.us-east-1.rds.amazonaws.com', user='ninaadmin505617', password='Phillipe505617')
cursor = db.cursor()

#print(cursor.execute("select version()"))

#sql = '''create database ninareminders'''
sql = '''use ninareminders'''

cursor.execute(sql)

sql2 = '''
create table reminder (
id int not null auto_increment,
data text,
task text,
dono text,
primary key (id)
)
'''

sql = '''show tables'''
print(cursor.execute(sql))
print(cursor.fetchall())
