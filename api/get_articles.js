const mongoose = require('mongoose');
console.log("MONGO_URI:", process.env.MONGO_URI);


mongoose.connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

export default function handler(req, res) {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.status(200).json({ message: "API is working!" });
}


const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => console.log("Connected to MongoDB"));

const articleSchema = new mongoose.Schema({
    title: String,
    link: String,
    keywords: [String]
});

const Article = mongoose.model('news_articles', articleSchema, 'news_articles');

module.exports = async (req, res) => {
    if (req.method === 'GET' && req.url.includes("/search")) {
        try {
            const query = req.query.q;
            if (!query) return res.json([]);

            const articles = await Article.find({
                keywords: { $regex: query, $options: "i" }
            });

            res.json(articles);
        } catch (err) {
            res.status(500).json({ message: err.message });
        }
    } else {
        try {
            const articles = await Article.find();
            res.json(articles);
        } catch (err) {
            res.status(500).json({ message: err.message });
        }
    }
};
