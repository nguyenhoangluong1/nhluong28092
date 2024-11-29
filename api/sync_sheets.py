from utils.weather_sync import sync_weather_data
from flask import jsonify

def handler(request):
    try: 
        data = sync_weather_data()
        if data:
            return jsonify(data)
        else:
            return jsonify({"error": "No data found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
