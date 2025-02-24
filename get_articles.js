const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());

// Connect to MongoDB
mongoose.connect('YOUR_MONGODB_CONNECTION_STRING', { useNewUrlParser: true, useUnifiedTopology: true });

// Define a schema
const articleSchema = new mongoose.Schema({
    title: String,
    link: String
});

const Article = mongoose.model('Article', articleSchema);

// API endpoint to fetch articles
app.get('/api/articles', async (req, res) => {
    try {
        const articles = await Article.find();
        res.json(articles);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
