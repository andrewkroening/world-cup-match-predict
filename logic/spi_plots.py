"""This module plots the SPI distributions for the data and teams selected."""

import altair as alt


def spi_plots(spi_dist_df):
    """Plot the distributions for the two teams selected, with the higher ranked team in green and the lower in red.

    Args:
        spi_dist_df (pd.DataFrame): DataFrame containing the distributions for each team with this structure:
            team1 (float): SPI rank for team 1
            team2 (float): SPI rank for team 2
            winner (str): Name of the winning team of that simulation when compared

    Returns:
        spi_plots (alt.Chart): Altair chart object containing the plots for the two teams selected"""

    # rename the columns to team1, team2, winner
    spi_dist_df = spi_dist_df.rename(
        columns={spi_dist_df.columns[0]: "team1", spi_dist_df.columns[1]: "team2"}
    )

    # Create the plots
    spi_plot = (
        alt.Chart(spi_dist_df)
        .transform_fold(
            ["team1", "team2"], as_=["Team", "SPI Simulated Scores (Binned)"]
        )
        .mark_bar(opacity=0.2, binSpacing=0)
        .encode(
            alt.X(
                "SPI Simulated Scores (Binned):Q",
                bin=alt.Bin(maxbins=100),
                title="SPI Simulated Scores (Binned)",
            ),
            alt.Y("count()", stack=None),
            alt.Color("Team:N"),
        )
    )

    return spi_plot
