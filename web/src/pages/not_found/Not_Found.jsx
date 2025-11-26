import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useToastContext } from '../../assets/context/toastContext/toast.context';

// import { Container } from './styles';

function Not_Found() {
    const navigate = useNavigate();
    const { setToast } = useToastContext();

    useEffect(() => {
        setToast({
            message: 'Página não encontrada! Redirecionando ao login...',
            type: 'warning',
            action: 'ADD_TOAST',
        });
        navigate('/login');
    }, []);

    return (
        <div>
            <p>Página não encontrada</p>
            <a href="/login">
                <u>Redirecionar ao login</u>
            </a>
        </div>
    );
}

export default Not_Found;
