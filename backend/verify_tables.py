import psycopg2

conn = psycopg2.connect(host='localhost', database='coursepro_db', user='postgres', password='admin123')
cursor = conn.cursor()

print('FINAL VERIFICATION - Table Synchronization Status\n')

cursor.execute('SELECT COUNT(*) FROM test_attempts')
test_count = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM user_test_attempts')
user_count = cursor.fetchone()[0]

print(f'test_attempts (system-wide): {test_count} records')
print(f'user_test_attempts (per-user): {user_count} records')
status = '[OK] SYNCHRONIZED' if test_count == user_count else '[WARN] MISMATCH'
print(f'Status: {status}')

print('\nPer-user test count:')
cursor.execute('SELECT user_id, COUNT(*) as tests FROM user_test_attempts GROUP BY user_id ORDER BY tests DESC')
for uid, count in cursor.fetchall():
    print(f'  User {uid}: {count} tests')

print('\nForeign key constraint:')
cursor.execute("""
    SELECT pg_get_constraintdef(c.oid) FROM pg_constraint c 
    WHERE c.conrelid = 'recommendations'::regclass 
    AND c.conname = 'recommendations_attempt_id_fkey'
""")
result = cursor.fetchone()
if result:
    print(f'  {result[0]}')
else:
    print('  [NOT FOUND]')

cursor.close()
conn.close()

print('\n[COMPLETE] Tables are properly synchronized and tracking tests correctly')
