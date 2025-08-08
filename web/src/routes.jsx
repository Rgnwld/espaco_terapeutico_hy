import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/login/Login';
import AdminRoute from './pages/admin/AdminRoute';

function ProjectRoutes() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/home" element={<AdminRoute>Home</AdminRoute>} />
                <Route path="/info" element={<AdminRoute>info</AdminRoute>} />
                <Route path="/contact" element={<AdminRoute>contact</AdminRoute>} />
                <Route path="/about" element={<AdminRoute>about</AdminRoute>} />
            </Routes>
        </BrowserRouter>
    );
}

export default ProjectRoutes;
