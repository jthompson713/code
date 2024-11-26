// server.js
const express = require('express');
const cors = require('cors');
const path = require('path');
const app = express();
const port = 3001;

// Middleware
app.use(cors({
    origin: ['http://localhost:3001', 'https://jthompson713.github.io/recipe-calc/'],
    methods: ['GET', 'POST'],
    credentials: true
}));
app.use(express.json());
app.use(express.static('public')); // Serve static files

// Index route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// API routes
app.get('/api/test', (req, res) => {
    res.json({ message: 'API is working' });
});

app.post('/api/calculate', (req, res) => {
    try {
        const { name, calories, protein, fats, carbs, servings } = req.body;
        
        if (!servings || servings <= 0) {
            return res.status(400).json({ error: 'Invalid servings' });
        }
        
        const result = {
            name,
            perServing: {
                calories: calories / servings,
                protein: protein / servings,
                fats: fats / servings,
                carbs: carbs / servings
            }
        };
        
        res.json(result);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Error handling
app.use((req, res) => {
    res.status(404).json({ error: 'Not found' });
});

app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Server error' });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});