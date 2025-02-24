import os
import json
import pymongo
from dotenv import load_dotenv

load_dotenv()

project_path = "https://project1-three-omega.vercel.app/"

# MongoDB Setup
MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client["my_articles"]
collection = db["news_articles"]  # Collection where articles will be stored

article = {}
article['title'] = '''Love Turns to Blood: Fatal Affair at Maha Kumbh'''
article['link'] = f"{project_path}/articles/Man_Kills_Wife_During_Kumbh_Tour/index.html"
keywords = "news, latest news, updates, maha kumbh tour, alleged affair, throat slit, knife, murder, blood-stained clothes, dustbin, crime confession, missing person, wife killed, husband accused, domestic violence, marital dispute, kumbh festival, murder weapon, throat slashingcrime, uttar pradesh"
keywords = [i.strip() for i in keywords.split(',')]
article['keywords'] = keywords
article['image'] = "https://res.cloudinary.com/duix0mwfx/image/upload/v1740350712/Man%20Kills%20Wife%20During%20Kumbh%20Tour.webp"

article_data = {
        "title": article["title"],
        "link": article['link'],
        "keywords": article['keywords'],
        "image": article['image']
    }
    
collection.insert_one(article_data)
print(f"Stored in MongoDB: {article_data}")