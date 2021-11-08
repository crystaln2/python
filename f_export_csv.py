import mysql.connector
import pandas as pd

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_buah",
  use_pure=True
)

try:
    query = "SELECT * FROM stok_buah"
    result_dataFrame = pd.read_sql(query,db)
    result_dataFrame.to_csv('Test.csv')
    
except Exception as e:
    print(str(e))