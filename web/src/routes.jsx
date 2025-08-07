import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/login/Login';
import AdminHeader from './assets/components/Header.component';
import { useEffect } from 'react';
import { useCookies } from 'react-cookie';

function ProjectRoutes() {
    const [cookie, setCookie] = useCookies(['token']);

    useEffect(() => {
        if (location.href != '/login' && (cookie.token == '' || cookie.token == undefined)) {
            // location.href = '/login';
            console.log('redir');
        }
    });

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route
                    path="/home"
                    element={
                        <>
                            <AdminHeader />
                        </>
                    }
                />
            </Routes>
        </BrowserRouter>
    );
}

export default ProjectRoutes;
