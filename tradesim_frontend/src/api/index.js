import axios from 'axios';

const API = axios.create({
  baseURL: 'http://44.204.161.233:5000/api',  // replace with your actual API route
});

export default API;
