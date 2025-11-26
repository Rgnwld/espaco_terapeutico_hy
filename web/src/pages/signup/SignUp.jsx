import { useState } from 'react';
import { useCookies } from 'react-cookie';
import { useToastContext } from '../../assets/context/toastContext/toast.context.jsx';
import { instance } from '../../assets/api/connection.jsx';
import bg from '../../assets/img/bg_v1.jpg';
import { useNavigate } from 'react-router-dom';

function SignUp() {
    const [validated, setValidated] = useState(false);
    const [userValidation, setUserValidation] = useState({
        diff_password: true,
        email: true,
        full_name: true,
    });
    const [spinner, setSpiner] = useState(false);
    const [cookie, setCookie] = useCookies();
    const navigate = useNavigate();
    const { setToast } = useToastContext();

    async function handleSubmit(event) {
        setSpiner(true);
        let user_step_validation = { diff_password: true, email: true, full_name: true };

        event.preventDefault();
        event.stopPropagation();
        const form = event.currentTarget;

        if (form.checkValidity() === true) {
            const login = {
                nome_completo: event.target[0].value,
                email: event.target[1].value,
                senha: event.target[2].value,
                confirmar_senha: event.target[3].value,
                perfil: 1,
            };
            var jsonfyied_login = JSON.stringify(login);

            if (login.confirmar_senha !== login.senha) {
                setToast({ message: 'As senhas não coincidem!', type: 'error', action: 'ADD_TOAST' });
                user_step_validation.diff_password = false;
                setSpiner(false);
                setUserValidation(user_step_validation);
                return;
            }

            try {
                // const response = await instance('login', { data: jsonfyied_login, method: 'POST' });
                const response = await instance('/usuario', {
                    data: jsonfyied_login,
                    headers: { 'Content-Type': 'application/json' },
                    method: 'POST',
                });

                setCookie('token', response.data.token);
                setValidated(true);
                setToast({ message: 'Cadastro realizado com sucesso!', type: 'success', action: 'ADD_TOAST' });
                // Redirecionar ou atualizar a página após o login bem-sucedido
                navigate('/dashboard');
            } catch (error) {
                console.log(error);
                if (error.response && error.response.status === 401) {
                    console.error('Erro de Validação de Usuário!', error);
                    setToast({
                        message: 'Erro de validação! Por favor, verifique os dados informados.',
                        type: 'error',
                        action: 'ADD_TOAST',
                    });
                    setValidated(false);
                } else if (error.response && error.response.status === 400) {
                    console.error('Já existe um usuário com este Email!', error);
                    setToast({
                        message: 'Já existe um usuário com este Email!',
                        type: 'error',
                        action: 'ADD_TOAST',
                    });
                    user_step_validation.email = false;
                    user_step_validation.full_name = true;
                    user_step_validation.diff_password = true;
                    setValidated(false);
                } else if (error.response && error.response.status === 500) {
                    console.error('Erro no Servidor!', error);
                    setToast({
                        message: 'Erro no servidor! Por favor, tente novamente mais tarde.',
                        type: 'error',
                        action: 'ADD_TOAST',
                    });
                    setValidated(false);
                } else {
                    console.error('Erro desconhecido!', error);
                    setToast({
                        message: 'Erro desconhecido! Por favor, tente novamente.',
                        type: 'error',
                        action: 'ADD_TOAST',
                    });
                    setValidated(false);
                }
            } finally {
                setSpiner(false);
                setValidated(true);
                setUserValidation(user_step_validation);
            }
        } else {
            setUserValidation({ diff_password: false, email: false, full_name: false });
            setToast({
                message: 'Por favor, preencha todos os campos corretamente.',
                type: 'error',
                action: 'ADD_TOAST',
            });
            console.log('Formulário inválido');
        }
    }

    return (
        <>
            <div
                className={
                    'flex h-screen w-screen justify-center items-center bg-cover bg-center ' +
                    (localStorage.theme === 'dark' ? 'invert' : '')
                }
                style={{ backgroundImage: `url(${bg})` }}
            >
                <div className={'flex items-center justify-center ' + (localStorage.theme === 'dark' ? 'invert' : '')}>
                    <div className="rounded-lg border border-gray-200 bg-white shadow-md dark:border-gray-700 dark:bg-gray-900 flex-col flex h-full items-center justify-center sm:px-4">
                        <div className="flex h-full flex-col justify-center gap-4 p-6">
                            <div className="left-0 right-0 inline-block border-gray-200 px-2 py-2.5 sm:px-4">
                                <form onSubmit={handleSubmit} className="flex flex-col gap-4 pb-4">
                                    <h1 className="mb-4 text-2xl font-bold dark:text-white">Cadastro</h1>
                                    <div>
                                        <div className="mb-2">
                                            <label
                                                className="text-sm font-medium text-gray-900 dark:text-gray-300"
                                                htmlFor="full_name"
                                            >
                                                Nome Completo:
                                            </label>
                                        </div>
                                        <div className="flex w-full rounded-lg pt-1">
                                            <div className="relative w-full">
                                                <input
                                                    className={
                                                        'block w-full border disabled:cursor-not-allowed disabled:opacity-50 p-2.5 text-sm rounded-lg ' +
                                                        (userValidation.full_name
                                                            ? 'bg-gray-50 border-gray-300 text-gray-900 focus:border-cyan-500 focus:ring-cyan-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-cyan-500 dark:focus:ring-cyan-500'
                                                            : 'border-red-300')
                                                    }
                                                    id="full_name"
                                                    type="text"
                                                    name="full_name"
                                                    placeholder="Fulado da Silva"
                                                    required
                                                />
                                            </div>
                                        </div>
                                    </div>
                                    <div>
                                        <div className="mb-2">
                                            <label
                                                className="text-sm font-medium text-gray-900 dark:text-gray-300"
                                                htmlFor="email"
                                            >
                                                Email:
                                            </label>
                                        </div>
                                        <div className="flex w-full rounded-lg pt-1">
                                            <div className="relative w-full">
                                                <input
                                                    className={
                                                        'block w-full border disabled:cursor-not-allowed disabled:opacity-50 p-2.5 text-sm rounded-lg ' +
                                                        (userValidation.email
                                                            ? 'bg-gray-50 border-gray-300 text-gray-900 focus:border-cyan-500 focus:ring-cyan-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-cyan-500 dark:focus:ring-cyan-500'
                                                            : 'border-red-300')
                                                    }
                                                    id="email"
                                                    type="email"
                                                    autoComplete="email"
                                                    name="email"
                                                    placeholder="email@exemplo.com"
                                                    required
                                                />
                                            </div>
                                        </div>
                                    </div>
                                    <div>
                                        <div className="mb-2">
                                            <label
                                                className="text-sm font-medium text-gray-900 dark:text-gray-300"
                                                htmlFor="password"
                                            >
                                                Senha
                                            </label>
                                        </div>
                                        <div className="flex w-full rounded-lg pt-1">
                                            <div className="relative w-full">
                                                <input
                                                    className={
                                                        'block w-full border disabled:cursor-not-allowed disabled:opacity-50 p-2.5 text-sm rounded-lg ' +
                                                        (userValidation.diff_password
                                                            ? 'bg-gray-50 border-gray-300 text-gray-900 focus:border-cyan-500 focus:ring-cyan-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-cyan-500 dark:focus:ring-cyan-500'
                                                            : 'border-red-300')
                                                    }
                                                    id="password"
                                                    type="password"
                                                    autoComplete="new-password"
                                                    name="senha"
                                                    required
                                                />
                                            </div>
                                        </div>
                                    </div>
                                    <div>
                                        <div className="mb-2">
                                            <label
                                                className="text-sm font-medium text-gray-900 dark:text-gray-300"
                                                htmlFor="confirmar_senha"
                                            >
                                                Confirmar Senha
                                            </label>
                                        </div>
                                        <div className="flex w-full rounded-lg pt-1">
                                            <div className="relative w-full">
                                                <input
                                                    className={
                                                        'block w-full border disabled:cursor-not-allowed disabled:opacity-50 p-2.5 text-sm rounded-lg ' +
                                                        (userValidation.diff_password
                                                            ? 'bg-gray-50 border-gray-300 text-gray-900 focus:border-cyan-500 focus:ring-cyan-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-cyan-500 dark:focus:ring-cyan-500'
                                                            : 'border-red-300')
                                                    }
                                                    id="confirmar_senha"
                                                    type="password"
                                                    name="confirmar_senha"
                                                    autoComplete="new-password"
                                                    required
                                                />
                                            </div>
                                        </div>
                                    </div>
                                    <div className="flex flex-col gap-2">
                                        {!spinner ? (
                                            <button
                                                type="submit"
                                                className="border transition-colors focus:ring-2 p-0.5 disabled:cursor-not-allowed border-transparent bg-sky-600 hover:bg-sky-700 active:bg-sky-800 text-white disabled:bg-gray-300 disabled:text-gray-700 rounded-lg "
                                            >
                                                <span className=" flex items-center justify-center gap-1 font-medium py-1 px-2.5 text-base false">
                                                    Cadastrar
                                                </span>
                                            </button>
                                        ) : (
                                            <>
                                                <button
                                                    type="submit"
                                                    className="border transition-colors focus:ring-2 p-0.5 disabled:cursor-not-allowed border-transparent bg-sky-600 hover:bg-sky-700 active:bg-sky-800 text-white disabled:bg-gray-300 disabled:text-gray-700 rounded-lg "
                                                    onClick={(ev) => ev.preventDefault()}
                                                >
                                                    <span className="flex items-center justify-center gap-1 font-medium py-1 px-2.5 text-base false">
                                                        Carregando...
                                                    </span>
                                                </button>
                                            </>
                                        )}
                                    </div>
                                </form>
                                <div className="min-w-[270px]">
                                    <div className="mt-4 text-center dark:text-gray-200">Já possuí conta? </div>
                                    <div className="text-center dark:text-gray-200">
                                        <a className="text-blue-500 underline hover:text-blue-600" href="/login">
                                            Faça o seu login aqui.
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}

export default SignUp;
