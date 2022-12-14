# Welcome to this Totally Not Serious FIFA Outcome Prediction Tool for the 2022 World Cup

### We call it TONS OF FUN
[![CI/CD Pipeline to Docker Hub](https://github.com/andrewkroening/tons-of-fun/actions/workflows/docker_push.yml/badge.svg)](https://github.com/andrewkroening/tons-of-fun/actions/workflows/docker_push.yml)

#### Overview

This was a project for data engineering, not a statistics class. As such, the predictions are engineered to be somewhat serious, but we really used this opportunity to exercise several other things and try some new stuff. Check out the youtube demo here.

It's important to point out that this tool will work for matches outside the 2022 World Cup. If you want to simulate any matches, navigate to the [Streamlit App Landing](https://tons-of-fun.streamlit.app/) and run some simulated matches of your own!

Below is an architectural schematic of this project:

<img src="https://github.com/andrewkroening/tons-of-fun/blob/619d467cbac8841a057a47f90ce5362fc47b3e70/project_sketch.png" alt="Project Overview" width="800"/>

#### Data

We are accessing data from two locations:

* [538's Soccer Power Index](https://projects.fivethirtyeight.com/soccer-api/international/spi_global_rankings_intl.csv) - The Soccer Power Index, or SPI, is a calculated relative strength for each international team. We stream this data live each time the app is loaded and use it as the base for many of the actions in our logic tools.

* [ESPN's World Cup Scoreboard](https://www.espn.com/soccer/scoreboard?league=fifa.world&xhr=1) - JSON source data for the scoreboard web page available on ESPN. We add the `&xhr=1` to the end of the address to access the JSON, which significantly reduces the complexity of the logic required.

#### Logic

Four modules support the app:

* `scraper.py` - A web scraper to get today's games from ESPN (this was easier than other scrappy/beautiful soup options we explored). We pull the JSON data behind the scoreboard web page and then query for a specific location where the score data is scored. That is transformed slightly as it is ingested into a data frame and passed to the main app.

* `spi_dist.py` - A generator for 1000 matches between two teams. It uses the SPI dataset as its reference and calculates the SPI for each team over the 1000-match range. We introduced a variance factor of 25 to the simulations, which is pretty significant given the range of SPI values is 0-100. This is a good amount of variance because it allows for more upsets or surprises. The simulator tends to be 'less sure' than other popular prediction tools.

* `spi_plots.py` - A plot generator that shows a layered histogram of the simulation outcomes. This tool is relatively straightforward, it just needs the outputs from `spi_dist.py`, and it will do the necessary transformations to get to the plot outcome. We used Altair for this function and are generally pleased, although Altair has a few limitations in what we could and could not customize.

* `spi_winner` - A logic tool that returns a string describing the simulation. It uses the `spi_dist.py` output to determine which team won which percentage of the simulations and then returns the most probable winner.

#### Main App

`streamlit_app.py`

#### Deployment

We use GitHub actions to push our app to two places:

* It is deployed through the [Streamlit service](https://tons-of-fun.streamlit.app) and can be consumed directly there

* We also build a Dockerfile that is automatically pushed to Docker Hub, then on to Azure where it is sent to a Container Instance and a Web App

*We don't have public endpoints on the Azure portion enabled. It was redundant, we just wanted to see if we could do it.*

#### References

#### Credits
* Dany Jabban
* Sukhpreet Sahota
* Paul McKee
* Andrew Kroening
