import os
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from .database import insert_data, init_database

# Chạy hàm này để load các biến môi trường từ file .env
load_dotenv()

def sync_weather_data():
    """Đồng bộ dữ liệu thời tiết từ Google Sheets"""
    init_database()

    # Lấy thông tin từ file .env
    CREDENTIALS_JSON = os.getenv("SERVICE_ACCOUNT_FILE=")
    SPREADSHEET_ID = os.getenv("GOOGLE_SHEET_ID")

    if not CREDENTIALS_JSON or not SPREADSHEET_ID:
        raise ValueError("Missing environment variables")
    
    # Lưu trữ thông tin xác thực vào 1 tệp tạm thời
    with open('/tmp/credentials.json', 'w') as f:
        f.write(CREDENTIALS_JSON)

    # Xác thực và khởi tạo API client
    try:
        credentials = Credentials.from_authorized_user_file('/tmp/credentials.json')
        service = build('sheets', 'v4', credentials=credentials)
        

        # Lấy dữ liệu từ Google Sheets
        RANGE_NAME = os.getenv("GOOGLE_SHEETS_RANGE", "Sheet1!C3:F3")

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        values = result.get('values', [])

        if values and len(values[0]) == 4:
            # Chuyển dữ liệu từ Google Sheets sang kiểu số
            temperature = int(values[0][0])
            humidity = int(values[0][1])
            precipitation = float(values[0][2])
            wind_speed = float(values[0][3])

            # Chèn dữ liệu vào cơ sở dữ liệu
            insert_data(temperature, humidity, precipitation, wind_speed)


            return {
                "temperature": temperature,
                "humidity": humidity,
                "precipitation": precipitation,
                "wind_speed": wind_speed
            }
        
        return None
    except Exception as e:
        print(f"Error syncing weather data: {e}")
        return None
    