import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from etl.extract import extract_table
from etl.transform import clean_property, clean_tenant
import pandas as pd

def run_pipeline():
    # Extract
    property_df = extract_table("Property")
    tenant_df = extract_table("Tenant")

    # Transform
    property_clean = clean_property(property_df)
    tenant_clean = clean_tenant(tenant_df)

    # Load (CSV)
    property_clean.to_csv("data/processed/property.csv", index=False)
    tenant_clean.to_csv("data/processed/tenant.csv", index=False)

    print("Pipeline complete! Processed data ready for Power BI.")

if __name__ == "__main__":
    run_pipeline()
