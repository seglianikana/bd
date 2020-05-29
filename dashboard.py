import chart_studio
import plotly.graph_objects as go
chart_studio.tools.set_credentials_file(username='seglianikana', api_key='cAx3oj5rc0rOxhvyCNxc')
import chart_studio.plotly as py
import cx_Oracle
username = 'system'
password = '8882'
database = 'localhost:1521/xe'
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

x1=[]
y1=[]
for row in cursor.fetchall():
    x1.append(row[0])
    y1.append(row[1])
    print(row[0], row[1])
fig = go.Figure([go.Bar(x=x1, y=y1)])
py.plot(fig, auto_open=True, filename='nastya1')

print("Запит 2 - Відношення кількості народжених під певним ім'ям дітей до кількості народжених під іншими іменами у відсотках\n")
query2 ="""
select NAME_BABY,(SUM(BABY_COUNT)*100)/(select SUM(BABY_COUNT) from NAMES_POPULARITY)
from NAMES_POPULARITY
inner join NAMES1 using(name_id) 
GROUP BY NAME_BABY
"""
cursor.execute(query2)

x2=[]
y2=[]
for row in cursor.fetchall():
    x2.append(row[0])
    y2.append(row[1])
    print(row[0], row[1])

fig2 = go.Figure(data=[go.Pie(labels=x2,
                              values=y2)])
py.plot(fig2, auto_open=True, filename='nastya2')

print("Запит 3 - Вивести динаміку загальної кількості імен в залежності від року\n")
query3 ="""
select BD_YEAR, SUM(BABY_COUNT)
from NAMES_POPULARITY
GROUP BY BD_YEAR
"""
cursor.execute(query3)

x3=[]
y3=[]
for row in cursor:
    x3.append(row[0])
    y3.append(row[1])
    print(row[0], row[1])

fig3= go.Figure(data=go.Scatter(x=x3, y=y3, mode='lines+markers'))
py.plot(fig3, auto_open=True, filename='nastya3')


cursor.close()
connection.close()