// server.js
const express = require('express');
const cors = require('cors');
const path = require('path');
const app = express();
const port = 3001;

// Debug logging middleware
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
});

// CORS configuration
app.use(cors({
    origin: process.env.NODE_ENV === 'production' 
        ? ['https://jthompson713.github.io/recipe-calc/', 'https://www.jthompson713.github.io/recipe-calc/']
        : '*',
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

// Calculation endpoint with validation
app.post('/api/calculate', (req, res) => {
    console.log('Received calculation request:', req.body);

    try {
        const { name, calories, protein, fats, carbs, servings } = req.body;

        // Validate inputs
        if (!name || !calories || !protein || !fats || !carbs || !servings) {
            console.log('Missing required fields');
            return res.status(400).json({ 
                error: 'All fields are required',
                received: req.body 
            });
        }

        // Validate numbers
        if (servings <= 0) {
            return res.status(400).json({ error: 'Servings must be greater than 0' });
        }

        const result = {
            name,
            servings,
            perServing: {
                calories: Number((calories / servings).toFixed(1)),
                protein: Number((protein / servings).toFixed(1)),
                fats: Number((fats / servings).toFixed(1)),
                carbs: Number((carbs / servings).toFixed(1))
            }
        };

        console.log('Calculation result:', result);
        res.json(result);

    } catch (error) {
        console.error('Calculation error:', error);
        res.status(500).json({ 
            error: 'Calculation failed', 
            details: error.message 
        });
    }
});

// Error handlers
app.use((req, res) => {
    console.log('404 - Route not found:', req.url);
    res.status(404).json({ error: 'Route not found' });
});

app.use((err, req, res, next) => {
    console.error('Server error:', err);
    res.status(500).json({ 
        error: 'Calculation failed',
        message: process.env.NODE_ENV === 'production' 
            ? 'An error occurred' 
            : err.message
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});