import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import API from '../api';

export default function Register() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const register = async () => {
    try {
      await API.post('/auth/register', { email, password });
      alert("Registration successful");
      navigate('/');
    } catch (err) {
      alert(err.response.data.error || 'Registration failed');
    }
  };

  return (
    <div className="p-10 max-w-md mx-auto space-y-4">
      <h1 className="text-2xl font-bold">Register</h1>
      <input className="border p-2 w-full" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
      <input className="border p-2 w-full" placeholder="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} />
      <button className="bg-green-600 text-white px-4 py-2 w-full" onClick={register}>Register</button>
    </div>
  );
}
