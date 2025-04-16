import React, { useEffect, useState } from 'react';
import API from '../api';

export default function ComplianceTable() {
  const [violations, setViolations] = useState([]);

  const fetchViolations = async () => {
    try {
      const user_id = localStorage.getItem('user_id');
      const res = await API.get(`/compliance/violations?user_id=${user_id}`);
      setViolations(res.data.violations || []);
    } catch (err) {
      console.error("Error fetching compliance violations:", err);
    }
  };

  useEffect(() => {
    fetchViolations();
  }, []);

  return (
    <div className="bg-white shadow-md rounded p-4 mt-6">
      <h2 className="text-xl font-semibold mb-3">🚨 Compliance Violations</h2>
      {violations.length === 0 ? (
        <p className="text-gray-500 italic">No violations logged yet.</p>
      ) : (
        <table className="w-full text-sm border">
          <thead className="bg-red-100 text-red-900">
            <tr>
              <th className="p-2">Trade ID</th>
              <th className="p-2">Violation</th>
              <th className="p-2">Timestamp</th>
            </tr>
          </thead>
          <tbody>
            {violations.map((v, i) => (
              <tr key={i} className="border-t">
                <td className="p-2">{v.trade_id}</td>
                <td className="p-2">{v.violation}</td>
                <td className="p-2 text-gray-500">{v.timestamp}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
