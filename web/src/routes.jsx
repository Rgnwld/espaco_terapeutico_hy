import { BrowserRouter, Routes, Route, useNavigate } from 'react-router-dom';
import Login from './pages/login/Login';
import AdminRoute from './pages/admin/AdminRoute';
import Not_Found from './pages/not_found/not_found';
import SignUp from './pages/signup/SignUp';

function ProjectRoutes() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/home" element={<AdminRoute>Home</AdminRoute>} />
                <Route path="/info" element={<AdminRoute>info</AdminRoute>} />
                <Route path="/contact" element={<AdminRoute>contact</AdminRoute>} />
                <Route path="/about" element={<AdminRoute>about</AdminRoute>} />
                <Route path="SignUp" element={<SignUp />} />
                <Route path="*" element={<Not_Found />} />
            </Routes>
        </BrowserRouter>
    );
}

export default ProjectRoutes;
