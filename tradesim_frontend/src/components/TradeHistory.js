import React, { useEffect, useState } from 'react';
import API from '../api';

export default function TradeHistory() {
  const [trades, setTrades] = useState([]);

  const fetchHistory = async () => {
    try {
      const user_id = localStorage.getItem('user_id');
      const res = await API.get(`/trade/history?user_id=${user_id}`);
      setTrades(res.data.trades || []);
    } catch (err) {
      console.error("Failed to load trade history:", err);
    }
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  return (
    <div className="bg-white shadow-md rounded p-4 mt-6">
      <h2 className="text-xl font-semibold mb-3">📜 Trade History</h2>
      {trades.length === 0 ? (
        <p className="text-gray-500 italic">No trades yet.</p>
      ) : (
        <table className="w-full text-sm border">
          <thead className="bg-gray-100">
            <tr>
              <th className="p-2">Symbol</th>
              <th className="p-2">Type</th>
              <th className="p-2">Qty</th>
              <th className="p-2">Price</th>
              <th className="p-2">Time</th>
            </tr>
          </thead>
          <tbody>
            {trades.map((t, i) => (
              <tr key={i} className="border-t">
                <td className="p-2">{t.symbol}</td>
                <td className="p-2">{t.type}</td>
                <td className="p-2">{t.quantity}</td>
                <td className="p-2">${t.price}</td>
                <td className="p-2 text-gray-500">{t.timestamp}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
