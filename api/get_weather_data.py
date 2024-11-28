from flask import Flask, jsonify
from flask_cors import CORS
from utils import get_latest_weather_data

app = Flask(__name__)
CORS(app)

def handler(request):
    """"""
    try:
        data = get_latest_weather_data()
        if data:
            return jsonify({
                "temperature": data[0],
                "humidity": data[1],
                "precipitation": data[2],
                "wind_speed": data[3]
            })
        else:
            return jsonify({"error": "No data found"}), 404
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500