import os
import json
import pymongo
from dotenv import load_dotenv

load_dotenv()

# MongoDB Setup
MONGO_URI = os.getenv('MONGODB_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client["my_articles"]
collection = db["news_articles"]  # Collection where articles will be stored

article = {}
article['title'] = "BJP Criticizes Opposition Over Maha Tragedy"
article['link'] = "https://timesofindia.indiatimes.com/city/varanasi/oppn-seeking-political-gain-in-maha-kumbh-tragedy-bjp/articleshow/118511161.cms"
keywords = 'news, latest news, updates, maha kumbh tragedy, bjp, sudhanshu trivedi, samajwadi party, akhilesh yadav, covid-19 vaccines, ram lalla consecration, union budget, indian economy, cultural awakening, us deportation, panama, illegal immigration, caa, nrcpolitics, varanasi'.split(',')
keywords = [i.strip() for i in keywords]
article['keywords'] = keywords

article_data = {
        "title": article["title"],
        "link": article['link'],
        "keywords": article['keywords']
    }
    
collection.insert_one(article_data)
print(f"Stored in MongoDB: {article_data}")