import React, { useEffect, useState } from 'react';
import API from '../api';

export default function Ticker() {
  const [prices, setPrices] = useState({});

  const fetchPrices = async () => {
    try {
      const res = await API.get('/market/ticker');
      setPrices(res.data.prices || {});
    } catch (err) {
      console.error("Error fetching market data:", err);
    }
  };

  useEffect(() => {
    fetchPrices();
    const interval = setInterval(fetchPrices, 5000); // Update every 5s
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="bg-white shadow-md rounded p-4">
      <h2 className="text-xl font-semibold mb-3">📈 Live Market Prices</h2>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {Object.entries(prices).map(([symbol, price]) => (
          <div key={symbol} className="border rounded p-3 text-center">
            <div className="text-sm text-gray-600">{symbol}</div>
            <div className="text-xl font-bold text-green-600">${price}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
