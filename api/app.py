from flask import Flask, request, jsonify
import pandas as pd 
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/app/api": {"origins": "http://127.0.0.1:5500"}})


# Define an endpoint
@app.route('/app/api', methods=['GET'])
def get_data():
    # Sample data to return
    df = pd.read_excel('D:/js-project/project-j/api/temp.xlsx')
    print(df)
    data = {"temperatures": "36°C", "humidity": "36%", "precipitation": "36mm", "wind_speed": "36km/h"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
