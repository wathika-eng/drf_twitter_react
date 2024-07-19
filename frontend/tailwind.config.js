/** @type {import('tailwindcss').Config} */
import daisyui from 'daisyui';
export default {
	content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
	theme: {
		extend: {
			container: {
				padding: {
					DEFAULT: '0.5rem',
					sm: '2rem',
					lg: '4rem',
					xl: '5rem',
					'2xl': '6rem',
				},
			},
		},
	},
	plugins: [daisyui],
};
