"""
Example script demonstrating and VERIFYING Connection Pooling.

This script provides empirical evidence that the pool:
1. Maintains multiple distinct connections.
2. Handles concurrent requests simultaneously.
3. Reuses connections once they are returned.
"""

import os
import threading
import time
from chinook_pydantic_repository import DatabasePoolManager, ArtistRepository

# Database URL is pulled from the environment
DB_URL = os.environ.get("DATABASE_URL")

def fetch_worker(worker_id, pool_manager):
    """
    Simulates a worker performing a database task.
    """
    repo = ArtistRepository(pool_manager)
    
    # Borrow a connection and get its unique backend PID from PostgreSQL
    with pool_manager.connection() as conn:
        pid = conn.info.backend_pid
        print(f"[Worker {worker_id}] Borrowed connection with Backend PID: {pid}")
        
        # Simulate some work
        artist = repo.get_by_id(1, conn=conn)
        time.sleep(1) # Hold the connection for a second
        
        print(f"[Worker {worker_id}] Finished task for Artist: {artist.name}")

def main():
    if not DB_URL:
        print("Error: DATABASE_URL environment variable is not set.")
        return

    print("--- 1. Initializing Pool (min_size=2, max_size=5) ---")
    # We explicitly set a small pool to see it in action
    pool_manager = DatabasePoolManager(DB_URL, min_size=2, max_size=5)
    
    try:
        print("\n--- 2. Evidence: Concurrent Execution ---")
        print("Starting 3 workers simultaneously...")
        print("Because max_size > 3, the pool should give each worker a UNIQUE connection.\n")
        
        threads = []
        for i in range(3):
            t = threading.Thread(target=fetch_worker, args=(i, pool_manager))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print("\n--- 3. Evidence: Connection Reuse ---")
        print("Starting 2 more workers sequentially...")
        print("The pool should now REUSE PIDs seen above because they were returned to the pool.\n")
        
        for i in range(3, 5):
            fetch_worker(i, pool_manager)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pool_manager.close()
        print("\n--- 4. Pool Closed ---")

if __name__ == "__main__":
    main()
