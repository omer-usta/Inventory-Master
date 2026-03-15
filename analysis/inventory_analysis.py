import sys
import os
import matplotlib.pyplot as plt 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.database_connection import get_connection

def create_chart():
    conn = get_connection()
    if not conn: return
    cursor = conn.cursor()

    cursor.execute("SELECT Category, SUM(StockQuantity) as TotalStock FROM Products GROUP BY Category")
    data = cursor.fetchall()
    
    categories = [row.Category for row in data]
    stocks = [row.TotalStock for row in data]

    plt.figure(figsize=(10, 6))
    plt.bar(categories, stocks, color='skyblue') 
    plt.xlabel('Kategoriler')
    plt.ylabel('Toplam Stok Adedi')
    plt.title('Kategori Bazlı Stok Durumu')
    
    plt.show()
    conn.close()

if __name__ == "__main__":
    create_chart()