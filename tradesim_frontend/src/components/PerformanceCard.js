import React, { useEffect, useState } from 'react';
import API from '../api';

export default function PerformanceCard() {
  const [stats, setStats] = useState(null);

  const fetchPerformance = async () => {
    try {
      const user_id = localStorage.getItem('user_id');
      const res = await API.get(`/analytics/performance?user_id=${user_id}`);
      setStats(res.data);
    } catch (err) {
      console.error("Failed to fetch performance:", err);
    }
  };

  useEffect(() => {
    fetchPerformance();
  }, []);

  if (!stats) return <div className="p-4 bg-white rounded shadow">Loading performance...</div>;

  return (
    <div className="bg-white shadow-md rounded p-4">
      <h2 className="text-xl font-semibold mb-3">📊 Performance Analytics</h2>
      <ul className="space-y-1">
        <li><strong>Total Trades:</strong> {stats.total_trades}</li>
        <li><strong>Win Rate:</strong> {stats.win_rate}</li>
        <li><strong>Avg Return/Trade:</strong> ${stats.avg_return_per_trade}</li>
        <li><strong>Sharpe Ratio:</strong> {stats.sharpe_ratio}</li>
        <li><strong>Total Profit:</strong> ${stats.total_profit}</li>
      </ul>
    </div>
  );
}
