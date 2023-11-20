import sqlite3
from sqlite3 import Error


# monkey create table
con = sqlite3.connect("db_file.db")
print("database has been made.")

# monkey create variable for function cursor so monkey won't have to call out con.cursor() again and again
cur = con.cursor()


# monkey is making a function to establish a connection to the db_file.db to access data
def create_connection(database_file):
    '''
    CREATE A DATABASE CONNECTION TO THE SQLite DATABASE
    SPECIFIED BY database_file

    :param database_file:
    :return: Connection object or None

    '''


    connection = None
    try:
        connection = sqlite3.connect(database_file)
        print("Successfully connected to the database.")
        return connection
    except Error as object_error:
        print(object_error)

    return connection

# monkey does not know if connection is made so this code helps monkey
_connection = create_connection("db_file.db")


# monkey thinks that it will look like sht if everything is stored here so monkey
# created another file so that data can be inserted and this function will let monkey
# be able to access the db_file.db
def share_connectiion():
    return create_connection("db_file.db")


def create_table (connection, create_table_sql):
    '''
    CREATE A TABLE FORM THE  create_table_sql STATEMENT

    :param connection:
    :param create_table_sql:
    :return:
    '''

    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        print("Table has been created")
    except Error as object_error:
        print(object_error)



def tables():
    db_file_location = r"db_file.db"

    sql_create_project_table = '''
        CREATE TABLE IF NOT EXISTS projects (
            id integer PRIMARY KEY,
            name text NOT NULL,
            begin_date text,
            end_date text
            
            
        );
    
    '''

    sql_create_task_table ='''
       CREATE TABLE IF NOT EXISTS tasks (
            id integer PRIMARY KEY,
            name text NOT NULL,
            priority integer,
            project_id integer NOT NULL,
            status_id integer NOT NULL,
            begin_date text NOT NULL,
            end_date text NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects (id)
            
            
        );
    '''

    # monkey create connection to the create_connection function so that table can be made
    connection = create_connection(db_file_location)


    if connection is not  None:
        create_table(connection, sql_create_project_table)
        print("Table project has been made")

        create_table(connection, sql_create_task_table)
        print("Table tasks has been made")

    else:
        print("Table/s has yet been made")




if __name__ == '__main__':
    tables()



