# Welcome to TONS OF FUN

### The *TOtally Not SeriOus FiFa oUtcome predictioN* tool for the 2022 World Cup

[![CI/CD Pipeline to Docker Hub](https://github.com/andrewkroening/tons-of-fun/actions/workflows/docker_push.yml/badge.svg)](https://github.com/andrewkroening/tons-of-fun/actions/workflows/docker_push.yml)

#### Overview

This was a project for an engineering, not a statistics class. As such, the predictions are somewhat engineered to be serious, but we really used this opportunity to exercise several other things. 

Check out the youtube demo here.

Below is an architecture schematic of this project:

<img src="https://github.com/andrewkroening/tons-of-fun/blob/619d467cbac8841a057a47f90ce5362fc47b3e70/project_sketch.png" alt="Project Overview" width="800"/>

There are four modules that support the app:

* A web scraper to get today's games from ESPN (this was easier than other scrappy/beautiful soup options we explored)

* An SPI generator for 1000 matches between two teams

* An SPI plot generator that shows a layered histogram of those simulation outcomes

* An SPI winner logic tool that returns a string describing the simulation

Those inputs are fed to a streamlit app script which is deployed two ways.

#### Deployment

We use GitHub actions to push our app two places:

* It is deployed through the [Streamlit service](https://tons-of-fun.streamlit.app) and can be consumed directly there

* We also build a Dockerfile that is automatically pushed to Docker Hub, then on to Azure where it is sent to a Container Instance and a Web App

*We don't have public endpoints on the Azure portion enabled. It was redundant, we just wanted to see if we could do it.*

#### Credits:

* Dany Jabban

* Sukhpreet Sahota

* Paul McKee

* Andrew Kroening
