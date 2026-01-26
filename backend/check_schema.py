import database
from sqlalchemy import inspect

db = database.SessionLocal()
inspector = inspect(database.engine)

# Get all tables
tables = inspector.get_table_names()
print('Tables in database:')
for table in sorted(tables):
    print(f'  - {table}')

# Check if user_test_attempts exists and get its structure
if 'user_test_attempts' in tables:
    columns = inspector.get_columns('user_test_attempts')
    print('\nuser_test_attempts columns:')
    for col in columns:
        col_type = str(col['type'])
        print(f'  - {col["name"]}: {col_type}')
    
    # Check data
    from sqlalchemy import text
    result = db.execute(text('SELECT COUNT(*) FROM user_test_attempts')).scalar()
    print(f'  Data count: {result} rows')
else:
    print('\nuser_test_attempts does NOT exist in database')

# Check test_attempts structure
if 'test_attempts' in tables:
    columns = inspector.get_columns('test_attempts')
    print('\ntest_attempts columns:')
    for col in columns:
        col_type = str(col['type'])
        print(f'  - {col["name"]}: {col_type}')
    
    # Check data
    from sqlalchemy import text
    result = db.execute(text('SELECT COUNT(*) FROM test_attempts')).scalar()
    print(f'  Data count: {result} rows')

db.close()
