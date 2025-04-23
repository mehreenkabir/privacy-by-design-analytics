import pandas as pd
import numpy as np
from datetime import datetime

# Load anonymized dataset
df = pd.read_csv('data/anonymized_data.csv')

# Add random noise (-1, 0, or +1 year)
np.random.seed(42)
df['year_of_birth_noisy'] = df['year_of_birth'] + np.random.choice([-1, 0, 1], size=len(df))

# Save the new file with noise
df.to_csv('data/anonymized_data_differential.csv', index=False)

# Log the action
with open('logs/audit_log.txt', 'a') as log:
    log.write(f"[{datetime.now()}] Injected noise into year_of_birth for differential privacy.\n")


