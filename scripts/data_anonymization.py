import pandas as pd
import hashlib
from datetime import datetime

# Hash function using SHA-256
def anonymize(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Load the raw data
df = pd.read_csv('data/raw_data.csv')

# Apply hashing to all personal fields
df['full_name'] = df['full_name'].apply(anonymize)
df['email'] = df['email'].apply(anonymize)
df['phone_number'] = df['phone_number'].apply(anonymize)
df['address'] = df['address'].apply(anonymize)

# Replace full birthdate with just the year (minimization)
df['year_of_birth'] = pd.to_datetime(df['date_of_birth']).dt.year
df.drop(columns=['date_of_birth'], inplace=True)

# Save anonymized data
df.to_csv('data/anonymized_data.csv', index=False)

# Log the action
with open('logs/audit_log.txt', 'a') as log:
    log.write(f"[{datetime.now()}] Anonymized personal data and saved to anonymized_data.csv\n")

