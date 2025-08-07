# PostgreSQL Duplicate Key Error Analysis

**Date**: August 7, 2025  
**Error**: `duplicate key value violates unique constraint "threads_id_key"`  
**Status**: 🔴 **CRITICAL** - Occurs across entire system

## 🔍 Root Cause Analysis

### The Problem

PostgreSQL unique constraint violation occurs when the same `thread_id` is used multiple times. The error appears everywhere in the system:

```
psycopg.errors.UniqueViolation: duplicate key value violates unique constraint "threads_id_key"
DETAIL:  Key (id)=(todo_planner_71598832-bf32-4b39-acf3-9518096e86c6) already exists.
```

### Database Table Structure

The `threads` table has a unique constraint:

```sql
CREATE TABLE threads (
    id TEXT PRIMARY KEY,      -- This is the thread_id
    user_id UUID NOT NULL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    last_access TIMESTAMP
);
```

The unique constraint `"threads_id_key"` is on the `id` column (thread_id).

### Why the Duplicate Occurs

**Thread ID Generation Logic** (from `persistence_mixin.py:428`):

```python
def _generate_default_thread_id(self) -> str:
    unique_id = str(uuid.uuid4())
    agent_name = getattr(self, "name", "agent")
    thread_id = f"{agent_name}_{unique_id}"
    return thread_id
```

**The Issue**: While each UUID is unique, the **same thread_id is being reused** between different executions or processes.

### Where the Error Occurs

Found in `postgres_saver_with_thread_creation.py` line 68-87:

```python
cursor.execute(
    """
    INSERT INTO threads (id, user_id, created_at, updated_at, last_access)
    VALUES (%s, %s, NOW(), NOW(), NOW())
    ON CONFLICT (id, user_id) DO NOTHING
    """,
    (thread_id, user_id),
)
```

**The Key Problem**: The `ON CONFLICT` clause is `ON CONFLICT (id, user_id)` but the unique constraint is only on `id` (thread_id). This mismatch means the conflict handling doesn't work properly.

## 🚨 Technical Analysis

### Database Schema vs Code Mismatch

1. **Database Constraint**: `UNIQUE (id)` - only thread_id must be unique
2. **Code Conflict Handling**: `ON CONFLICT (id, user_id)` - expects both to be unique
3. **Result**: When same thread_id exists with different user_id, constraint fails

### Example Scenario

1. Agent runs with `thread_id="todo_planner_abc123"` and `user_id="user1"`
2. Later execution uses same `thread_id="todo_planner_abc123"` but `user_id="user2"`
3. Database rejects because thread_id already exists (even with different user_id)
4. `ON CONFLICT (id, user_id) DO NOTHING` doesn't trigger because it needs BOTH to match

## 🔧 Root Causes

### 1. Thread ID Reuse

Thread IDs are being reused across different executions. This happens when:

- Same agent name generates similar patterns
- Development/testing with consistent names
- Process restarts but database persists

### 2. Constraint Mismatch

The database schema and conflict handling don't match:

- Database: `UNIQUE(id)`
- Code: `ON CONFLICT (id, user_id)`

### 3. User ID Strategy

Default user ID is hardcoded:

```python
user_id = "5335c7e6-1d51-42d2-b958-0ad2ad2c269b"  # deloreanblack@gmail.com
```

Same thread_id with same user_id should use `DO NOTHING`, but that's not happening.

## 🛠️ Solutions

### Option 1: Fix the Conflict Handling (Quick Fix)

```python
# Change from:
ON CONFLICT (id, user_id) DO NOTHING

# To:
ON CONFLICT (id) DO NOTHING
```

### Option 2: Make Thread IDs Truly Unique (Better)

```python
def _generate_default_thread_id(self) -> str:
    # Include timestamp for true uniqueness
    unique_id = str(uuid.uuid4()) + "_" + str(int(time.time()))
    agent_name = getattr(self, "name", "agent")
    thread_id = f"{agent_name}_{unique_id}"
    return thread_id
```

### Option 3: Fix Database Schema (Proper Fix)

Change the constraint to match the code:

```sql
-- Add composite unique constraint
ALTER TABLE threads ADD CONSTRAINT threads_id_user_id_key UNIQUE (id, user_id);
```

### Option 4: Update Handling (Recommended)

```python
cursor.execute(
    """
    INSERT INTO threads (id, user_id, created_at, updated_at, last_access)
    VALUES (%s, %s, NOW(), NOW(), NOW())
    ON CONFLICT (id) DO UPDATE SET
        last_access = NOW(),
        updated_at = NOW()
    """,
    (thread_id, user_id),
)
```

## 📊 Impact Assessment

### Files Affected (147+ occurrences)

- **Every agent execution** that uses persistence
- **All game environments** (battleship, chess, etc.)
- **Multi-agent workflows**
- **API endpoints** and data flow
- **Tests** across packages

### Critical Impact

- **Battleship game**: Fails on initialization
- **SimpleAgentV3**: Cannot save state
- **Multi-agent workflows**: Break on persistence
- **Production APIs**: Thread creation failures

## 🚀 Recommended Fix

**Immediate (5 minutes)**:

```python
# In postgres_saver_with_thread_creation.py line 72
ON CONFLICT (id) DO NOTHING  # Remove user_id from conflict
```

**Long-term (proper solution)**:

1. Fix database schema to match expectations
2. Add proper update-on-conflict handling
3. Consider thread ID uniqueness strategies
4. Add monitoring for constraint violations

## 🎯 Testing Plan

1. **Verify Fix**: Run SimpleAgentV3 with postgres enabled
2. **Test Multi-Agent**: Ensure workflows complete
3. **Load Testing**: Multiple agents with same names
4. **Production Check**: Monitor constraint violations

## 📝 Next Steps

1. ✅ **IDENTIFIED**: Root cause in conflict handling mismatch
2. 🔄 **FIX**: Update `ON CONFLICT` clause
3. 🧪 **TEST**: Verify fix works across system
4. 📊 **MONITOR**: Check for recurring issues

---

**Key Insight**: The postgres error is a **schema mismatch issue** between the database constraint (id only) and the conflict handling code (id + user_id). This causes the `DO NOTHING` to fail when it should succeed.
