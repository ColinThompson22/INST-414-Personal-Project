from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from Misinformation Analysis.config import FIGURES_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
#file setup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df= pd.read_csv("birds_arent_real_tweets.csv")
#user_followers boxplot setup
sns.boxplot(x=df["user_followers"])
plt.title("followers Boxplot (Detecting Outliers)")
plt.show()
#user_friends boxplot setup
sns.boxplot(x=df["user_friends"])
plt.title("friends Boxplot (Detecting Outliers)")
plt.show()
#favorites boxplot setup
sns.boxplot(x=df["favorites"])
plt.title("favorites Boxplot (Detecting Outliers)")
plt.show()
#favorites boxplot after IQR method
favorite_q1= df["favorites"].quantile(0.25)
favorite_q3= df["favorites"].quantile(0.75)
favorite_iqr= favorite_q3-favorite_q1
favorite_lowerbound= favorite_q1-1.5*favorite_iqr
favorite_upperbound= favorite_q3+1.5*favorite_iqr
df= df[(df["favorites"] >= favorite_lowerbound) & (df["favorites"] <= favorite_upperbound)]
sns.boxplot(x=df["favorites"])
plt.title("favorites Boxplot (Detecting Outliers)")
plt.show()
#user friends boxplot after IQR method
friend_q1= df["user_friends"].quantile(0.25)
friend_q3= df["user_friends"].quantile(0.75)
friend_iqr= friend_q3-friend_q1
friend_lowerbound= friend_q1-1.5*friend_iqr
friend_upperbound= friend_q3+1.5*friend_iqr
df= df[(df["user_friends"] >= friend_lowerbound) & (df["user_friends"] <= friend_upperbound)]
sns.boxplot(x=df["user_friends"])
plt.title("friends Boxplot (Detecting Outliers)")
plt.show()
#user_followers boxplot after IQR method
follower_q1= df["user_followers"].quantile(0.25)
follower_q3= df["user_followers"].quantile(0.75)
follower_iqr= follower_q3-follower_q1
follower_lowerbound= follower_q1-1.5*follower_iqr
follower_upperbound= follower_q3+1.5*follower_iqr
df= df[(df["user_followers"] >= follower_lowerbound) & (df["user_followers"] <= follower_upperbound)]
sns.boxplot(x=df["user_followers"])
plt.title("followers Boxplot (Detecting Outliers)")
plt.show()
#User_followers histogram distribution setup
plt.figure(figsize=(8, 5))
sns.histplot(data= df, x= "user_followers", bins= 20, color= "green")
plt.title("follower Distribution")
plt.xlabel("follower count")
plt.ylabel("post frequency")
plt.show()
#user_follower and favorites regression plot setup
plt.figure(figsize=(8, 5))
sns.regplot(data= df, x= "favorites", y= "user_followers", color= "blue")
plt.title("Relationship Between followers and favorites")
plt.xlabel("favorites")
plt.ylabel("followers")
plt.show()
#dataset correlation heatmap setup
acc_numeric= df.select_dtypes(include=["number"])
sns.heatmap(acc_numeric.corr(), annot= True, cmap= "coolwarm")
plt.title("Correlation Heatmap")
plt.show()



if __name__ == "__main__":
    app()
