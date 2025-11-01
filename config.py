import os
import dotenv

dotenv.load_dotenv()
class MySQLConfig:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", 3306))
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        self.database = os.getenv("DB_NAME", "test")
        self.charset = os.getenv("DB_CHARSET", "utf8mb4")

# import pymysql
# def test_connection():
#     config = MySQLConfig()
#     try:
#         conn = pymysql.connect(
#             host=config.host,
#             port=config.port,
#             user=config.user,
#             password=config.password,
#             database=config.database,
#             charset=config.charset
#         )
#         print("连接成功！")
#         conn.close()
#     except Exception as e:
#         print("连接失败:", e)
#
# if __name__ == "__main__":
#     test_connection()