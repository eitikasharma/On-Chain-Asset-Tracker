import pandas as pd
import plotly.express as px

# Load the CSV you downloaded from Dune
df = pd.read_csv("erc20_data.csv")

# Make sure the date column is read correctly
df['date'] = pd.to_datetime(df['date'])

# Show line chart of volume over time
fig = px.line(df, x="date", y="volume_usd", color="symbol", title="Token Transfer Volume (DAI & USDC)")
fig.show()
