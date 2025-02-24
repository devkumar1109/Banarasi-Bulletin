import os
import time
import re
import json
import pymongo
from dotenv import load_dotenv
load_dotenv()

USER_AGENT = os.getenv('USER_AGENT')
project_path = "https://project1-three-omega.vercel.app/"

from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from gradio_client import Client
from PIL import Image
import cloudinary
import cloudinary.uploader

def fetch_news():
    wrapper = DuckDuckGoSearchAPIWrapper(region='in-en', time='d')
    search = DuckDuckGoSearchResults(api_wrapper=wrapper, backend = 'news', num_results=7, output_format='list')
    MONGO_URI = os.getenv('MONGO_URI')
    client = pymongo.MongoClient(MONGO_URI)
    db = client["my_articles"]
    collection = db["news_articles"]  # Collection where articles will be stored

    genres = ['sports', 'politics', 'health', 'crime', 'entertainment', 'technology']
    locations = ['Varanasi', 'Uttar Pradesh']
    news = []
    for genre in genres:
        for location in locations:
            try:
                result = search.invoke(f"{location} {genre}")
                result = [i for i in result if 'www.msn.com' not in i['link'] and 'www.business-standard.com' not in i['link']]
                article = {}
                article['date'] = result[0]['date']
                article['link'] = result[0]['link']
                article['source'] = result[0]['source']
                
                loader = WebBaseLoader(web_path=result[0]['link'])
                text = loader.load()
                
                text = re.sub(r'\s+' , ' ', text[0].page_content[:4000])
                page_content = text.strip()
                
                if len(page_content) < 20:
                    continue
                
                llm = ChatGroq(model='llama3-70b-8192', api_key='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')
                
                result_summary = llm.invoke(f"""Please extract factual, valuable and relevant news from the provided content
                                         and summarize it in 150 words.
                                    Do not skip any valuable news related information.
                                    Do not generate any extra text.
                                    <content>{page_content}</content>""")
                time.sleep(1.5)
                article['summary'] = result_summary.content
                
                result_title = llm.invoke(f"""Provide me a catchy, relevant and clever title for the following news summary of at max 10 words.
                                        Do not generate any extra text.
                                        <summary>{result_summary.content}</summary>""")
                time.sleep(1.5)
                article['title'] = result_title.content

                result_prompt = llm.invoke(f"""Give me a suitable prompt in 100 words for the provided summary so that
                                        i can use this prompt in a llm to generate a real image.
                                        Do not generate anything extra.
                                        <summary>{result_summary.content}</summary>""")
                time.sleep(1.5)
                

                image_model = Client('black-forest-labs/FLUX.1-schnell', hf_token = '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')
                result_image = image_model.predict(prompt = result_prompt.content, seed=0,randomize_seed=True,
                                                    width=512,height=288,num_inference_steps=10,api_name="/infer")
                
                
                cloudinary.config(cloud_name = "duix0mwfx", api_key = "951464569893896", api_secret = "gD6hwHlMYcT08QcYj8vnVxBJZkg", secure=True)
                upload_result = cloudinary.uploader.upload(result_image[0],public_id=result_title.content)
                article['image_url'] = upload_result["secure_url"]
                
                time.sleep(1.5)
                
                result_keywords = llm.invoke(f"""From the provided summary of a news article, give me around 15 keyowrds that are relevant, 
                                             factual and would be good to use in SEO keywords. Try to include all the small details as well. 
                                             Only generate the keywords and print them in a comma-separated format. Do not generate any other text. 
                                             <summary>{result_summary.content}</summary>""")
                time.sleep(1.5)
                article['keywords'] = result_keywords.content
                article['keywords']+= ", " + genre + ', ' + location
                
                result_hashtags =  llm.invoke(f"""From the provided summary of a news article, give me around 15 small hashtags that are relevant,
                                              factual and would be good to use with my article. Try to include all the small details as well. 
                                              Only generate the hashtags with a "#" and print them in a comma-separated format. 
                                              Do not generate any other text. 
                                              <summary>{result_summary.content}</summary>""")
                time.sleep(1.5)
                article['hashtags'] = result_hashtags.content
                article['hashtags']+= ', #' + genre + ', #' + location + ', #BanarasiBulletin'
                
                news.append(article)
                
                article_data = {
                    "title": article["title"],
                    "link": f"{project_path}/articles/{re.sub(r'[<>:"/\\|?*]', '', (article["title"].replace(" ", "_")))}/index.html",
                    "keywords": article['keywords'],
                    "image": article['image_url']
                }
                
                collection.insert_one(article_data)
                print(f"Stored in MongoDB successfully!")
               
            except Exception as e:
                print(e)
                continue
    return news

def generate_news_page(article, html_file="index.html", css_file="style.css"):
    # HTML Content with enhanced styling and hashtag section
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Banarasi Bulletin - {article['title']}</title>
    <meta name="description" content="{article['summary']}">
    <meta name="keywords" content="news, latest news, updates, {article['keywords'].lower()}">
    <meta name="author" content="Banarasi Bulletin">

    <!-- Open Graph for social media -->
    <meta property="og:title" content="{article['title']}">
    <meta property="og:description" content="{article['summary']}">
    <meta property="og:image" content="{article['image_url']}">
    <meta property="og:url" content="{article['source']}">
    <meta property="og:type" content="article">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{article['title']}">
    <meta name="twitter:description" content="{article['summary']}">
    <meta name="twitter:image" content="{article['image_url']}">

    <link rel="stylesheet" href="./style.css">
</head>
<body>
    <header>
        <h1>Banarasi Bulletin</h1>
    </header>
    <main>
        <div class="news-card">
            <img src="{article['image_url']}" alt={article['title']}>
            <div class="news-content">
                <h2>{article['title']}</h2>
                <p class="date">{article['date']}</p>
                <p class="summary">{article['summary']}</p>
                <a href="{article['link']}" target="_blank" class="source">Read full article by {article['source']}</a>
                <p class="hashtags">{article['hashtags']}</p>
            </div>
        </div>
    </main>
</body>
</html>
"""

    # CSS Content with better styling
    css_content = """body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
}

header {
    width: 100%;
    background: #2c3e50;
    color: white;
    text-align: center;
    padding: 20px 0;
    font-size: 28px;
    font-weight: bold;
    letter-spacing: 1px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

main {
    width: 90%;
    max-width: 800px;
    margin: 30px auto;
}

.news-card {
    background: white;
    border-radius: 12px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    margin-bottom: 25px;
    border: 1px solid #ddd;
    transition: transform 0.2s ease-in-out;
}

.news-card:hover {
    transform: scale(1.02);
}

.news-card img {
    width: 100%;
    height: auto;
    border-bottom: 3px solid #007bff;
}

.news-content {
    padding: 20px;
    text-align: center;
}

.news-content h2 {
    font-size: 24px;
    margin: 0 0 12px;
    color: #333;
}

.date {
    font-size: 14px;
    color: #777;
    margin-bottom: 8px;
}

.summary {
    font-size: 16px;
    color: #444;
    margin-bottom: 15px;
    line-height: 1.6;
}

.source {
    display: inline-block;
    text-decoration: none;
    background: #007bff;
    color: white;
    padding: 10px 16px;
    border-radius: 5px;
    font-size: 14px;
    transition: background 0.3s ease-in-out;
}

.source:hover {
    background: #0056b3;
}

.hashtags {
    margin-top: 15px;
    font-size: 14px;
    color: #555;
    font-style: italic;
}
"""

    # Write HTML file
    article_title = re.sub(r'[<>:"/\\|?*]', '', (article["title"].replace(" ", "_")))  # Create a safe directory name
    directory = os.path.join("public\\articles", article_title)

    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    # File paths
    html_file_path = os.path.join(directory, "index.html")
    css_file_path = os.path.join(directory, "style.css")

    # Write HTML file
    with open(html_file_path, "w") as html_f:
        html_f.write(html_content)

    # Write CSS file
    with open(css_file_path, "w") as css_f:
        css_f.write(css_content)

    print(f"Generated {html_file_path} and {css_file_path} successfully!")



news = fetch_news()

for article in news:
    article_title = re.sub(r'[<>:"/\\|?*]', '', (article["title"].replace(" ", "_")))
    directory = os.path.join("public\\articles", article_title)
    generate_news_page(article, html_file=f"{directory}/index.html", css_file=f"{directory}/style.css")
    
