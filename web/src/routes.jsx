import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/login/Login';
import AdminHeader from './assets/components/Header.component';

function ProjectRoutes() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/home" element={<><AdminHeader /></>} />
            </Routes>
        </BrowserRouter>
    );
}

export default ProjectRoutes;
