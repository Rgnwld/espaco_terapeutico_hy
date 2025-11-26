import { act, createContext, useContext, useEffect, useReducer, useState } from 'react';
import '../../../output.css';

export const toastContext = createContext();

export const useToastContext = () => {
    const context = useContext(toastContext);
    if (context === undefined) {
        throw new Error('useToastContext must be used within a CookieProvider');
    }
    return context;
};

const reducer = (state, ev) => {
    console.log(ev);

    function TypeSelector(type) {
        switch (type) {
            case 'success':
                return toastStyles.icons.sucess;
            case 'error':
                return toastStyles.icons.error;
            case 'warning':
                return toastStyles.icons.warning;
            default:
                return null;
        }
    }

    switch (ev.action) {
        case 'ADD_TOAST':
            let _state = [{ ...ev, id: Date.now(), icon: TypeSelector(ev.type) }, ...state];
            return _state;
        case 'REMOVE_TOAST':
            return state.filter((toast) => toast.id !== ev.id);
        default:
            throw new Error(`Unhandled action type: ${ev.action}`);
    }
};

export const ToastProvider = ({ children }) => {
    const [toast, setToast] = useReducer(reducer, []);
    const maxToastCount = 3;

    function RemoveToast(toastItem) {
        setToast({ action: 'REMOVE_TOAST', id: toastItem.id });
    }

    return (
        <toastContext.Provider value={{ toast, setToast }}>
            <div className="absolute space-y-3 w-full margin-top-5 top-5 left-0 flex flex-col items-center z-50 ">
                {toast.map((toastItem, id) =>
                    id < maxToastCount ? (
                        <div key={toastItem.id} className="flex justify-center">
                            <div
                                id="toast-default"
                                className="flex items-center w-full p-4 text-gray-500 bg-white rounded-lg shadow-sm dark:text-gray-400 dark:bg-gray-800 gap-10  cursor-pointer animate-bounce"
                                style={{ animationIterationCount: '.50' }}
                                onClick={() => RemoveToast(toastItem)}
                                role="alert"
                            >
                                {toastItem.icon}
                                <div className=" text-sm font-normal text-nowrap">{toastItem.message}</div>
                                <button
                                    type="button"
                                    className=" bg-white text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700"
                                    data-dismiss-target="#toast-default"
                                    aria-label="Close"
                                >
                                    <span className="sr-only">Close</span>
                                    <svg
                                        className="w-3 h-3"
                                        aria-hidden="true"
                                        xmlns="http://www.w3.org/2000/svg"
                                        fill="none"
                                        viewBox="0 0 14 14"
                                    >
                                        <path
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
                                        />
                                    </svg>
                                </button>
                            </div>
                        </div>
                    ) : (
                        ''
                    )
                )}
            </div>
            {children}
        </toastContext.Provider>
    );
};

// const toastInitialState = { id: Date.now(), show: false, message: '', type: 'info' }

const toastStyles = {
    icons: {
        warning: (
            <div className="inline-flex items-center justify-center shrink-0 w-8 h-8 text-orange-500 bg-orange-100 rounded-lg dark:bg-orange-700 dark:text-orange-200">
                <svg
                    className="w-5 h-5"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                >
                    <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM10 15a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-4a1 1 0 0 1-2 0V6a1 1 0 0 1 2 0v5Z" />
                </svg>
                <span className="sr-only">Warning icon</span>
            </div>
        ),
        sucess: (
            <div className="inline-flex items-center justify-center shrink-0 w-8 h-8 text-green-500 bg-green-100 rounded-lg dark:bg-green-800 dark:text-green-200">
                <svg
                    className="w-5 h-5"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                >
                    <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z" />
                </svg>
                <span className="sr-only">Check icon</span>
            </div>
        ),
        error: (
            <div className="inline-flex items-center justify-center shrink-0 w-8 h-8 text-red-500 bg-red-100 rounded-lg dark:bg-red-800 dark:text-red-200">
                <svg
                    className="w-5 h-5"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                >
                    <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 11.793a1 1 0 1 1-1.414 1.414L10 11.414l-2.293 2.293a1 1 0 0 1-1.414-1.414L8.586 10 6.293 7.707a1 1 0 0 1 1.414-1.414L10 8.586l2.293-2.293a1 1 0 0 1 1.414 1.414L11.414 10l2.293 2.293Z" />
                </svg>
                <span className="sr-only">Error icon</span>
            </div>
        ),
    },
};
