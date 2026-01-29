# TABLE STRUCTURE CLARIFICATION
## `user_test_attempts` vs `test_attempts`

### Purpose
- **`user_test_attempts`** = Tests taken by each SPECIFIC user (per-user tracking table)
- **`test_attempts`** = Total tests of all users in the system (system-wide tracking)

### Schema

#### user_test_attempts (PRIMARY PER-USER TABLE)
```sql
CREATE TABLE user_test_attempts (
    attempt_id INTEGER PRIMARY KEY,           -- Unique attempt ID
    user_id INTEGER NOT NULL,                 -- Which user took this test
    test_id INTEGER NOT NULL,                 -- Which test was taken
    score INTEGER,                            -- Test score
    total_questions INTEGER,                  -- Number of questions answered
    attempt_date TIMESTAMP WITH TIME ZONE,   -- When the test was taken
    time_taken INTEGER,                      -- How long it took (seconds)
    created_at TIMESTAMP WITH TIME ZONE      -- Record creation timestamp
);

PURPOSE: Track individual user's test history
QUERY EXAMPLE: "Get all tests taken by User 42"
    SELECT * FROM user_test_attempts WHERE user_id = 42;
    Result: Shows all 11 tests User 42 has taken with detailed data
```

#### test_attempts (SYSTEM-WIDE TABLE)
```sql
CREATE TABLE test_attempts (
    attempt_id INTEGER PRIMARY KEY,           -- Unique attempt ID
    user_id INTEGER NOT NULL,                 -- Which user took this test
    test_id INTEGER NOT NULL,                 -- Which test was taken
    taken_at TIMESTAMP                        -- When the test was taken
);

PURPOSE: Track all test attempts across all users
QUERY EXAMPLE: "Get total test count"
    SELECT COUNT(*) FROM test_attempts;
    Result: 25 tests from all users
```

### Dual-Table Synchronization

Both tables are kept in sync automatically:
1. When a test attempt is saved, it goes to `test_attempts`
2. Then it's immediately synced to `user_test_attempts`
3. Duplicate checks prevent re-insertion

### Current Data (January 30, 2026)

**Per-User Breakdown:**
- User 42: 11 tests
- User 48: 7 tests
- User 46: 2 tests
- User 47: 2 tests
- User 43: 2 tests
- User 45: 1 test
- **Total: 25 tests from 6 users**

Both tables now contain exactly 25 records ✅

### Code Implementation

**In main.py - FormAssessment endpoint:**
```python
# 1. Create and commit TestAttempt to test_attempts
db.add(models.TestAttempt(...))
db.commit()

# 2. Sync to user_test_attempts
cursor = db.execute(text('''
    SELECT attempt_id FROM user_test_attempts WHERE attempt_id = :id
'''), {'id': attempt_id})

if not cursor.fetchone():  # Avoid duplicates
    db.execute(text('''
        INSERT INTO user_test_attempts (...) VALUES (...)
    '''))
    db.commit()
```

**In main.py - save_adaptive_session_to_db():**
Same dual-insert pattern ensures consistency.

### Query Examples

**Get all tests for a specific user:**
```sql
SELECT attempt_id, test_id, total_questions, attempt_date
FROM user_test_attempts
WHERE user_id = 48
ORDER BY attempt_date DESC;
```

**Get total tests across system:**
```sql
SELECT COUNT(*) as total_tests, COUNT(DISTINCT user_id) as total_users
FROM test_attempts;
-- Result: 25 tests from 6 users
```

**Get tests per user (system-wide report):**
```sql
SELECT user_id, COUNT(*) as tests_taken
FROM user_test_attempts
GROUP BY user_id
ORDER BY tests_taken DESC;
```

### Benefits of Dual-Table Approach
1. **user_test_attempts**: Optimized for user-centric queries with detailed tracking data
2. **test_attempts**: Lightweight for system-wide analytics and reporting
3. **No duplication**: Careful sync logic prevents duplicate records
4. **Flexibility**: Each table can be extended independently if needed

---
**Last Updated:** January 30, 2026
**Status:** ✅ Tables synchronized (both have 25 records)
