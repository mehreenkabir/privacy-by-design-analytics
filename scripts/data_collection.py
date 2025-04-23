from faker import Faker
import pandas as pd
from datetime import datetime

# Create the Faker generator
fake = Faker()

# Generate 100 fake user records
data = {
    'full_name': [fake.name() for _ in range(100)],
    'email': [fake.email() for _ in range(100)],
    'phone_number': [fake.phone_number() for _ in range(100)],
    'address': [fake.address().replace('\n', ', ') for _ in range(100)],
    'date_of_birth': [fake.date_of_birth().strftime("%Y-%m-%d") for _ in 
range(100)]
}

# Create a DataFrame and save it to CSV
df = pd.DataFrame(data)
df.to_csv('data/raw_data.csv', index=False)

# Log this action
with open('logs/audit_log.txt', 'a') as log:
    log.write(f"[{datetime.now()}] Generated synthetic personal data.\n")

