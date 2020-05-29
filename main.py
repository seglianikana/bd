import cx_Oracle

username = 'SYSTEM'
password = '8882'
database = 'localhost:1521/orcl'
print('connection start')
connection = cx_Oracle.connect(username, password, database)
cursor=connection.cursor()

print("Запит 1 - Вивести імена та загальну кількість народжених під цим ім'ям дітей\n")
query1 ="""
select NAME_BABY, sum(BABY_COUNT)
from NAMES_POPULARITY
inner join NAMES1 using(name_id) 
GROUP BY NAME_BABY
"""
cursor.execute(query1)

for row in cursor.fetchall():
    print(row[0], row[1])

print("Запит 2 - Відношення кількості народжених під певним ім'ям дітей до кількості народжених під іншими іменами у відсотках\n")
query2 ="""
select NAME_BABY,(SUM(BABY_COUNT)*100)/(select SUM(BABY_COUNT) from NAMES_POPULARITY)
from NAMES_POPULARITY
inner join NAMES1 using(name_id) 
GROUP BY NAME_BABY
"""
cursor.execute(query2)

for row in cursor.fetchall():
    print(row[0], row[1])

print("Запит 3 - Вивести динаміку загальної кількості імен в залежності від року\n")
query3 ="""
select BD_YEAR, SUM(BABY_COUNT)
from NAMES_POPULARITY
GROUP BY BD_YEAR

"""
cursor.execute(query3)

for row in cursor.fetchall():
    print(row[0], row[1])

cursor.close()
connection.close()