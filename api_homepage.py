from flask import  Flask, render_template
import sqlite3
from waitress import serve
from paste.translogger import TransLogger
import logging
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)


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
  serve(TransLogger(app, setup_console_handler=False), host='127.0.0.1', port=8080)
