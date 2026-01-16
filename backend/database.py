import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# If no DATABASE_URL in .env, use SQLite as fallback
if not DATABASE_URL:
    print("⚠️ No DATABASE_URL found in .env, using SQLite as fallback")
    DATABASE_URL = "sqlite:///./coursepro.db"

try:
    # Create engine with connection pool settings for PostgreSQL
    if DATABASE_URL.startswith("postgresql"):
        print(f"🔌 Connecting to PostgreSQL: {DATABASE_URL.split('@')[1] if '@' in DATABASE_URL else 'localhost'}")
        engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,  # Verify connections before using
            pool_size=10,
            max_overflow=20,
            echo=False  # Set to True for SQL query logging
        )
    else:
        print(f"🔌 Connecting to SQLite: {DATABASE_URL}")
        engine = create_engine(
            DATABASE_URL,
            connect_args={"check_same_thread": False}
        )
    
    # Test the connection
    with engine.connect() as conn:
        print("✅ Database connection successful!")
        
except Exception as e:
    print(f"❌ Database connection failed: {e}")
    print("⚠️ Falling back to SQLite...")
    DATABASE_URL = "sqlite:///./coursepro.db"
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()