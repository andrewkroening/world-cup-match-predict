"""This module makes an SPI distribution for the data and teams selected."""

import pandas as pd
import numpy as np


def get_spi_dist(spi_df, team1, team2):
    """Get the SPI ranks for two teams and generate distributions for 1000 simulations.

    Args:
        spi_df (pd.DataFrame): DataFrame containing SPI rankings
        team1 (str): Name of team 1
        team2 (str): Name of team 2

    Returns:
        spi_predictions (pd.DataFrame): DataFrame containing the distributions for each team with this structure:
            team1 (float): SPI rank for team 1
            team2 (float): SPI rank for team 2
            winner (str): Name of the winning team of that simulation when compared"""

    team1_spi = spi_df.loc[spi_df["name"] == team1, "spi"].tolist()[0]
    team2_spi = spi_df.loc[spi_df["name"] == team2, "spi"].tolist()[0]

    team1_sim = np.random.normal(team1_spi, 25, 1000)
    team2_sim = np.random.normal(team2_spi, 25, 1000)

    sim_mat = np.hstack((team1_sim, team2_sim))
    sim_mat = np.reshape(sim_mat, (1000, 2), order="F")

    max = np.argmax(sim_mat, axis=1)
    max = max[:, None]

    sim_mat = np.hstack((sim_mat, max))
    spi_predictions = pd.DataFrame(sim_mat, columns=[team1, team2, "winner"])
    spi_predictions = spi_predictions.replace({"winner": {0: team1, 1: team2}})

    return spi_predictions
