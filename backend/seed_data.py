from database_connection import get_connection
import random

def seed_products():
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    
    sample_products = [
        ('Mavi Kot Pantolon', 'Giyim', 450.00, 100),
        ('Beyaz Gömlek', 'Giyim', 300.00, 50),
        ('Siyah Ceket', 'Giyim', 850.00, 20),
        ('Spor Ayakkabı', 'Ayakkabı', 1200.00, 30),
        ('Deri Kemer', 'Aksesuar', 150.00, 80),
        ('Kırmızı T-Shirt', 'Giyim', 200.00, 150),
        ('Klasik Saat', 'Aksesuar', 2500.00, 10),
        ('Bez Çanta', 'Aksesuar', 50.00, 200),
        ('Yün Kazak', 'Giyim', 400.00, 45),
        ('Kumaş Pantolon', 'Giyim', 350.00, 60)
    ]

    try:
        cursor.executemany(
            "INSERT INTO Products (ProductName, Category, Price, StockQuantity) VALUES (?, ?, ?, ?)",
            sample_products
        )
        conn.commit() 
        print(f"{len(sample_products)} adet ürün başarıyla eklendi!")
    except Exception as e:
        print(f"Veri ekleme hatası: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    seed_products()