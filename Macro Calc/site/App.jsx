// App.jsx
import { useState } from 'react';
import './App.css';

function App() {
  const [recipe, setRecipe] = useState({
    name: '',
    calories: '',
    protein: '',
    fats: '',
    carbs: '',
    servings: ''
  });
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost:3000/calculate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(recipe)
    });
    const data = await response.json();
    setResult(data);
  };

  return (
    <div className="container">
      <h1>Recipe Calculator</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Recipe Name"
          value={recipe.name}
          onChange={e => setRecipe({...recipe, name: e.target.value})}
        />
        {/* Add other inputs similarly */}
        <button type="submit">Calculate</button>
      </form>
      
      {result && (
        <div className="result">
          <h2>{result.name}</h2>
          <p>Per Serving:</p>
          <ul>
            <li>Calories: {result.perServing.calories.toFixed(1)}</li>
            <li>Protein: {result.perServing.protein.toFixed(1)}g</li>
            <li>Fats: {result.perServing.fats.toFixed(1)}g</li>
            <li>Carbs: {result.perServing.carbs.toFixed(1)}g</li>
          </ul>
        </div>
      )}
    </div>
  );
}