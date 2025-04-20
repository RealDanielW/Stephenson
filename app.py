from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)

@app.route('/')
def index():
    # Read the CSV data and prepare it for the dashboard view
    tank_data = get_tank_data()
    return render_template('index.html', tank_data=tank_data)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/get_tank_data')
def get_tank_data():
    try:
        with open("stTankData.csv", 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)  # Skip header
            tank_data = []
            for i, row in enumerate(csvreader, start=15):
                if i > 24:
                    break
                if row:
                    tank_data.append({
                        'id': i,
                        'temperature': row[1],
                        'weight': row[2],
                    })
            return jsonify(tank_data)
    except Exception as e:
        print(f"Error reading data: {e}")
        return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)
