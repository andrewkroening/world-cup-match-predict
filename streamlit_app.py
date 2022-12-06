import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="TONS OF FUN",
    page_icon=":soccer:",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

# Load data
spi_df = pd.read_csv(
    "https://projects.fivethirtyeight.com/soccer-api/international/spi_global_rankings_intl.csv"
)

# import the scraper for the games
# import spi rankings df
# import the visualization tool

# Create a title and subtitle
st.title("Welcome to this totally not serious FIFA World Cup 2022 Predictor Tool")
st.subheader(
    "This tool will help you predict the outcome of the 2022 FIFA World Cup using SPI Rankings"
)

st.markdown("""---""")

st.subheader("Today's Matches")
st.caption("Matches go here")

# matches output

st.selectbox("Select a match", [0])

st.subheader("Predictions")
st.caption("Predictions go here")

# predictions output

st.markdown("""---""")
st.caption("Access the GitHub repo here")
st.caption("Special thanks to 538.com for the data")
st.caption("Access the youtube video here")
