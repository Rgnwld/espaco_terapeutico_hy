import React, { useState } from 'react';
import { Container, Navbar, Nav, Form, FormControl, Dropdown, Image } from 'react-bootstrap';
import logo from '../img/logo.svg'; // Adjust the path based on your file location

function AdminHeader() {
  const [user, setUser] = useState({name: 'NOME_USUARIO'});

  return (
    <Navbar bg="light" expand="lg" className="p-3 mb-3 border-bottom">
      <Container>
        <Navbar.Brand href="#" className="d-flex align-items-center p-0 ml-5 ">
          <Image
            src={logo}
            alt="logo"
            height='48'
            rounded
          />
        </Navbar.Brand>

        <Nav className="me-auto mb-2 mb-lg-0">
          <Nav.Link href="#" className="px-2 link-boyd-emphasis">
            <span>Inicio</span>
          </Nav.Link>
          <Nav.Link href="#" className="px-2 link-body-emphasis">
            <span>Agenda</span>
          </Nav.Link>
          <Nav.Link href="#" className="px-2 link-body-emphasis">
            <span>Pacientes</span>
          </Nav.Link>
        </Nav>
{/* 
        <Form className="d-flex me-3" role="search">
          <FormControl
            type="search"
            placeholder="Search..."
            className="me-2"
            aria-label="Search"
          />
        </Form> */}

        <Dropdown align="end">
          <Dropdown.Toggle variant="light" id="dropdown-basic" className="p-0 border-0 bg-transparent">
            {/* <Image
              src="https://github.com/mdo.png"
              alt="mdo"
              width="32"
              height="32"
              rounded
            /> */}
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" className="bi bi-person-circle text-secondary" viewBox="0 0 16 16">
              <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0" />
              <path fillRule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1" />
            </svg>
          </Dropdown.Toggle>

          <Dropdown.Menu className="text-small">
            <Dropdown.Item className='disabled'>{user.name}</Dropdown.Item>
            <Dropdown.Item href="#Config">Configurações</Dropdown.Item>
            <Dropdown.Item href="#Perfil">Perfil</Dropdown.Item>
            <Dropdown.Divider />
            <Dropdown.Item href="/login">Sair</Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      </Container>
    </Navbar>
  );
}

export default AdminHeader;
