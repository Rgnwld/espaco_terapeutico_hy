import { Children, useEffect } from 'react';
import AdminHeader from '../../assets/components/Header/Header.component';
import { useCookies } from 'react-cookie';

function AdminRoute({ children }) {
    const [cookie, setCookie] = useCookies(['token']);

    useEffect(() => {
        if (location.href != '/login' && (cookie.token == '' || cookie.token == undefined)) {
            console.log('redir');
        }
    });

    return (
        <>
            <AdminHeader />
            {children}
        </>
    );
}

export default AdminRoute;
