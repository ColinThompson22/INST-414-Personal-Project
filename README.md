# Misinformation and the Factors Leading to Spread and Belief

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         Misinformation Analysis and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── Misinformation Analysis   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes Misinformation Analysis a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```
## Description
This project was created to help analyze what factors are more likely to lead to the spread and greater belief in sources of misinformation. The data used for this project is twitter api data of user accounts that try to spread the belief that birds are not real. This project specifically uses data visualizations and hypothesis testing to analyze misinformation data, with the use of machine learning models to be used soon once I have completed sprint 3. 

## Dependicies
```
.pandas
.seaborn
.matplotlib
.pointbiserialr from scipy.stats
.mannwhitneyu from scipy.stats
```
## Setting up the enviornment
When it comes to setting the enviorment, you will first want to get the data. The link to the data is right below.
```
https://www.kaggle.com/code/venomsnake/aren-t-birds-real-examining-a-modern-conspiracy/input
```
After downloading the dataset you will want to read this dataset into your porgram. The code to do this is below.
```
import pandas as pd
df= pd.read_csv("birds_arent_real_tweets.csv")
df.head()
```
Rgus shiould help you set up the enviornment to process the data and run the visualizations and tests for this project.

## Running the Data Processing Pipeline
When it first comes to processing the data you will first want to search for na values. You can easily find na values on kaggle where it is listed in the dataset. You will then want to search for outliers, which you can do with the code below.
```
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(x=df["user_followers"])
plt.title("followers Boxplot (Detecting Outliers)")
plt.show()
```
```
sns.boxplot(x=df["user_friends"])
plt.title("friends Boxplot (Detecting Outliers)")
plt.show()
```
```
sns.boxplot(x=df["favorites"])
plt.title("favorites Boxplot (Detecting Outliers)")
plt.show()
```
If outliers are found, you can run this code that will help limit more extreme outliers.
```
favorite_q1= df["favorites"].quantile(0.25)
favorite_q3= df["favorites"].quantile(0.75)
favorite_iqr= favorite_q3-favorite_q1
favorite_lowerbound= favorite_q1-1.5*favorite_iqr
favorite_upperbound= favorite_q3+1.5*favorite_iqr
df= df[(df["favorites"] >= favorite_lowerbound) & (df["favorites"] <= favorite_upperbound)]
sns.boxplot(x=df["favorites"])
plt.title("favorites Boxplot (Detecting Outliers)")
plt.show()
```
```
friend_q1= df["user_friends"].quantile(0.25)
friend_q3= df["user_friends"].quantile(0.75)
friend_iqr= friend_q3-friend_q1
friend_lowerbound= friend_q1-1.5*friend_iqr
friend_upperbound= friend_q3+1.5*friend_iqr
df= df[(df["user_friends"] >= friend_lowerbound) & (df["user_friends"] <= friend_upperbound)]
sns.boxplot(x=df["user_friends"])
plt.title("friends Boxplot (Detecting Outliers)")
plt.show()
```
```
follower_q1= df["user_followers"].quantile(0.25)
follower_q3= df["user_followers"].quantile(0.75)
follower_iqr= follower_q3-follower_q1
follower_lowerbound= follower_q1-1.5*follower_iqr
follower_upperbound= follower_q3+1.5*follower_iqr
df= df[(df["user_followers"] >= follower_lowerbound) & (df["user_followers"] <= follower_upperbound)]
sns.boxplot(x=df["user_followers"])
plt.title("followers Boxplot (Detecting Outliers)")
plt.show()
```
After outliers are all processed out you will need to check for incosistiences in the data. You can do that using the code below.
```
acc_char_vars= df.select_dtypes(include=["object"])
for col in acc_char_vars.columns:
  display(acc_char_vars[col].value_counts().reset_index())
```
After the data is processed you can start the model evaluation process
## Model Evaluation
Coming Soon. No model was created in sprint 2
# Reproducing Results
To reproduce my visualizations and test results, you should start by checkin the basic summar staistics of your ata. You can do this through the code below
```
df.describe()
```
You can then start creating visualizations of important data points. he code used to create the histogram, regression plot, and heatmap for my own data visualizations is listed below.
```
plt.figure(figsize=(8, 5))
sns.histplot(data= df, x= "user_followers", bins= 20, color= "green")
plt.title("follower Distribution")
plt.xlabel("follower count")
plt.ylabel("post frequency")
plt.show()
```
```
plt.figure(figsize=(8, 5))
sns.regplot(data= df, x= "favorites", y= "user_followers", color= "blue")
plt.title("Relationship Between followers and favorites")
plt.xlabel("favorites")
plt.ylabel("followers")
plt.show()
```
```
acc_numeric= df.select_dtypes(include=["number"])
sns.heatmap(acc_numeric.corr(), annot= True, cmap= "coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```
Next, you will also want to run hypothesis tests to help you analyze interesting data points. The code for the bi serial test and the Mann Whitney U test I ran for my project are listed below.
```
from scipy.stats import mannwhitneyu
verified_users = df[df['user_verified'] == 1]['user_followers']
non_verified_users = df[df['user_verified'] == 0]['user_followers']
stat, p_value = mannwhitneyu(verified_users, non_verified_users, alternative='two-sided')
print(f"Test statistic: {stat}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("There is a significant difference between verified and non-verified users' followers.")
else:
    print("There is no significant difference between verified and non-verified users' followers.")
```
```
from scipy.stats import pointbiserialr
correlation, p_value = pointbiserialr(df['user_verified'], df['user_followers'])
print(f"Point-biserial correlation: {correlation}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    if correlation > 0:
        print("There is a significant positive correlation: Verified users tend to have more followers.")
    elif correlation < 0:
        print("There is a significant negative correlation: Verified users tend to have fewer followers.")
    else:
        print("There is no significant correlation.")
else:
    print("There is no significant correlation between being verified and the number of followers.")
```
Once this is done, you have successfully analyzed the data and should have achieved the same results as myself. More information coming soon with Sprint 3. 


--------

