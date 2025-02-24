# Banarasi Bulletin

## 📰 Overview
Banarasi Bulletin is an automated news aggregation and summarization platform that scrapes news articles related to different genres from **Varanasi** and **Uttar Pradesh** using **DuckDuckGo Search** and **LangChain WebBaseLoader**. The scraped articles are then processed using **AI-generated summaries** and **titles**, along with an AI-generated image stored on **Cloudinary**. These articles are displayed on an individual blog webpage, stored in **MongoDB**, and served through a globally deployed website on **Vercel**.

This project features an automated workflow using **GitHub Actions**, ensuring that the news articles are updated every **8 hours**.

---

## 🚀 Features
- **Automated News Scraping**: Uses **DuckDuckGo Search** and **LangChain WebBaseLoader** to scrape news articles.
- **AI-Powered Summarization & Title Generation**: Summarizes scraped content and generates meaningful titles.
- **Cloud-Based Image Generation**: Uses the generated summary to create an AI-powered news thumbnail stored in **Cloudinary**.
- **MongoDB Integration**: Stores summarized articles, metadata, and generated assets in **MongoDB Atlas**.
- **Dynamic Blog Webpages**: Each article has an individual blog page generated dynamically and stored in the `public/articles_hindi/` directory.
- **Homepage with Sidebar & Search**:
  - Fetches article links dynamically from **MongoDB**.
  - Sidebar allows genre selection for filtering articles.
  - Search bar enables keyword-based news retrieval.
- **Global Deployment on Vercel**: Ensures high availability and accessibility worldwide.
- **Automated CI/CD Workflow**: Uses **GitHub Actions** with a YAML configuration to update the system **every 8 hours**, ensuring the latest news is always available.

---

## 🏗️ Tech Stack
### **Backend & Data Processing**
- **Python** (For scraping, summarization, and storage)
- **LangChain WebBaseLoader** (For extracting article content)
- **DuckDuckGo Search API** (For fetching news links)
- **Cloudinary** (For AI-generated image storage)
- **MongoDB Atlas** (For storing articles & metadata)

### **Frontend & Deployment**
- **HTML, CSS, JavaScript** (For dynamic webpage rendering)
- **Node.js & Express.js** (For API endpoints & database interaction)
- **Vercel** (For global deployment)

### **Automation & DevOps**
- **GitHub Actions** (For CI/CD automation)
- **YAML Configuration** (For scheduled updates every 8 hours)

---

## 📂 Project Structure
```
Banarasi-Bulletin/
│-- public/
│   ├── articles_hindi/  # Generated individual article pages
│-- backend/
│   ├── scraper.py  # News scraping and summarization script
│   ├── generate_pages.py  # Generates blog pages dynamically
│   ├── db.py  # MongoDB connection and operations
│-- frontend/
│   ├── index.html  # Homepage with search & sidebar
│   ├── styles.css  # Styling for the website
│   ├── scripts.js  # Handles search & API calls
│-- .github/
│   ├── workflows/
│       ├── update_news.yml  # GitHub Actions automation (runs every 8 hours)
│-- README.md  # Project documentation
│-- requirements.txt  # Dependencies
│-- package.json  # Node.js dependencies for the API
│-- vercel.json  # Vercel deployment configuration
```

---

## 📌 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/banarasi-bulletin.git
cd banarasi-bulletin
```

### **2️⃣ Install Dependencies**
#### **Backend (Python)**
```sh
pip install -r requirements.txt
```
#### **Frontend & API (Node.js)**
```sh
npm install
```

### **3️⃣ Set Up Environment Variables**
Create a `.env` file and add the required API keys and database credentials:
```env
MONGO_URI=your_mongodb_connection_string
CLOUDINARY_URL=your_cloudinary_api_url
DDG_SEARCH_API_KEY=your_duckduckgo_api_key
```

### **4️⃣ Run Locally**
#### **Start Backend**
```sh
python backend/scraper.py
```
#### **Start Frontend**
```sh
npm run dev
```
Visit `http://localhost:3000` to see the homepage.

---

## 🔄 CI/CD Automation (GitHub Actions)
This project is configured with **GitHub Actions** to automate news updates every **8 hours**.

### **Workflow Overview**
- **Trigger:** Runs automatically every **8 hours**.
- **Jobs:**
  - Fetch latest news articles.
  - Summarize content & generate images.
  - Store data in **MongoDB**.
  - Deploy updated content to **Vercel**.

### **YAML Configuration (`.github/workflows/update_news.yml`)**
```yaml
name: Update News Articles
on:
  schedule:
    - cron: '0 */8 * * *'  # Runs every 8 hours
  workflow_dispatch:

jobs:
  update-news:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run scraper
        run: python backend/scraper.py
      - name: Commit and push changes
        run: |
          git config --global user.name 'github-actions'
          git config --global user.email 'github-actions@github.com'
          git add .
          git commit -m 'Auto-update news articles'
          git push
      - name: Deploy to Vercel
        run: vercel --prod
```

---

## 🌎 Deployment on Vercel
This project is deployed globally using **Vercel**, ensuring fast content delivery and seamless updates.

### **Vercel Configuration (`vercel.json`)**
```json
{
  "builds": [{ "src": "backend/api.js", "use": "@vercel/node" }],
  "routes": [{ "src": "/(.*)", "dest": "backend/api.js" }]
}
```

### **Deploy Manually**
```sh
vercel --prod
```

---

## 📌 Future Enhancements
- ✅ Add multilingual support (Hindi & English articles)
- ✅ Improve AI-generated summaries using fine-tuned models
- ✅ Enhance UI with better filters and categorization
- ✅ Implement a user-authenticated dashboard for contributors

---

## 📝 License
This project is **open-source** and available under the **MIT License**.

---

## 👨‍💻 Author
Developed by **[Your Name]** 🚀 | Contact: [your-email@example.com]

