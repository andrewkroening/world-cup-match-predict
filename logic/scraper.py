"""This module is a web scraper to get the matches for today from ESPN"""

import requests
import pandas as pd


def get_matches():
    # get the json content from the espn scoreboard site
    url = "https://www.espn.com/soccer/scoreboard?league=fifa.world&xhr=1"
    r = requests.get(url)

    # filter the r object to the content level
    content = r.json()["content"]["sbData"]["events"]

    # make a dataframe from the content object
    df = pd.DataFrame(content)

    # make a team 1 column
    df["Team1"] = df["name"].apply(lambda x: x.split(" at ")[0])

    # make a team 2 column
    df["Team2"] = df["name"].apply(lambda x: x.split(" at ")[1])

    # make a date column
    df["Date"] = df["date"].apply(lambda x: x.split("T")[0])

    # filter the dataframe to the date team one and team two columns
    df = df[["Date", "Team1", "Team2"]]

    # return the dataframe
    return df
