import React, { useEffect, useState } from 'react';
import API from '../api';

export default function Portfolio() {
  const [portfolio, setPortfolio] = useState({ cash: 0, holdings: {} });

  const fetchPortfolio = async () => {
    try {
      const user_id = localStorage.getItem('user_id');
      const res = await API.get(`/portfolio/?user_id=${user_id}`);
      setPortfolio(res.data);
    } catch (err) {
      console.error("Failed to load portfolio:", err);
    }
  };

  useEffect(() => {
    fetchPortfolio();
  }, []);

  return (
    <div className="bg-white shadow-md rounded p-4">
      <h2 className="text-xl font-semibold mb-3">💼 Portfolio Overview</h2>
      <p className="mb-4"><strong>Cash Balance:</strong> ${portfolio.cash?.toFixed(2)}</p>
      <h3 className="font-semibold">Holdings:</h3>
      {Object.keys(portfolio.holdings || {}).length === 0 ? (
        <p className="text-gray-500 italic">No current positions.</p>
      ) : (
        <ul className="list-disc pl-5">
          {Object.entries(portfolio.holdings).map(([symbol, qty]) => (
            <li key={symbol}>{symbol}: {qty} shares</li>
          ))}
        </ul>
      )}
    </div>
  );
}
