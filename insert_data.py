import sqlite3
from sqlite3 import Error
database=""
conn = None
#def create_connection(db_file):

#database = "g:\pythonaugust22\trail_prog/sqlitedatabase/pythonsqlite.db"
conn=sqlite3.connect("g:/pythonaugust22/trail_prog/sqlitedatabase/pythonsqlite.db")
ac = conn.cursor()
print("connected successfully")
sql = """ insert into projects(id, name, begin_date, end_date) values(2, "Cool App with SQLite & Python","2015-01-01", "2015-01-30")"""

ac.execute(sql)
conn.commit()
print("values inserted successfully",ac.rowcount)







def create_task(conn, task):
    sql='''
    insert into tasks(name, priority,status_id, project_id, begin_date,end_date)values(?,?,?,?,?,?)'''
    ac = conn.cursor()
    ac.execute(sql,task)
    ac.commit()
    return ac.lastrowid
'''
def main1():
    with conn:
        project = ()
        project_id=create_project(conn, project)
'''



      #  task_1=('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
       # task_2=('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')


       # create_task(conn, task_1)
      #  create_task(conn, task_2)

#if __name__ == '__main__':
 #   main1()
