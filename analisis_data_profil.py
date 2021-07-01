import pandas as pd
import datetime
import numpy as np
import tweepy
from time import sleep
import csv
from datetime import datetime, date, time, timedelta
import re
import numpy as np

def preprocess(df):
        train3 = pd.DataFrame(df)
        train3 = train3.drop_duplicates(keep='first', inplace=False)
        train3['Created_at']= pd.to_datetime(train3['Created_at'])
        now = pd.Timestamp('now')
        train3['age_in_days'] = (now - train3['Created_at']).dt.days
        train3["Created_at"]= pd.to_datetime(train3["Created_at"]) 
        train3['ratio statuses_count_per_age']=train3['Statuses_count']/train3['age_in_days']
 #Number of favourites/age
        train3['ratio favorites_per_age']=train3['Favorites_count']/train3['age_in_days']
        #Ratio friends/follower
        train3['ratio_friends_per_followers']=train3['Friends_count']/train3['Followers_count']
        train3['Description'].fillna('x', inplace = True)
        train3['length_of_bio']=train3['Description'].str.len()
        train3['reputation']= train3['Followers_count']/(train3['Followers_count']+ train3['Friends_count'])
        train3.drop(['Geo_enabled','Created_at'], axis=1,inplace=True)
        
        train3['URL'] = pd.notnull(train3['URL']) 
        train3['Location']=pd.notnull(train3['Location'])
        train3['contains_bot_name']=train3['Description'].str.contains("\b(bot|b0t|updates|hourly|automatically|generating|generated|every|computer-generated|twitterbot|automated|FakeBots|')\b|Bots", 
                                                                        flags=re.IGNORECASE, 
                                                                        regex=True)
        train3['contains_bot_name'].fillna(0).astype(bool).sum(axis=0)
        train3.drop(['Name','Description'], inplace=True, axis=1)
        train3["length_of_bio"].fillna(0, inplace = True) 
        train3["reputation"].fillna(0, inplace = True) 
        train3["contains_bot_name"].fillna(False, inplace=True)
        train3.replace(np.inf, 0)
        train3.replace(-np.inf, 0)

        train3=train3.replace([np.inf, -np.inf], np.nan)
        train3=train3.replace([np.inf, -np.inf], np.nan).dropna(how="all")
        train3 = train3.fillna(train3.mean())

