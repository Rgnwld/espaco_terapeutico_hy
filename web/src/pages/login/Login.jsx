import { useEffect, useState } from 'react';
import './login.css';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Row from 'react-bootstrap/Row';
import axios from 'axios';
import { useCookies } from 'react-cookie';
import { Card, Container, Spinner, Toast } from 'react-bootstrap';
import { ToastContainer } from 'react-bootstrap';

function Login() {
    const [validated, setValidated] = useState(false);
    const [userValidation, setUserValidation] = useState(true);
    const [spinner, setSpiner] = useState(false);
    const [cookie, setCookie] = useCookies();
    const [showToast, setShowToast] = useState(false);
    const [toastMessage, setToastMessage] = useState('');
    const [toastVariant, setToastVariant] = useState('danger'); // success ou danger

    async function handleSubmit(event) {
        setUserValidation(true);
        setShowToast(false);
        setSpiner(true);
        event.preventDefault();
        event.stopPropagation();
        const form = event.currentTarget;

        if (form.checkValidity() === true) {
            const login = { email: event.target[0].value, senha: event.target[1].value };
            var jsonfyied_login = JSON.stringify(login);

            try {
                const response = await axios('http://localhost:5000/api/login', {
                    data: jsonfyied_login,
                    headers: { 'Content-Type': 'application/json' },
                    method: 'POST',
                });
                setCookie('token', response.data.token);
                setShowToast(true);
                setToastVariant('success');
                setToastMessage('Login efetuado com sucesso.');
                setUserValidation(true);
                setValidated(true);

                // Redirecionar ou atualizar a página após o login bem-sucedido
                window.location.href = '/admin/home';
            } catch (error) {
                if (error.response && error.response.status === 401) {
                    console.error('Erro de Validação de Usuário!', error);
                    setShowToast(true);
                    setToastVariant('danger');
                    setToastMessage('Email ou senha incorretos.');
                    setUserValidation(false);
                    setValidated(false);
                } else if (error.response && error.response.status === 500) {
                    console.error('Erro no Servidor!', error);
                    setShowToast(true);
                    setToastVariant('danger');
                    setToastMessage('Erro interno do servidor. Tente novamente mais tarde.');
                } else {
                    console.error('Erro desconhecido!', error);
                    setShowToast(true);
                    setToastVariant('danger');
                    setToastMessage('Não foi possivel acessar o servidor. Tente novamente mais tarde.');
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
            {
                <div
                    aria-live="polite"
                    aria-atomic="true"
                    style={{
                        position: 'fixed',
                        top: 20,
                        right: 20,
                        zIndex: 9999,
                    }}
                >
                    <Toast
                        show={showToast}
                        delay={3000}
                        autohide
                        position="top-center"
                        bg={toastVariant} // success ou danger
                    >
                        <Toast.Body className="d-flex text-white">
                            <div className="me-auto">{toastMessage}</div>
                            <button
                                type="button"
                                className="btn-close btn-close-white"
                                data-bs-dismiss="toast"
                                aria-label="Close"
                                onClick={() => setShowToast(false)}
                            />
                        </Toast.Body>
                    </Toast>
                </div>
            }
        </Container>
    );
}

export default Login;
