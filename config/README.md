# Configuration Files

## Environment Setup

1. Copy `.env.template` to `.env`
2. Fill in your actual database credentials in `.env`
3. Never commit the `.env` file to version control

## Security Notice

The `.env` file contains sensitive information including database passwords. 
Always keep it local and never share it publicly.

## Files

- `.env.template` - Template file with placeholder values
- `.env` - Your actual environment variables (DO NOT COMMIT)
- `db_config.py` - Database configuration loader