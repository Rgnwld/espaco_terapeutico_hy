import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/login/Login';

function ProjectRoutes() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
            </Routes>
        </BrowserRouter>
    );
}

export default ProjectRoutes;
