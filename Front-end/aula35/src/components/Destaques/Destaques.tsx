const Destaques = () => {
  return (
    <>
      {/* <!-- Trending Movies --> */}
      <section className='mb-16'>
        <div className='flex justify-between items-center mb-8'>
          <h2 className='text-2xl md:text-3xl font-bold'>Filmes em Destaque</h2>
          <a href='#' className='text-red-400 hover:text-red-300 flex items-center'>
            Ver todos <i className='fas fa-chevron-right ml-2'></i>
          </a>
        </div>

        <div className='grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6'>
          {/* <!-- Movie Card 1 --> */}
          <div className='movie-card bg-gray-800 rounded-lg overflow-hidden shadow-lg hover:shadow-red-500/20 transition duration-300'>
            <div className='relative overflow-hidden'>
              <a href='aranhaverso.html'>
                <img src='imagens/8Vt6mWEReuy4Of61Lnj5Xj704m8.webp' alt='Duna' className='w-full h-64 object-cover movie-poster' />
              </a>
              <div className='absolute bottom-3 left-3'>
                <div className='rating-circle rating-high'>8.4</div>
              </div>
            </div>
            <div className='p-4'>
              <h3 className='font-bold text-lg mb-1'>Homem-Aranha: Através do Aranhaverso</h3>
              <div className='flex flex-wrap gap-2 mb-3'>
                <span className='genre-tag text-xs bg-red-900/50 text-red-300 px-2 py-1 rounded-full'>Ficção Científica</span>
                <span className='genre-tag text-xs bg-blue-900/50 text-blue-300 px-2 py-1 rounded-full'>Aventura</span>
              </div>
              <p className='text-gray-400 text-sm line-clamp-2'>
                Miles Morales retorna para o próximo capítulo da saga do Aranhaverso, uma aventura épica que transportará o Homem-Aranha.
              </p>
            </div>
          </div>

          {/* <!-- Movie Card 2 --> */}
          <div className='movie-card bg-gray-800 rounded-lg overflow-hidden shadow-lg hover:shadow-red-500/20 transition duration-300'>
            <div className='relative overflow-hidden'>
              <a href='oppenheimer.html'>
                <img src='imagens/1OsQJEoSXBjduuCvDOlRhoEUaHu.webp' alt='Oppenheimer' className='w-full h-64 object-cover movie-poster' />
              </a>
              <div className='absolute bottom-3 left-3'>
                <div className='rating-circle rating-high'>8.3</div>
              </div>
            </div>
            <div className='p-4'>
              <h3 className='font-bold text-lg mb-1'>
                Oppenheimer
                <br />
                &nbsp;
              </h3>
              <div className='flex flex-wrap gap-2 mb-3'>
                <span className='genre-tag text-xs bg-yellow-900/50 text-yellow-300 px-2 py-1 rounded-full'>Histórico</span>
                <span className='genre-tag text-xs bg-purple-900/50 text-purple-300 px-2 py-1 rounded-full'>Drama</span>
              </div>
              <p className='text-gray-400 text-sm line-clamp-2'>
                A história do cientista J. Robert Oppenheimer e seu papel no desenvolvimento da bomba atômica durante a Segunda Guerra Mundial.
              </p>
            </div>
          </div>

          {/* <!-- Movie Card 3 --> */}
          <div className='movie-card bg-gray-800 rounded-lg overflow-hidden shadow-lg hover:shadow-red-500/20 transition duration-300'>
            <div className='relative overflow-hidden'>
              <a href='godzilla.html'>
                <img src='imagens/fWSGD2yrzz6hscocnMD8AEXIThk.webp' alt='Godzilla e Kong' className='w-full h-64 object-cover movie-poster' />
              </a>
              <div className='absolute bottom-3 left-3'>
                <div className='rating-circle rating-medium'>7.1</div>
              </div>
            </div>
            <div className='p-4'>
              <h3 className='font-bold text-lg mb-1'>
                Godzilla e Kong: O Novo Império
                <br />
                &nbsp;
              </h3>
              <div className='flex flex-wrap gap-2 mb-3'>
                <span className='genre-tag text-xs bg-green-900/50 text-green-300 px-2 py-1 rounded-full'>Ação</span>
                <span className='genre-tag text-xs bg-gray-900/50 text-gray-300 px-2 py-1 rounded-full'>Ficção Científica</span>
              </div>
              <p className='text-gray-400 text-sm line-clamp-2'>
                Godzilla e Kong unem forças contra uma ameaça colossal escondida no interior da Terra, desafiando sua própria existência.
              </p>
            </div>
          </div>

          {/* <!-- Movie Card 4 --> */}
          <div className='movie-card bg-gray-800 rounded-lg overflow-hidden shadow-lg hover:shadow-red-500/20 transition duration-300'>
            <div className='relative overflow-hidden'>
              <a href='kungfupanda4.html'>
                <img src='imagens/kDp1vUBnMpe8ak4rjgl3cLELqjU.webp' alt='Kung Fu Panda 4' className='w-full h-64 object-cover movie-poster' />
              </a>
              <div className='absolute bottom-3 left-3'>
                <div className='rating-circle rating-medium'>7.0</div>
              </div>
            </div>
            <div className='p-4'>
              <h3 className='font-bold text-lg mb-1'>
                Kung Fu Panda 4<br />
                &nbsp;
              </h3>
              <div className='flex flex-wrap gap-2 mb-3'>
                <span className='genre-tag text-xs bg-orange-900/50 text-orange-300 px-2 py-1 rounded-full'>Animação</span>
                <span className='genre-tag text-xs bg-pink-900/50 text-pink-300 px-2 py-1 rounded-full'>Comédia</span>
                <span className='genre-tag text-xs bg-amber-900/50 text-amber-300 px-2 py-1 rounded-full'>Aventura</span>
              </div>
              <p className='text-gray-400 text-sm line-clamp-2'>
                Po precisa encontrar um sucessor como Dragão Guerreiro enquanto enfrenta um novo vilão que pode conjurar todos os vilões do passado.
              </p>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Destaques;
