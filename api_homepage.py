from flask import  Flask, render_template
import sqlite3

app = Flask(__name__, template_folder=r'C:\Users\DLTPO\PycharmProjects\pythonProject1\emergency_app\database_emer_file\emer_app_api_temp')


@app.route('/')
def home():
    make_connection = sqlite3.connect("db_file.db")
    cursor = make_connection.cursor()


    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()

    make_connection.close()

    make_connection.close()
    return render_template("homepage.html", tasks=tasks, projects=projects)



if __name__ == '__main__':
    app.run(debug=True)
