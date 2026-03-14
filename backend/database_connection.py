import pyodbc

def get_connection():
    server = r'.\SQLEXPRESS' 
    database = 'InventoryMasterDB'
    
    conn_str = (
        f'DRIVER={{SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )
    
    try:
        conn = pyodbc.connect(conn_str)
        print("Veritabanı bağlantısı başarılı!")
        return conn
    except Exception as e:
        print(f"Bağlantı hatası: {e}")
        return None

if __name__ == "__main__":
    get_connection()