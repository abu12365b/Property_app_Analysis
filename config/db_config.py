import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_connection():
    """Get database connection optimized for Supabase pooler"""
    return psycopg2.connect(
        host=os.getenv("SUPABASE_DB_HOST"),
        port=os.getenv("SUPABASE_DB_PORT"),
        dbname=os.getenv("SUPABASE_DB_NAME"),
        user=os.getenv("SUPABASE_DB_USER"),
        password=os.getenv("SUPABASE_DB_PASSWORD"),
        # Additional options for pooler compatibility
        sslmode='require',
        connect_timeout=10,
        application_name='property_app_analysis'
    )

# Connect to the database
try:
    connection = get_connection()
    print("Connection successful!")
    
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")