import React, { useState } from 'react';
import API from '../api';

export default function TradeForm() {
  const [symbol, setSymbol] = useState('');
  const [quantity, setQuantity] = useState(0);
  const [price, setPrice] = useState(0);
  const [type, setType] = useState('BUY');
  const [status, setStatus] = useState('');

  const handleTrade = async () => {
    try {
      const user_id = localStorage.getItem('user_id');
      if (!symbol || quantity <= 0 || price <= 0) {
        setStatus('Please fill all fields correctly.');
        return;
      }

      const res = await API.post('/trade/place', {
        user_id,
        symbol,
        quantity: parseInt(quantity),
        price: parseFloat(price),
        type
      });

      setStatus(res.data.message || 'Trade placed!');
    } catch (err) {
      console.error(err);
      setStatus(err.response?.data?.error || 'Trade failed');
    }
  };

  return (
    <div className="bg-white shadow-md rounded p-4">
      <h2 className="text-xl font-semibold mb-3">🛒 Place Trade</h2>
      <div className="grid grid-cols-2 gap-4 mb-4">
        <input className="border p-2" placeholder="Symbol (e.g. AAPL)" value={symbol} onChange={e => setSymbol(e.target.value.toUpperCase())} />
        <input className="border p-2" type="number" placeholder="Quantity" value={quantity} onChange={e => setQuantity(e.target.value)} />
        <input className="border p-2" type="number" placeholder="Price" value={price} onChange={e => setPrice(e.target.value)} />
        <select className="border p-2" value={type} onChange={e => setType(e.target.value)}>
          <option value="BUY">BUY</option>
          <option value="SELL">SELL</option>
        </select>
      </div>
      <button className="bg-blue-600 text-white px-4 py-2 rounded" onClick={handleTrade}>Execute Trade</button>
      {status && <p className="mt-3 text-sm text-green-700">{status}</p>}
    </div>
  );
}
