/** @type {import('tailwindcss').Config} */
export default {
    darkMode: 'class',
    content: ['./src/**/*.{js,jsx,ts,tsx}'],
    theme: {
        extend: {
            animation: {},
            colors: {
                'custom-prime': '#e4e1da',
            },
        },
    },
    plugins: [],
    variants: {
        extend: {},
    },
};
