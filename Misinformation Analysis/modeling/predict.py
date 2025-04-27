from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from Misinformation Analysis.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
#Code for setup
import pandas as pd
df= pd.read_csv("birds_arent_real_tweets.csv")


if __name__ == "__main__":
    app()
