import { useEffect, useState } from 'react';
import { Container, Nav, NavLink, Button, NavItem } from 'react-bootstrap';
import { useCookies } from 'react-cookie';

function AdminHeader() {
    const [user, setUser] = useState({ name: 'NOME_USUARIO' });
    const [selected, setSelected] = useState('');
    const [cookie, setCookie] = useCookies(['token']);

    useEffect(() => {
        console.log(location.pathname.split('/')[1]);
        setSelected(location.pathname.split('/')[1]);
    }, []);

    return (
        <Container className="d-flex flex p-4 justify-content-between">
            <Nav className="col-sm col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                <NavItem>
                    <NavLink className={selected == 'home' ? 'text-secondary' : 'text-primary'} href="home">
                        Inicio
                    </NavLink>
                </NavItem>
                <NavItem>
                    <NavLink className={selected == 'info' ? 'text-secondary' : 'text-primary'} href="info">
                        Informações
                    </NavLink>
                </NavItem>
                <NavItem>
                    <NavLink className={selected == 'contact' ? 'text-secondary' : 'text-primary'} href="contact">
                        Contato
                    </NavLink>
                </NavItem>
                <NavItem>
                    <NavLink className={selected == 'about' ? 'text-secondary' : 'text-primary'} href="about">
                        Sobre
                    </NavLink>
                </NavItem>
            </Nav>
            <Container className="d-flex gap-1 justify-content-end">
                <Button className="border-primary bg-light text-primary">Login</Button>
                <Button className="border-primary">Cadastro</Button>
            </Container>
        </Container>
    );
}

export default AdminHeader;
