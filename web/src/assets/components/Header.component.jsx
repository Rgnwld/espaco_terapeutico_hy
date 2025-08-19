import { useEffect, useState } from 'react';
import { useCookies } from 'react-cookie';

function AdminHeader() {
    const [user, setUser] = useState({ name: 'NOME_USUARIO' });
    const [selected, setSelected] = useState('');
    const [cookie, setCookie] = useCookies(['token']);

    useEffect(() => {
        console.log(location.pathname.split('/')[1]);
        setSelected(location.pathname.split('/')[1]);
    }, []);

    return <></>;
}

export default AdminHeader;
