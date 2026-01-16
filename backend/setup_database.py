import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_database():
    """Create the database if it doesn't exist"""
    try:
        # Connect to default 'postgres' database
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            user="postgres",
            password="admin123",
            database="postgres"  # Connect to default database first
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Check if database exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'coursepro_db'")
        exists = cursor.fetchone()
        
        if not exists:
            print("📊 Database 'coursepro_db' not found. Creating...")
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier('coursepro_db')
            ))
            print("✅ Database 'coursepro_db' created successfully!")
        else:
            print("✅ Database 'coursepro_db' already exists!")
        
        cursor.close()
        conn.close()
        
        # Test connection to the actual database
        print("\n🔌 Testing connection to coursepro_db...")
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            user="postgres",
            password="admin123",
            database="coursepro_db"
        )
        print("✅ Successfully connected to coursepro_db!")
        conn.close()
        
        return True
        
    except psycopg2.Error as e:
        print(f"❌ Database error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("PostgreSQL Database Setup")
    print("=" * 60)
    create_database()
