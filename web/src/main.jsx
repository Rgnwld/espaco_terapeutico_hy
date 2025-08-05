import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import App from './App.jsx';
import { CookiesProvider } from 'react-cookie';
import { ToastProvider } from './assets/context/toastContext/toast.context.jsx';

createRoot(document.getElementById('root')).render(
    <StrictMode>
        <ToastProvider>
            <CookiesProvider defaultSetOptions={{ path: '/' }}>
                <App />
            </CookiesProvider>
        </ToastProvider>
    </StrictMode>
);
