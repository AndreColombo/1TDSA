import { Link } from "react-router-dom";

const Header = () => {
  return (
    <>
      <header className='bg-blue-700 text-white p-4 text-center text-xl font-bold'>
        <h1>Meu site com Vite + TS + TW</h1>
        <nav className='bg-blue-100 p-4 flex gap-6 justify-center text-blue-700 - font-bold'>
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
      </header>
    </>
  );
};

export default Header;
