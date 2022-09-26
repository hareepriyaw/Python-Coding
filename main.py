import sqlite3
from sqlite3 import Error
from connect_db import conn


def create_table(conn, create_table_sql):
    try:
        c=conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print("not connected")
    c.close()
def main():
    database = r" g:/pythonaugust22/trail_prog/sqlitedatabase/pythonsqlite.db"

    sql_create_projects_table = """create table  projects(
        id integer primary key,
        name text not null,
        begin_date text,
        end_date text);"""

    sql_create_tasks_table = """create table tasks(
        id integer primary key,
        name text not null,
        priority integer,
        project_id integer not null,
        status_id integer not null,
        begin_date text not null,
        end_date text not null,
        foreign key (project_id) references projects (id));"""

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tasks_table)

    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()




