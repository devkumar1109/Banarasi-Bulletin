const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());

// MongoDB Connection
mongoose.connect('YOUR_MONGODB_CONNECTION_STRING', { useNewUrlParser: true, useUnifiedTopology: true });

const articleSchema = new mongoose.Schema({
    title: String,
    link: String,
    keywords: [String]
});

const Article = mongoose.model('Article', articleSchema);

// API Endpoint: Fetch All Articles
app.get('/api/articles', async (req, res) => {
    try {
        const articles = await Article.find();
        res.json(articles);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// API Endpoint: Search Articles by Keywords
app.get('/api/search', async (req, res) => {
    try {
        const query = req.query.q;
        if (!query) {
            return res.json([]);
        }

        // Find articles where keywords match the search query (case-insensitive)
        const articles = await Article.find({
            keywords: { $regex: query, $options: "i" }
        });

        res.json(articles);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
