const Header = () => {
  return (
    <>
      <header className='fixed w-full z-50 bg-gray-900/80 backdrop-blur-md'>
        <div className='container mx-auto px-4 py-3 flex justify-between items-center'>
          <div className='flex items-center space-x-2'>
            <a href='index.html'>
              <img src='imagens/cinefront.png' alt='CineFront Logo' className='h-20' />
            </a>
          </div>

          <nav className='hidden md:flex space-x-8'>
            <a href='#' className='hover:text-red-400 transition'>
              Filmes
            </a>
            <a href='#' className='hover:text-red-400 transition'>
              Séries
            </a>
            <a href='#' className='hover:text-red-400 transition'>
              Em Breve
            </a>
            <a href='#' className='hover:text-red-400 transition'>
              Contato
            </a>
          </nav>

          <div className='flex items-center space-x-4'>
            <button className='p-2 rounded-full hover:bg-gray-700 transition'>
              <i className='fas fa-search'></i>
            </button>
            <button className='md:hidden p-2 rounded-full hover:bg-gray-700 transition' id='mobile-menu-button'>
              <i className='fas fa-bars'></i>
            </button>
          </div>
        </div>

        {/* <!-- Mobile Menu --> */}
        <div className='md:hidden hidden bg-gray-800 w-full py-3 px-4' id='mobile-menu'>
          <div className='flex flex-col space-y-3'>
            <a href='#' className='hover:text-red-400 transition'>
              Início
            </a>
            <a href='#' className='hover:text-red-400 transition'>
              Filmes
            </a>
            <a href='#' className='hover:text-red-400 transition'>
              Séries
            </a>
            <a href='#' className='hover:text-red-400 transition'>
              Em Breve
            </a>
            <a href='#' className='hover:text-red-400 transition'>
              Contato
            </a>
          </div>
        </div>
      </header>
    </>
  );
};

export default Header;
