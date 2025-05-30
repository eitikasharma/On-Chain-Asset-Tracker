

📌 Project Title: On-Chain Asset Tracker

🧭 Goal

To track how frequently and how much value is being transferred across popular Ethereum tokens like DAI and USDC, using public blockchain data.

💡 Why This Is Useful

This tracker gives real-time insight into user activity and liquidity trends across decentralized finance (DeFi). 

Some examples:

🔍 DeFi Analysts can spot spikes in token transfers and investigate if a major event happened (e.g., a protocol hack, major market move).

📊 Investors can understand if a token is gaining popularity by looking at daily transfer volume.

🛡️ Risk teams can monitor unusual surges or drops in transaction counts, which may signal market manipulation or whale movement.

🧱 Founders or developers of DeFi protocols can see how frequently their tokens are used or held — a key health metric.

🔗 Data Source

Dune Analytics: Public Ethereum blockchain data (ERC-20 token transfers)

SQL used to extract:

-Daily number of transactions (tx_count)

-Total USD value transferred (volume_usd)

-For specific tokens like DAI, USDC, etc.

🛠 Tools Used
-Dune SQL

-Python and Pandas for data visualization

-Google Sheets / Excel to analyze or chart trends

📉 Future Additions
Add more tokens (e.g., UNI, AAVE)

Show wallet-level activity (e.g., new vs. returning users)

Build live charts with Python or Streamlit

Compare activity across chains (e.g., Ethereum vs. Base or Arbitrum)
