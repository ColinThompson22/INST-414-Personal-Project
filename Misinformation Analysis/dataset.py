from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from Misinformation Analysis.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()

#code for setting up the birds aren't real dataset. Orignal file can be found on Kaggle as birds_arent_real_tweets.csv
import pandas as pd
df= pd.read_csv("birds_arent_real_tweets.csv")
df.head()


if __name__ == "__main__":
    app()
