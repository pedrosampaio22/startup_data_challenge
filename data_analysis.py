# Import necessary libraries
import pandas as pd
import plotly.express as px

# Read the Parquet file
# Note: Make sure the Parquet file is in the same directory as your script
df = pd.read_parquet('dados_sensores_5000.parquet')

# Let's first look at what's in our dataset
print("\n=== Basic Information About Our Dataset ===")
print(df.info())

print("\n=== First Few Rows of Our Data ===")
print(df.head())

print("\n=== Basic Statistical Summary ===")
print(df.describe())