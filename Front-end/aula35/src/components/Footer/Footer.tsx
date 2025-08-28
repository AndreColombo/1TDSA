const Footer = () => {
  return (
    <>
      <section className='bg-gradient-to-r from-gray-700 to-gray-700 py-12'>
        <div className='container mx-auto px-4 text-center'>
          <h2 className='text-2xl md:text-3xl font-bold mb-4'>Receba as últimas novidades do cinema</h2>
          <p className='max-w-2xl mx-auto text-gray-300 mb-6'>Assine nossa newsletter e fique por dentro dos lançamentos, trailers exclusivos e promoções especiais.</p>

          <div className='max-w-md mx-auto flex'>
            <input
              type='email'
              placeholder='Seu melhor e-mail'
              className='flex-grow py-3 px-4 rounded-l-full bg-gray-300 focus:outline-none focus:ring-2 focus:ring-red-500'
            />
            <button className='bg-red-600 hover:bg-red-00 text-white py-3 px-6 rounded-r-full transition'>Assinar</button>
          </div>
        </div>
      </section>
      <footer className='bg-gray-900 py-12'>
        <div className='container mx-auto px-4'>
          <div className='grid grid-cols-1 md:grid-cols-4 gap-8'>
            <div>
              <div className='flex items-center space-x-2 mb-4'>
                <a href='index.html'>
                  <img src='imagens/cinefront.png' alt='CineFront Logo' className='h-10' />
                </a>
              </div>
              <p className='text-gray-400 text-sm'>Seu universo cinematográfico favorito, com os melhores filmes, críticas e trailers em um só lugar.</p>
              <div className='flex space-x-4 mt-4'>
                <a href='#' className='text-gray-400 hover:text-red-500 transition'>
                  <i className='fab fa-facebook-f'></i>
                </a>
                <a href='#' className='text-gray-400 hover:text-red-500 transition'>
                  <i className='fab fa-twitter'></i>
                </a>
                <a href='#' className='text-gray-400 hover:text-red-500 transition'>
                  <i className='fab fa-instagram'></i>
                </a>
                <a href='#' className='text-gray-400 hover:text-red-500 transition'>
                  <i className='fab fa-youtube'></i>
                </a>
              </div>
            </div>

            <div>
              <h4 className='text-lg font-semibold mb-4'>Links Rápidos</h4>
              <ul className='space-y-2'>
                <li>
                  <a href='#' className='text-gray-400 hover:text-red-400 transition text-sm'>
                    Início
                  </a>
                </li>
                <li>
                  <a href='#' className='text-gray-400 hover:text-red-400 transition text-sm'>
                    Filmes
                  </a>
                </li>
                <li>
                  <a href='#' className='text-gray-400 hover:text-red-400 transition text-sm'>
                    Séries
                  </a>
                </li>
                <li>
                  <a href='#' className='text-gray-400 hover:text-red-400 transition text-sm'>
                    Em Breve
                  </a>
                </li>
                <li>
                  <a href='#' className='text-gray-400 hover:text-red-400 transition text-sm'>
                    Top Avaliados
                  </a>
                </li>
              </ul>
            </div>

            <div>
              <h4 className='text-lg font-semibold mb-4'>Gêneros</h4>
              <ul className='space-y-2'>
                <li>
                  <a href='#' className='text-gray-400 hover:text-red-400 transition text-sm'>
                    Ação
                  </a>
                </li>
                <li>
                  <a href='#' className='text-gray-400 hover:text-red-400 transition text-sm'>
                    Comédia
                  </a>
                </li>
                <li>
                  <a href='#' className='text-gray-400 hover:text-red-400 transition text-sm'>
                    Drama
                  </a>
                </li>
                <li>
                  <a href='#' className='text-gray-400 hover:text-red-400 transition text-sm'>
                    Ficção Científica
                  </a>
                </li>
                <li>
                  <a href='#' className='text-gray-400 hover:text-red-400 transition text-sm'>
                    Terror
                  </a>
                </li>
              </ul>
            </div>

            <div>
              <h4 className='text-lg font-semibold mb-4'>Contato</h4>
              <ul className='space-y-2'>
                <li className='flex items-center text-gray-400 text-sm'>
                  <i className='fas fa-envelope mr-2 text-red-400'></i>
                  contato@cinefront.com
                </li>
                <li className='flex items-center text-gray-400 text-sm'>
                  <i className='fas fa-phone mr-2 text-red-400'></i> (11) 1234-5678
                </li>
                <li className='flex items-center text-gray-400 text-sm'>
                  <i className='fas fa-map-marker-alt mr-2 text-red-400'></i> São Paulo, Brasil
                </li>
              </ul>
            </div>
          </div>

          <div className='border-t border-gray-800 mt-12 pt-8 text-center'>
            <p className='text-gray-500 text-sm'>© 2024 CineFront. Todos os direitos reservados.</p>
          </div>
        </div>
      </footer>
    </>
  );
};

export default Footer;
