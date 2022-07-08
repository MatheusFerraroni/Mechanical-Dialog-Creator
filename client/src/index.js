import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Chat from './Chat';

const root = ReactDOM.createRoot(document.getElementById('root'));


if (window.location.pathname=="/chat" || window.location.pathname=="/Mechanical-Dialog-Creator/chat"){
    root.render(
        <Chat />
    );
}else{
    root.render(
        <App />
    );
}


