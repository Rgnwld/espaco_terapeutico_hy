import { useEffect } from 'react';
import './App.css';
import ProjectRoutes from './routes';

function App() {
    // const [count, setCount] = useState(0)

    useEffect(() => {
        // On page load or when changing themes, best to add inline in `head` to avoid FOUC
        document.documentElement.classList.toggle(
            'dark',
            localStorage.theme === 'dark' ||
                (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)
        );

        if (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)
            localStorage.setItem('theme', 'dark');
    }, []);

    return (
        <>
            <ProjectRoutes />
        </>
    );
}

export default App;
