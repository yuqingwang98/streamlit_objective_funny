# streamlit_objective_funny
**Work In Progress**

This is the front-end of [Objectively Funny](https://github.com/rmelbardis/ObjectivelyFunny).

## Link to Application
https://objectively-funny.streamlit.app/

# Objectively Funny

This project was made by 4 Le Wagon Data Science students as our final project.
We have sourced and processed a wide range of stand-up scripts to analyse comedians and make our own comedy.

## Description

* Constructed a scraper to source and clean 3.6 million words of stand-up comedy from a variety of online sources using BeautifulSoup, Requests, and Pandas.
* Carried out a machine learning analysis using a Latent Dirichlet Allocation (LDA) on the processed dataset and used wordclouds to visualise results.
* Finetuned a bot using GPT2 ([gpt-2-simple](https://github.com/minimaxir/gpt-2-simple), credit: Max Woolf) on the subset of female comedian scripts & generted entirely original stand-up comedy material from only a few words of text input. Created an API for the bot using FastAPI, Docker and Google Cloud Run.
* Integrated and published the completed project on a public site using Streamlit.

Note: Our joke-generating API is no longer running, but you can view here the word clouds of stand-up comedy themes, and a few jokes our bot generated before.

## Running locally

make install_requirements <br>
make streamlit
