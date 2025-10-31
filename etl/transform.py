import pandas as pd

def clean_property(df: pd.DataFrame) -> pd.DataFrame:
    # Example: drop duplicates, fix column names
    df = df.drop_duplicates()
    df.columns = [col.lower() for col in df.columns]
    return df

def clean_tenant(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df.columns = [col.lower() for col in df.columns]
    return df

if __name__ == "__main__":
    property_df = pd.read_csv("data/raw/property.csv")
    tenant_df = pd.read_csv("data/raw/tenant.csv")

    property_clean = clean_property(property_df)
    tenant_clean = clean_tenant(tenant_df)

    property_clean.to_csv("data/processed/property.csv", index=False)
    tenant_clean.to_csv("data/processed/tenant.csv", index=False)

    print("Transformation complete! Clean tables saved to data/processed/")
