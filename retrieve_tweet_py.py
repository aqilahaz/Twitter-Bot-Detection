import tweepy
from tweepy import Cursor
import unicodecsv
import numpy
from unidecode import unidecode

# Authentication and connection to Twitter API.
consumer_key ='-'
consumer_secret ='-'
access_key ='-'
access_secret ='-'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def download_user(dl_user):
        with open('coba.csv', 'wb') as file:
            writer = unicodecsv.writer(file, delimiter = ',', quotechar = '"')
        # Write header row.
        
            writer.writerow(["id",
                        "id_str",
                        "Name",
                        "Username",
                        "Followers_count",
                        "Listed_count",
                        "Friends_count",
                        "Favorites_count",
                        "Created_at",
                        "Verified",
                        "Default_profile",
                        "Default_profile_image",
                        "Location",
                        "Statuses_count",
                        "Description",
                        "URL",
                        "Geo_enabled"
                    ])
            
            user_obj = api.get_user(dl_user)
                        # Gather info specific to the current user.
            user_info = [user_obj.name,
                            user_obj.screen_name,
                            user_obj.followers_count,
                            user_obj.listed_count,
                            user_obj.friends_count,
                            user_obj.favourites_count,
                            user_obj.created_at,
                            user_obj.verified,
                            user_obj.default_profile,
                            user_obj.default_profile_image,
                            user_obj.location,
                            user_obj.statuses_count,
                            user_obj.description,
                            user_obj.url,
                            user_obj.geo_enabled]

            
            writer.writerow(user_info)

            # Show progress.
            print("Wrote tweets by %s to CSV." % dl_user)

download_user('jokowi')