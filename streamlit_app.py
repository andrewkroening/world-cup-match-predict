import pandas as pd
import streamlit as st

# Load data
spi_df = pd.read_csv(
    "https://projects.fivethirtyeight.com/soccer-api/international/spi_global_rankings_intl.csv"
)
