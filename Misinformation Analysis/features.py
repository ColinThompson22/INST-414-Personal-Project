from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from Misinformation Analysis.config import PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
#code setup
import pandas as pd
df= pd.read_csv("birds_arent_real_tweets.csv")
#code for using IQR method on user_follower
follower_q1= df["user_followers"].quantile(0.25)
follower_q3= df["user_followers"].quantile(0.75)
follower_iqr= follower_q3-follower_q1
follower_lowerbound= follower_q1-1.5*follower_iqr
follower_upperbound= follower_q3+1.5*follower_iqr
df= df[(df["user_followers"] >= follower_lowerbound) & (df["user_followers"] <= follower_upperbound)]
#code for using IQR method on user_friends
riend_q1= df["user_friends"].quantile(0.25)
friend_q3= df["user_friends"].quantile(0.75)
friend_iqr= friend_q3-friend_q1
friend_lowerbound= friend_q1-1.5*friend_iqr
friend_upperbound= friend_q3+1.5*friend_iqr
df= df[(df["user_friends"] >= friend_lowerbound) & (df["user_friends"] <= friend_upperbound)]
code for using IQR method on favorites
favorite_q1= df["favorites"].quantile(0.25)
favorite_q3= df["favorites"].quantile(0.75)
favorite_iqr= favorite_q3-favorite_q1
favorite_lowerbound= favorite_q1-1.5*favorite_iqr
favorite_upperbound= favorite_q3+1.5*favorite_iqr
df= df[(df["favorites"] >= favorite_lowerbound) & (df["favorites"] <= favorite_upperbound)]
#Code for user_verified data into numeric instead of boolean for poisson modeling
df['user_verified'] = df['user_verified'].astype(int)

if __name__ == "__main__":
    app()
