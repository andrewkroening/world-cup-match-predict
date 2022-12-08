"""Function to caluclate the winner of a match based on the SPI distribution of the match"""


def spi_winner(spi_dist_df, team1name, team2name):

    # calculate the winner of the simulation
    team1_wins = spi_dist_df[spi_dist_df["winner"] == team1name].shape[0]
    team2_wins = spi_dist_df[spi_dist_df["winner"] == team2name].shape[0]

    if team1_wins > team2_wins:
        perc_win = round(team1_wins / spi_dist_df.shape[0] * 100, 2)
        winner = (
            "The winner is "
            + str(team1name)
            + " with "
            + str(perc_win)
            + "% of the simulations"
        )
    elif team1_wins == team2_wins:
        winner = (
            "The match is a draw based on 5000 simulations. We don't believe it either."
        )
    else:
        perc_win = round(team2_wins / spi_dist_df.shape[0] * 100, 2)
        winner = (
            "The winner is "
            + str(team2name)
            + " with "
            + str(perc_win)
            + "% of the simulations"
        )

    return winner
