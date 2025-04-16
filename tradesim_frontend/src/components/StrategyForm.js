import React, { useState } from 'react';
import API from '../api';

export default function StrategyForm() {
  const [name, setName] = useState('');
  const [symbol, setSymbol] = useState('');
  const [price, setPrice] = useState('');
  const [comparison, setComparison] = useState('lt');
  const [status, setStatus] = useState('');

  const handleSave = async () => {
    const user_id = localStorage.getItem('user_id');
    const conditions = {
      symbol: symbol.toUpperCase(),
      price: parseFloat(price),
      comparison
    };

    try {
      const res = await API.post('/strategy/save', {
        user_id,
        name,
        conditions
      });
      setStatus('Strategy saved successfully!');
    } catch (err) {
      console.error(err);
      setStatus(err.response?.data?.error || 'Failed to save strategy');
    }
  };

  return (
    <div className="bg-white shadow-md rounded p-4">
      <h2 className="text-xl font-semibold mb-3">🤖 Strategy Builder</h2>
      <input className="border p-2 mb-2 w-full" placeholder="Strategy Name" value={name} onChange={e => setName(e.target.value)} />
      <input className="border p-2 mb-2 w-full" placeholder="Symbol (e.g. AAPL)" value={symbol} onChange={e => setSymbol(e.target.value)} />
      <input className="border p-2 mb-2 w-full" placeholder="Price Threshold" type="number" value={price} onChange={e => setPrice(e.target.value)} />
      <select className="border p-2 mb-2 w-full" value={comparison} onChange={e => setComparison(e.target.value)}>
        <option value="lt">Price &lt; Threshold</option>
        <option value="gt">Price &gt; Threshold</option>
      </select>
      <button className="bg-purple-600 text-white px-4 py-2 rounded" onClick={handleSave}>Save Strategy</button>
      {status && <p className="mt-3 text-sm text-green-700">{status}</p>}
    </div>
  );
}
