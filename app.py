import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# ---------------------------
# PAGE CONFIG (MUST BE FIRST)
# ---------------------------
st.set_page_config(
    page_title="AI Arbitrage Dashboard",
    layout="wide"
)

# ---------------------------
# SAFE START (prevents blank screen)
# ---------------------------
st.title("💰 AI Blockchain Arbitrage Dashboard")
st.write("System initializing...")

# ---------------------------
# SIDEBAR SETTINGS
# ---------------------------
st.sidebar.header("⚙️ Settings")

initial_balance = st.sidebar.number_input("Initial Balance ($)", 100, 100000, 1000)
threshold = st.sidebar.slider("Arbitrage Threshold (%)", 0.1, 5.0, 1.0)

# ---------------------------
# BUTTON
# ---------------------------
run = st.button("▶ Run Bot")

# ---------------------------
# PLACEHOLDERS
# ---------------------------
price_placeholder = st.empty()
status_placeholder = st.empty()
profit_placeholder = st.empty()
log_placeholder = st.empty()

# ---------------------------
# FUNCTION (SAFE DATA)
# ---------------------------
def get_prices():
    return np.random.uniform(30000, 31000), np.random.uniform(30000, 31000)

# ---------------------------
# MAIN EXECUTION
# ---------------------------
try:
    balance = initial_balance
    profit = 0
    logs = []

    if run:
        for i in range(15):
            binance, coinbase = get_prices()

            diff = abs(binance - coinbase)
            percent = (diff / min(binance, coinbase)) * 100

            # PRICE TABLE
            df = pd.DataFrame({
                "Exchange": ["Binance", "Coinbase"],
                "Price ($)": [round(binance, 2), round(coinbase, 2)]
            })
            price_placeholder.dataframe(df, use_container_width=True)

            # ARBITRAGE LOGIC
            if percent > threshold:
                trade_profit = np.random.uniform(5, 20)
                profit += trade_profit
                balance += trade_profit

                status_placeholder.success("✅ Arbitrage Opportunity Found!")
                logs.append(f"{datetime.now().strftime('%H:%M:%S')} Profit: ${round(trade_profit,2)}")
            else:
                status_placeholder.warning("⏳ No Opportunity")

            # METRICS
            profit_placeholder.metric("💵 Total Profit", f"${round(profit,2)}")

            # LOGS
            log_placeholder.text("\n".join(logs[-5:]))

            time.sleep(1)

    else:
        st.info("👆 Click 'Run Bot' to start simulation")

except Exception as e:
    st.error("❌ Error occurred:")
    st.code(str(e))

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.markdown("👨‍💻 Final Year Project | AI + Blockchain Arbitrage Simulator")