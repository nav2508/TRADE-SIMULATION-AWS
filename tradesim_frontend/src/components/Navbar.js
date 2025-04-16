import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function Navbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('user_id');
    navigate('/');
  };

  return (
    <nav className="bg-gray-800 text-white px-6 py-3 flex justify-between items-center">
      <h1 className="text-xl font-bold">💹 TradeSim360</h1>
      <button onClick={handleLogout} className="bg-red-500 hover:bg-red-600 px-4 py-2 rounded">
        Logout
      </button>
    </nav>
  );
}
