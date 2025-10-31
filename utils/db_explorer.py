import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from config.db_config import get_connection
import pandas as pd

def explore_database():
    """Explore what tables and schemas exist in the database"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        print("=== Database Exploration ===\n")
        
        # List all schemas
        print("1. Available Schemas:")
        cursor.execute("""
            SELECT schema_name 
            FROM information_schema.schemata 
            WHERE schema_name NOT IN ('information_schema', 'pg_catalog', 'pg_toast')
            ORDER BY schema_name;
        """)
        schemas = cursor.fetchall()
        for schema in schemas:
            print(f"   - {schema[0]}")
        
        print("\n2. Tables in 'public' schema:")
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name;
        """)
        tables = cursor.fetchall()
        if tables:
            for table in tables:
                print(f"   - {table[0]}")
        else:
            print("   No tables found in public schema")
        
        print("\n3. All user tables (any schema):")
        cursor.execute("""
            SELECT table_schema, table_name 
            FROM information_schema.tables 
            WHERE table_schema NOT IN ('information_schema', 'pg_catalog', 'pg_toast')
            ORDER BY table_schema, table_name;
        """)
        all_tables = cursor.fetchall()
        if all_tables:
            for table in all_tables:
                print(f"   - {table[0]}.{table[1]}")
        else:
            print("   No user tables found")
            
        print("\n4. Sample data from first available table (if any):")
        if all_tables:
            first_table_schema = all_tables[0][0]
            first_table_name = all_tables[0][1]
            sample_query = f'SELECT * FROM "{first_table_schema}"."{first_table_name}" LIMIT 3;'
            print(f"   Querying: {sample_query}")
            
            try:
                df = pd.read_sql(sample_query, conn)
                print(f"   Columns: {list(df.columns)}")
                print(f"   Sample data:")
                print(df)
            except Exception as e:
                print(f"   Error reading sample data: {e}")
        
    except Exception as e:
        print(f"Error exploring database: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    explore_database()