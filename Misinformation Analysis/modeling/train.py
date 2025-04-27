from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from Misinformation Analysis.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
#code for setup
import pandas as pd
df= pd.read_csv("birds_arent_real_tweets.csv")
#Code for setting up poisson model
import statsmodels.api as sm
from statsmodels.formula.api import poisson
df['user_verified'] = df['user_verified'].astype(int)
poisson_model = poisson('favorites ~ user_verified', data=df).fit()



if __name__ == "__main__":
    app()
