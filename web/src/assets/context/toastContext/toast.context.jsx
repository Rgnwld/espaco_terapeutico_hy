import { act, createContext, useContext, useEffect, useReducer, useState } from "react";
import { Toast, ToastContainer } from "react-bootstrap";

export const toastContext = createContext();

export const useToastContext = () => {
    const context = useContext(toastContext);
    if (context === undefined) {
        throw new Error("useToastContext must be used within a CookieProvider");
    }
    return context;
};

// const toastInitialState = { id: Date.now(), show: false, message: '', type: 'info' }

const reducer = (state, action) => {
    switch (action.type) {
        case 'ADD_TOAST':
            return [{ id: Date.now(), ...action.payload }, ...state];
        case 'REMOVE_TOAST':
            return state.filter(toast => toast.id !== action.payload.id);
        default:
            throw new Error(`Unhandled action type: ${action.type}`);
    }
};

export const ToastProvider = ({ children }) => {
    const [toast, setToast] = useReducer(reducer, []);


    return (
        <toastContext.Provider value={{ toast, setToast }}>
            {children}
            <ToastContainer
                aria-live="polite"
                aria-atomic="true"
                style={{
                    position: 'fixed',
                    top: 20,
                    right: 20,
                    zIndex: 9999,
                }}
            >
                {
                    toast.map((t) => {
                        setTimeout(() => setToast({ type: 'REMOVE_TOAST', payload: { id: t.id } }), 3000)

                        return <Toast
                            key={t.id}
                            show={t.show}
                            delay={3000}
                            autohide
                            position="top-center"
                            bg={t.type} // success ou danger
                        >
                            <Toast.Body className="d-flex text-white">
                                <div className="me-auto">{t.message}</div>
                                <button
                                    type="button"
                                    className="btn-close btn-close-white"
                                    data-bs-dismiss="toast"
                                    aria-label="Close"
                                    onClick={() => setToast({ type: 'REMOVE_TOAST', payload: { id: t.id } })}
                                />
                            </Toast.Body>
                        </Toast>
                    })
                }
            </ToastContainer>
        </toastContext.Provider>
    );
};

