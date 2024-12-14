import axios from 'axios';

const API = axios.create({
  // baseURL: 'http://127.0.0.1:8000/api/',
  baseURL: `${import.meta.env.VITE_API_URL}`,  
  

});

API.interceptors.request.use((config) => {
  const accessToken = localStorage.getItem('access_token');
  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }
  return config;
});

export default API;
