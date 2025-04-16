import React from 'react';
import Ticker from '../components/Ticker';
import Portfolio from '../components/Portfolio';
import TradeForm from '../components/TradeForm';
import StrategyForm from '../components/StrategyForm';
import PerformanceCard from '../components/PerformanceCard';
import TradeHistory from '../components/TradeHistory';
import ComplianceTable from '../components/ComplianceTable';

export default function Dashboard() {
  const user_id = localStorage.getItem('user_id');

  if (!user_id) {
    return <div className="p-4">User not authenticated. Please login again.</div>;
  }

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold mb-4">TradeSim360 Dashboard</h1>
      <Ticker />
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Portfolio />
        <PerformanceCard />
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <TradeForm />
        <StrategyForm />
      </div>
      <TradeHistory />
      <ComplianceTable />
    </div>
  );
}
