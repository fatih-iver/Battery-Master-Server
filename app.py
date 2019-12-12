from flask import Flask, request, jsonify
import sqlite3

# command: flask run --host=0.0.0.0

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn

app = Flask(__name__)

@app.route('/')
def root():
    return 'Battery!'

@app.route('/battery', methods = ['GET', 'POST'])
def battery():
    if request.method == 'GET':
        rows = []
        conn = create_connection('battery.db')
        if conn:
            cur = conn.cursor()
            sql = '''SELECT * FROM BATTERY'''
            cur.execute(sql)
            rows = cur.fetchall()
        print(rows)
        return jsonify({"rows": rows})
    elif request.method == "POST":
        print("POST")
        keys = ["charge_status", "charge_level", "current", "remaining_cap", "voltage", "health_level", "current_av", "battery_power", "cell_temp"]
        params = []
        for key in keys:
            if key in request.form:
                params.append(request.form[key])
        params = tuple(params)
        print(params)

        conn = create_connection("battery.db")
        print(conn)
        if conn:
            sql = ''' INSERT INTO BATTERY (charge_status,charge_level,current,remaining_cap,voltage,health_level,current_av,battery_power,cell_temp) VALUES(?,?,?,?,?,?,?,?,?) '''
            cur = conn.cursor()
            print(sql)
            cur.execute(sql, params)
            conn.commit()
            print(cur.lastrowid)
        return "POST BATTERY"
    else:
        return "[METHOD] BATTERY"

if __name__ == '__main__':
    app.run()
