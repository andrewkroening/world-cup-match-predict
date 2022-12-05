"""Logic to ingest spi ranks for two teams and generate a distribution of each team's strength over 1000 simulations"""

import pandas as pd
import numpy as np


def get_spi_ranks(spi_df, team1, team2):
    """Get the SPI ranks for two teams and generate distributions

    Args:
        spi_df (pd.DataFrame): DataFrame containing SPI rankings
        team1 (str): Name of team 1
        team2 (str): Name of team 2

    Returns:
        team1_spi (np.array): Array of SPI for team 1
        team2_spi (np.array): Array of SPI for team 2"""
    pass
