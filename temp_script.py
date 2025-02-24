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
article['title'] = '''Divine From Above: Viral Aerial Video Captures Varanasi's Timeless Essence'''
article['link'] = f"{project_path}/articles/Varanasi's_Divine_Essence_Caught_on_Camera/index.html"
keywords = "news, latest news, updates, varanasi, kashi, banaras, india, holy city, aerial video, drone footage, kashi vishwanath temple, manikarnika ghat, ganga aarti, spiritual essence, divine energy, viral video, social media, indian culture, religious tourism, drone shots, ganga riverbusiness, varanasi"
keywords = [i.strip() for i in keywords.split(',')]
article['keywords'] = keywords
article['image'] = "https://res.cloudinary.com/duix0mwfx/image/upload/v1740350743/Varanasi%27s%20Divine%20Essence%20Caught%20on%20Camera.webp"

article_data = {
        "title": article["title"],
        "link": article['link'],
        "keywords": article['keywords'],
        "image": article['image']
    }
    
collection.insert_one(article_data)
print(f"Stored in MongoDB: {article_data}")