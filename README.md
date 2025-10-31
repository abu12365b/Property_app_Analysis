# Property App Analysis 🏠📊

A comprehensive ETL (Extract, Transform, Load) pipeline for property management data analysis, designed to extract data from a Supabase PostgreSQL database and prepare it for Power BI analytics.

## 📋 Overview

This project provides a complete data pipeline that:
- **Extracts** property and tenant data from a Supabase database
- **Transforms** and cleans the data for analysis
- **Loads** processed data into CSV files for Power BI consumption
- **Analyzes** property management metrics through interactive notebooks

## 🏗️ Project Structure

```
Property_app_Analysis/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── config/                      # Configuration files
│   ├── __init__.py
│   ├── .env.template           # Environment template (copy to .env)
│   ├── db_config.py            # Database connection configuration
│   └── README.md               # Configuration guide
├── data/                       # Data storage
│   ├── lookup/                 # Reference data
│   ├── processed/              # Cleaned data for Power BI
│   └── raw/                    # Raw extracted data
├── etl/                        # ETL pipeline modules
│   ├── __init__.py
│   ├── extract.py              # Data extraction from database
│   ├── transform.py            # Data cleaning and transformation
│   ├── load.py                 # Data loading utilities
│   └── pipeline.py             # Main ETL orchestrator
├── notebooks/                  # Jupyter notebooks for analysis
│   └── exploration.ipynb       # Data exploration and visualization
├── powerbi/                    # Power BI assets
│   └── datasets/               # Power BI dataset configurations
└── utils/                      # Utility functions
    ├── helpers.py              # Helper functions
    └── db_explorer.py          # Database exploration tool
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- PostgreSQL database access (Supabase)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/abu12365b/Property_app_Analysis.git
   cd Property_app_Analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the template and fill in your actual values
   copy config\.env.template config\.env
   ```
   
   Edit `config/.env` with your actual database credentials:
   ```env
   SUPABASE_DB_HOST="your-supabase-host"
   SUPABASE_DB_PORT="6543"
   SUPABASE_DB_NAME="postgres"
   SUPABASE_DB_USER="postgres.your-project-id"
   SUPABASE_DB_PASSWORD="your-secure-password"
   ```

4. **Test database connection**
   ```bash
   python config\db_config.py
   ```

5. **Run the ETL pipeline**
   ```bash
   python etl\pipeline.py
   ```

## 📊 Database Schema

The pipeline works with the following Supabase tables:

### Property Table
- Property details including name, address, location
- Financial information (monthly rent, status)
- Metadata (created/updated timestamps)

### Tenant Table
- Tenant personal information
- Contact details
- Property associations and lease information

### Additional Tables
- **Expense**: Property-related expenses
- **Financial**: Financial records and transactions
- **Payment**: Payment history and tracking

## 🔧 ETL Pipeline

### Extract (`etl/extract.py`)
- Connects to Supabase PostgreSQL database using connection pooler
- Extracts data from specified tables
- Handles PostgreSQL case-sensitive table names

### Transform (`etl/transform.py`)
- Cleans and standardizes data
- Removes duplicates
- Normalizes column names to lowercase
- Applies business logic transformations

### Load (`etl/load.py`)
- Exports processed data to CSV format
- Optimized for Power BI consumption
- Maintains data integrity and relationships

## 📈 Usage Examples

### Running Individual Components

**Extract data only:**
```bash
python etl\extract.py
```

**Transform existing data:**
```bash
python etl\transform.py
```

**Full pipeline:**
```bash
python etl\pipeline.py
```

### Database Exploration

Explore your database structure:
```bash
python utils\db_explorer.py
```

### Jupyter Analysis

Launch Jupyter for interactive analysis:
```bash
jupyter lab notebooks/exploration.ipynb
```

## 🔒 Security

- **Environment Variables**: All sensitive data is stored in `.env` files (not committed to Git)
- **Connection Security**: Uses SSL/TLS connections to Supabase
- **Credential Management**: Template-based configuration prevents accidental exposure

## 📦 Dependencies

Key packages used in this project:

```txt
psycopg2-binary==2.9.11     # PostgreSQL adapter
python-dotenv==1.1.0        # Environment management
pandas                      # Data manipulation
numpy                       # Numerical computing
matplotlib                  # Data visualization
seaborn                     # Statistical visualization
jupyter                     # Interactive notebooks
```

## 🛠️ Configuration

### Database Connection

The project uses Supabase's transaction pooler for optimal performance:

- **Host**: Uses pooler endpoint for better connection management
- **Port**: 6543 (transaction pooler port)
- **SSL**: Required for secure connections
- **Timeout**: 10 seconds connection timeout

### Environment Setup

1. Copy `config/.env.template` to `config/.env`
2. Fill in your Supabase credentials
3. Never commit the `.env` file to version control


