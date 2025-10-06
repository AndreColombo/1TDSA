import { Link } from "react-router-dom";

import { useContext } from "react";
import { ThemeContext } from "../../contexts/ThemeContext";

export default function Header() {
  const { theme, toggleTheme } = useContext(ThemeContext);
  return (
    <>
      <header className='bg-black text-white px-8 py-4 text-center font-bold flex justify-between items-center'>
        <h1 className='text-3xl'>Nossos Livrinhos ❤️</h1>
        <div className='flex gap-6'>
          <nav className='bg-black p-4 flex gap-6 text-lg justify-center text-white font-bold'>
            <Link to='/' className='hover:underline'>
              Home
            </Link>
            <Link to='/sobre' className='hover:underline'>
              Sobre
            </Link>
            <Link to='/contato' className='hover:underline'>
              Contato
            </Link>
          </nav>
          <button onClick={toggleTheme}>
            <svg className='w-6' viewBox='0 0 512 512' fill='none' xmlns='http://www.w3.org/2000/svg'>
              <path
                d='M256 0C397.385 0 512 114.615 512 256C512 397.385 397.385 512 256 512C114.615 512 0 397.385 0 256C0 114.615 114.615 0 256 0ZM256 25C128.422 25 25 128.422 25 256C25 383.578 128.422 487 256 487C383.578 487 487 383.578 487 256C487 128.422 383.578 25 256 25ZM245.504 62.2588C251.019 61.9735 255.5 66.4772 255.5 72V439C255.5 444.523 251.019 449.027 245.504 448.741C223.509 447.603 201.844 442.718 181.451 434.271C157.975 424.546 136.643 410.293 118.675 392.325C100.707 374.357 86.4538 353.025 76.7295 329.549C67.0053 306.072 62 280.911 62 255.5C62 230.089 67.0053 204.928 76.7295 181.451C86.4538 157.975 100.707 136.643 118.675 118.675C136.643 100.707 157.975 86.4538 181.451 76.7295C201.844 68.2825 223.509 63.3965 245.504 62.2588Z'
                fill='white'
              />
            </svg>
          </button>
        </div>
      </header>
    </>
  );
}
