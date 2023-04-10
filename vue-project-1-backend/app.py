from flask import Flask,render_template,jsonify,request
from flaskext.mysql import MySQL
from flask_cors import CORS

mysql = MySQL()
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'db'

mysql.init_app(app)


# @app.route('/')
# def get_user():
#     cur = mysql.connect().cursor()
#     cur.execute('SELECT * FROM jobs')
#     get_users = cur.fetchall()
#     result_data = jsonify(get_users)
#     return result_data


@app.route('/',methods=['Post'])
def post_user():
    insert_value = (
        "INSERT INTO db.jobs(id,name,position) VALUES (%s,%s,%s)"
    )
    conn = mysql.connect()
    cur = conn.cursor()
    data = request.get_json()
    name = data['name']
    position = data['position']
    id = data['id']
    cur.execute(insert_value, (id,name,position))
    conn.commit()
    conn.close()
    cur.close()
    

if __name__ == '__main__':
    app.run(debug=True)
