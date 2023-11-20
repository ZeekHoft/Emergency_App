import sqlite3
from db_tables_connections import share_connectiion

# monkey set parameter values for the target table and the list of data to be added
# table_name is either the project or task and the data list is the key value pairs
def insert_data_into_table(table_name, data_list):
    connection = share_connectiion()

    if connection is not  None:
        try:
            cursor = connection.cursor()

            for data in data_list:
                # monkey thinks that name will always be the first one to be checked, if so, if the name
                # is the same the data won't be added twice

                unique_key = 'name' # this can be modified if names are similar but other data's is not... but not now too lazy
                unique_value = data.get(unique_key)

                cursor.execute(f'SELECT * FROM {table_name} WHERE {unique_key} = ?', (unique_value,))
                existing_data = cursor.fetchone()

                if existing_data is None:
                    # Data does not exist, so proceed with the insertion
                    # monkey got lost here but is okay because everything work monkey happy.
                    columns = ', '.join(data.keys())
                    placeholders = ', '.join(['?' for _ in data.values()])
                    query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
                    cursor.execute(query, tuple(data.values()))
                else:
                    print(
                        f"Data with {unique_key}={unique_value} already exists in the {table_name} table. Skipping insertion.")

            connection.commit()
            print("All data has been added")

        except Exception as Object_error:
            print(Object_error)
        finally:
            connection.commit()


if __name__ == '__main__':
    # monkey found efficient way to insert data into table

    project_data_to_insert = [
        {"name": "Project Alphot", "begin_date": "2023-01-01", "end_date": "2023-12-31"},
        {"name": "Project Beta", "begin_date": "2023-02-01", "end_date": "2023-12-31"},
        # Add more projects as needed
    ]

    task_data_to_insert = [
        {"name": "Task 1", "priority": 1, "project_id": 1, "status_id": 1, "begin_date": "2023-01-01", "end_date": "2023-01-31"},
        {"name": "Task 2", "priority": 2, "project_id": 1, "status_id": 1, "begin_date": "2023-02-01", "end_date": "2023-02-28"},
        # Add more tasks as needed
    ]

    # monkey is making a connection to the parameters by calling out the function and the table name
    insert_data_into_table('projects', project_data_to_insert)
    insert_data_into_table('tasks', task_data_to_insert)

