import { useEffect, useState } from 'react';
import { useCookies } from 'react-cookie';
import '../../../output.css';

function Header() {
    const [user, setUser] = useState({ name: 'NOME_USUARIO' });
    const [selected, setSelected] = useState('');
    const [cookie, setCookie] = useCookies(['token']);

    useEffect(() => {
        console.log(location.pathname.split('/')[1]);
        setSelected(location.pathname.split('/')[1]);
    }, []);

    return (
        <header className="flex justify-between items-center p-4 bg-white border-b-2 border-custom-prime">
            <div>Icone</div>
            <div className="flex gap-8">
                <div>
                    <a href="home">Home</a>
                </div>
                <div>
                    <a href="contato">Contato</a>
                </div>
                <div>
                    <a href="dashboard">Dashboard</a>
                </div>
            </div>
            <div>
                <a href="login">LogOut</a>
            </div>
        </header>
    );
}

export default Header;
