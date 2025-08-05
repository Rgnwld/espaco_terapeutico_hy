import { useState } from 'react';
import './login.css';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Row from 'react-bootstrap/Row';
import axios from 'axios';
import { useCookies } from 'react-cookie';
import { Card, Container, Spinner, Toast } from 'react-bootstrap';
import { useToastContext } from '../../assets/context/toastContext/toast.context';
import { instance } from '../../assets/api/connection.jsx';
import { data } from 'react-router-dom';

function Login() {
    const [validated, setValidated] = useState(false);
    const [userValidation, setUserValidation] = useState(true);
    const [spinner, setSpiner] = useState(false);
    const [cookie, setCookie] = useCookies();
    const { setToast } = useToastContext();

    async function handleSubmit(event) {
        setUserValidation(true);
        setSpiner(true);

        event.preventDefault();
        event.stopPropagation();
        const form = event.currentTarget;

        if (form.checkValidity() === true) {
            const login = { email: event.target[0].value, senha: event.target[1].value };
            var jsonfyied_login = JSON.stringify(login);

            try {
                const response = await instance('/login', { data: jsonfyied_login, method: 'POST' })
                setCookie('token', response.data.token);
                setUserValidation(true);
                setValidated(true);
                setToast({
                    type: 'ADD_TOAST', payload: { show: true, message: 'Login realizado com sucesso!', type: 'success', }
                });
                // Redirecionar ou atualizar a página após o login bem-sucedido
                window.location.href = '/home';
            } catch (error) {
                if (error.response && error.response.status === 401) {
                    console.error('Erro de Validação de Usuário!', error);
                    setToast({ type: 'ADD_TOAST', payload: { show: true, message: 'Usuário ou senha inválidos.', type: 'danger' } });
                    setUserValidation(false);
                    setValidated(false);
                } else if (error.response && error.response.status === 500) {
                    console.error('Erro no Servidor!', error);
                    setToast({
                        type: 'ADD_TOAST',
                        payload: { show: true, message: 'Erro no servidor. Tente novamente mais tarde.', type: 'danger' }
                    });
                    setUserValidation(false);
                    setValidated(false);
                } else {
                    setToast({
                        type: 'ADD_TOAST',
                        payload: { show: true, message: 'Erro no Desconhecido. Tente novamente mais tarde.', type: 'danger' }
                    });
                    console.error('Erro desconhecido!', error);
                    setUserValidation(false);
                    setValidated(false);
                }
            } finally {
                setSpiner(false);
            }
        }
    }

    return (
        <Container fluid className="d-flex justify-content-center align-items-center p-0" style={{ height: '100vh' }}>
            <Row>
                <Card className="p-4 shadow">
                    <Container className='d-flex justify-content-center p-4'>
                        <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor" class="bi bi-person-circle text-secondary" viewBox="0 0 16 16">
                            <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0" />
                            <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1" />
                        </svg>
                    </Container>
                    <Form validated={validated} onSubmit={handleSubmit} className="card-body">
                        <Row className="mb-3">
                            <Form.Group as={Col} controlId="validationCustomUsername">
                                <Form.Label>Email</Form.Label>
                                <InputGroup hasValidation>
                                    <InputGroup.Text id="inputGroupPrepend">🔒</InputGroup.Text>
                                    <Form.Control
                                        type="text"
                                        placeholder="email@domain.com"
                                        aria-describedby="inputGroupPrepend"
                                        isInvalid={!userValidation}
                                        required
                                        feedback="Usuário é obrigatório."
                                    />
                                    <Form.Control.Feedback type="invalid"></Form.Control.Feedback>
                                </InputGroup>
                            </Form.Group>
                        </Row>
                        <Row className="mb-3">
                            <Form.Group as={Col} controlId="validationCustomPassword">
                                <Form.Label>Senha</Form.Label>
                                <InputGroup hasValidation>
                                    <InputGroup.Text id="inputGroupPrepend">🔑</InputGroup.Text>
                                    <Form.Control
                                        type="password"
                                        placeholder="Senha"
                                        aria-describedby="inputGroupPrepend"
                                        required
                                        isInvalid={!userValidation}
                                    />
                                    <Form.Control.Feedback type="invalid"></Form.Control.Feedback>
                                </InputGroup>
                            </Form.Group>
                        </Row>
                        <Form.Group className="mb-3">
                            <Form.Check
                                required
                                label="Aceito os termos de uso"
                                feedback="Você precisa aceitar os termos de uso."
                                feedbackType="invalid"
                            />
                        </Form.Group>
                        <Container className="d-flex p-0 m-0 justify-content-center">
                            <Button className="flex-grow-1" type="submit">
                                {spinner ? (
                                    <Spinner animation="border" role="status" variant="light" size="sm">
                                        <span className="visually-hidden">Loading...</span>
                                    </Spinner>
                                ) : (
                                    'Acessar'
                                )}
                            </Button>
                        </Container>
                    </Form>
                </Card>
            </Row>
        </Container>
    );
}

export default Login;
