# import sqlite3
# import os

# def get_db_path():
#     """Trả về đường dẫn đến cơ sở dữ liệu SQLite"""
#     return os.path.join('/tmp', 'sheets_data.db')

# def init_database():
#     """Khởi tạo cơ sở dữ liệu SQLite"""
#     conn = sqlite3.connect(get_db_path())
#     cursor = conn.cursor()

#     # Khởi tạo bảng sheets_data
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS sheets_data (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT NOT NULL,
#             phone TEXT NOT NULL
#         )
#     """)

#     conn.commit()
#     conn.close()


# def insert_data(temperature, humidity, precipitation, wind_speed):
#     """Chèn dữ liệu vào bảng sheets_data"""
#     conn = sqlite3.connect(get_db_path())
#     cursor = conn.cursor()

#     cursor.execute("""
#     INSERT INTO sheets_data (temperature, humidity, precipitation, wind_speed)
#     VALUES (?, ?, ?, ?)
#     """, (temperature, humidity, precipitation, wind_speed))


#     conn.commit()
#     conn.close()


# def get_latest_weather_data():
#     """Lấy dữ liệu thời tiết mới nhất từ bảng sheets_data"""
#     conn = sqlite3.connect(get_db_path())
#     cursor = conn.cursor()

#     cursor.execute("""
#     SELECT temperature, humidity, precipitation, wind_speed
#     FROM sheets_data
#     ORDER BY id DESC
#     LIMIT 1
#     """)

#     data = cursor.fetchone()
#     conn.close()

#     return data


import os 
import psycopg2
from psycopg2.extras import DictCursor

def get_db_connection():
    
    DATABASE_URL = os.getenv("POSTGRES_URL")
    if not DATABASE_URL:
        raise ValueError("Missing environment variables")
    return psycopg2.connect(DATABASE_URL, sslmode='require')

def init_database():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sheets_data (
            id SERIAL PRIMARY KEY,
            temperature INTEGER NOT NULL,
            humidity INTEGER NOT NULL,
            precipitation FLOAT NOT NULL,
            wind_speed FLOAT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def insert_data(temperature, humidity, precipitation, wind_speed):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO sheets_data (temperature, humidity, precipitation, wind_speed)
    VALUES (%s, %s, %s, %s)
    """, (temperature, humidity, precipitation, wind_speed))

    conn.commit()
    conn.close()


def get_latest_weather_data():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=DictCursor)

    cursor.execute("""
    SELECT temperature, humidity, precipitation, wind_speed
    FROM sheets_data
    ORDER BY id DESC
    LIMIT 1
    """)

    data = cursor.fetchone()
    conn.close()

    return data