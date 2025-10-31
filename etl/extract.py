import pandas as pd
from config.db_config import get_connection

def extract_table(table_name: str) -> pd.DataFrame:
    conn = get_connection()
    # Quote table name for PostgreSQL case sensitivity
    query = f'SELECT * FROM "{table_name}";'
    df = pd.read_sql(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    property_df = extract_table("Property")
    tenant_df = extract_table("Tenant")

    # Save raw data locally
    property_df.to_csv("data/raw/property.csv", index=False)
    tenant_df.to_csv("data/raw/tenant.csv", index=False)

    print("Extraction complete! Tables saved to data/raw/")
