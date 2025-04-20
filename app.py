import csv
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Read the data from the CSV file
    tank_data = read_tank_data()
    return render_template("index.html", tank_data=tank_data)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/get_tank_data')
def get_tank_data():
    tank_data = read_tank_data()
    return jsonify(tank_data)

def read_tank_data():
    tank_data = []
    try:
        with open("stTankData.csv", 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)  # Skip header
            for i, row in enumerate(csvreader, start=15):
                if i > 24:
                    break
                if row:
                    tank_data.append({
                        "id": i,
                        "temperature": f"{row[1]}°C",
                        "weight": f"{row[2]}Te"
                    })
    except Exception as e:
        print("Error reading data:", e)
    return tank_data

if __name__ == '__main__':
    app.run(debug=True)
