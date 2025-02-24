# Banarasi Bulletin - Automated News Aggregator

## 📰 Overview
Banarasi Bulletin is an automated news aggregation and blogging platform focused on curating and summarizing news from Varanasi and Uttar Pradesh. It scrapes articles from various sources, processes them using AI, and generates structured blog pages with SEO optimization. The website is globally deployed on Vercel, with an automated workflow ensuring continuous updates every 8 hours.

## 🚀 Features
- **News Scraping**: Uses DuckDuckGo search along with LangChain's WebBaseLoader to scrape news articles.
- **AI-Powered Summarization**: Utilizes an LLM model via Groq API to summarize news content and generate optimized titles.
- **Image Generation**: Generates relevant images based on the summary and uploads them to Cloudinary.
- **Dynamic Blog Generation**: Automatically creates blog web pages for each article and stores them in MongoDB.
- **Homepage with Filtering**:
  - Displays all available articles fetched from MongoDB.
  - **Sidebar with Genre Selection**: Allows filtering articles based on predefined news genres (Crime, Politics, Sports, Education, Entertainment, Technology).
  - **Search Bar**: Enables users to search articles based on keywords present in the MongoDB schema.
- **SEO Optimization**:
  - Generates keywords and hashtags automatically for better discoverability.
  - Implements SEO metadata techniques including Open Graph, Twitter Card, and meta descriptions.
- **Global Deployment**: Hosted on **Vercel**, accessible worldwide.
- **Automated Workflow**:
  - Configured with GitHub Actions to fetch new articles and update the website every **8 hours**.
  - A YAML configuration ensures seamless automated updates.

## 🏗️ Tech Stack
- **Backend**: Python
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB Atlas
- **AI & NLP**: Groq API, LangChain, HuggingFace Spaces
- **Web Scraping**: DuckDuckGo Search API, WebBaseLoader
- **Image Processing**: Cloudinary API
- **Hosting & Deployment**: Vercel, GitHub Actions

## 📂 Project Structure

Banarasi-Bulletin/
│-- public/
│   ├── articles/  # Generated individual article pages
|   ├── index.html  # Homepage with search & sidebar
│   ├── styles.css  # Styling for the website
│   ├── scripts.js  # Handles search & API calls
│-- english_blogs.py  # News scraping and summarization script
│-- .github/
│   ├── workflows/
│       ├── update_news.yml  # GitHub Actions automation (runs every 8 hours)
│-- README.md  # Project documentation
│-- requirements.txt  # Dependencies
│-- package.json  # Node.js dependencies for the API
│-- vercel.json  # Vercel deployment configuration
│-- package-lock.json
│-- .gitignore
│-- .env
│-- node_modules/
│-- api/
│   ├── get_articles.js

## Automation Setup
GitHub Actions is configured to update the website **every 8 hours** by running the scraping and content generation script. The YAML workflow file ensures a fully automated process without manual intervention.

## Future Enhancements
- **User Authentication**: Enable user accounts for personalized news feeds.
- **Comments & Engagement**: Allow users to comment and interact with news articles.
- **Multilingual Support**: Expand content generation to include multiple languages.

## Contributing
We welcome contributions! Feel free to fork the repo, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License.

---
🚀 **Banarasi Bulletin - Keeping You Updated with the Latest News from Varanasi & UP!**

