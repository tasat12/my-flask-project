from flask import Flask
import os
import psycopg2

app= Flask(__name__)

@app.route('/')
def hello_world():
    db_host = os.environ.get('POSTGRES_HOST', 'localhost')

    # データベース接続のテスト
    try:
        conn = psycopg2.connect(
           host=db_host,
           user=os.environ.get('POSTGRES_USER', 'user'),
           password=os.environ.get('POSTGRES_PASSWORD', 'password'),
           dbname=os.environ.get('POSTGRES_DB', 'mydatabase'),
           port='5432'
        )
        conn.close()
        db_status = '接続成功'
    except Exception as e:
        db_status = f'接続失敗: {e}'

    return f'Hello, Docker! The database is running at {db_host}. DB接続ステータス: {db_status}'


if  __name__ == '__main__':
     print(f"POSTGRES_HOST environment variable: {os.environ.get('POSTGRES_HOST')}")
     print(f"Flask app starting with DB host: {os.environ.get('POSTGRES_HOST')}")
     app.run(host='0.0.0.0', port=5000)

