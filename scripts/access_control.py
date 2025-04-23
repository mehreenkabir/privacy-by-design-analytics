import pandas as pd

ROLE = input("Enter your role (admin or analyst): ").strip().lower()

if ROLE == "admin":
    df = pd.read_csv('data/raw_data.csv')
    print("\n[ADMIN VIEW] Full raw data:\n")
    print(df.head())

elif ROLE == "analyst":
    df = pd.read_csv('data/anonymized_data_differential.csv')
    print("\n[ANALYST VIEW] Anonymized data with noise:\n")
    print(df[['email', 'year_of_birth_noisy']].head())

else:
    print("Access denied: Invalid role.")

