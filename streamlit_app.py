import pandas as pd

import streamlit as st


from logic.scraper import get_matches

from logic.spi_dist import get_spi_dist

from logic.spi_plots import spi_plots

from logic.spi_winner import spi_winner


st.set_page_config(
    page_title="TONS OF FUN",
    page_icon="⚽️",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)


# Load data

spi_df = pd.read_csv(
    "https://projects.fivethirtyeight.com/soccer-api/international/spi_global_rankings_intl.csv"
)


# Get the next match

next_match = get_matches()

# convert the date column to datetime format

next_match["Date"] = pd.to_datetime(next_match["Date"])

# format the date to be more readable

next_match["Date"] = next_match["Date"].dt.strftime("%B %d, %Y")


# Create a title and subtitle

st.title("Welcome to this totally not serious FIFA World Cup 2022 Predictor Tool")

st.caption(
    "This tool will help you predict the outcome of the 2022 FIFA World Cup using Soccer Power Index Rankings"
)

st.caption(
    "Although built for the 2022 World Cup, it will work for any international match."
)


# add a sidebar with upcoming matches

st.sidebar.header("Upcoming Matches")


st.sidebar.markdown("""---""")


for i in next_match.index:

    st.sidebar.subheader(f"{next_match['Team1'][i]} vs {next_match['Team2'][i]}")

    st.sidebar.write(
        spi_winner(
            get_spi_dist(spi_df, next_match["Team1"][i], next_match["Team2"][i]),
            next_match["Team1"][i],
            next_match["Team2"][i],
        )
    )

    st.sidebar.caption(f"Date: {next_match['Date'][i]}")


st.sidebar.markdown("""---""")


st.markdown("""---""")


st.subheader("Make a match prediction")


c1, c2, c3 = st.columns((2, 2, 1))


with c1:

    team1 = st.selectbox("Team 1", spi_df["name"].sort_values())


with c2:

    team2 = st.selectbox(
        "Team 2",
        spi_df["name"].sort_values()[
            1:,
        ],
    )


with c3:

    st.write(" ")

#     st.write(" ")

#     st.button("Predict", on_click=[]))


spi_dist_df = get_spi_dist(spi_df, team1, team2)


st.write(spi_winner(spi_dist_df, team1, team2))


pred_plot = spi_plots(spi_dist_df)


st.altair_chart(pred_plot, use_container_width=True)


# predictions output


st.markdown("""---""")

st.markdown(
    "Special thanks to fivethirtyeight.com for providing the [Soccer Power Index](https://projects.fivethirtyeight.com/soccer-api/international/spi_global_rankings_intl.csv) we used in our predictions."
)

st.markdown(
    "For more info on the code behind this tool, check out the [GitHub repo](https://github.com/andrewkroening/tons-of-fun)"
)

st.caption("Access the youtube video here")

st.caption("Brought to you by 4 dudes just tryna make it")
