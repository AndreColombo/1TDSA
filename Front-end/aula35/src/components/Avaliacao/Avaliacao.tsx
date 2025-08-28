const Avaliacao = () => {
  return (
    <>
      {/* <!-- Top Rated --> */}
      <section>
        <div className='flex justify-between items-center mb-8'>
          <h2 className='text-2xl md:text-3xl font-bold'>Melhores Avaliados</h2>
          <a href='#' className='text-red-400 hover:text-red-300 flex items-center'>
            Ver todos <i className='fas fa-chevron-right ml-2'></i>
          </a>
        </div>

        <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6'>
          {/* <!-- Top Rated 1 --> */}
          <div className='bg-gray-800 rounded-lg overflow-hidden shadow-lg'>
            <div className='relative'>
              <img src='imagens/7g6wvsWHxBQujUcSXvZLhdFpDUy.webp' alt='O Poderoso Chefão' className='w-full h-48 object-cover' />
              <div className='absolute inset-0 bg-gradient-to-t from-gray-900 to-transparent'></div>
              <div className='absolute bottom-0 left-0 p-4'>
                <h3 className='font-bold text-xl'>O Poderoso Chefão</h3>
                <div className='flex items-center mt-1'>
                  <div className='rating-circle rating-high mr-2'>9.2</div>
                  <span className='text-sm'>(1972)</span>
                </div>
              </div>
            </div>
            <div className='p-4'>
              <p className='text-gray-400 text-sm line-clamp-3'>
                O patriarca de uma dinastia do crime organizado transfere o controle de seu império clandestino para seu filho relutante.
                <br />
                &nbsp;
              </p>
              <button className='mt-4 w-full bg-gray-700 hover:bg-gray-600 text-white py-2 px-4 rounded-full text-sm transition'>Assistir Trailer</button>
            </div>
          </div>

          {/* <!-- Top Rated 2 --> */}
          <div className='bg-gray-800 rounded-lg overflow-hidden shadow-lg'>
            <div className='relative'>
              <img src='imagens/4lj1ikfsSmMZNyfdi8R8Tv5tsgb.webp' alt='O Cavaleiro das Trevas' className='w-full h-48 object-cover' />
              <div className='absolute inset-0 bg-gradient-to-t from-gray-900 to-transparent'></div>
              <div className='absolute bottom-0 left-0 p-4'>
                <h3 className='font-bold text-xl'>O Cavaleiro das Trevas</h3>
                <div className='flex items-center mt-1'>
                  <div className='rating-circle rating-high mr-2'>8.5</div>
                  <span className='text-sm'>(2008)</span>
                </div>
              </div>
            </div>
            <div className='p-4'>
              <p className='text-gray-400 text-sm line-clamp-3'>
                Quando o Coringa mergulha Gotham City na anarquia, Batman deve enfrentar o caos enquanto luta com seus próprios limites.
                <br />
                &nbsp;
              </p>
              <button className='mt-4 w-full bg-gray-700 hover:bg-gray-600 text-white py-2 px-4 rounded-full text-sm transition'>Assistir Trailer</button>
            </div>
          </div>

          {/* <!-- Top Rated 3 --> */}
          <div className='bg-gray-800 rounded-lg overflow-hidden shadow-lg'>
            <div className='relative'>
              <img src='imagens/bik2BZjmVjeE6LOZqtuTjb4jJPQ.webp' alt='Parasita' className='w-full h-48 object-cover' />
              <div className='absolute inset-0 bg-gradient-to-t from-gray-900 to-transparent'></div>
              <div className='absolute bottom-0 left-0 p-4'>
                <h3 className='font-bold text-xl'>Parasita</h3>
                <div className='flex items-center mt-1'>
                  <div className='rating-circle rating-high mr-2'>8.5</div>
                  <span className='text-sm'>(2019)</span>
                </div>
              </div>
            </div>
            <div className='p-4'>
              <p className='text-gray-400 text-sm line-clamp-3'>
                Uma família pobre se infiltra na casa de uma família rica, desencadeando eventos inesperados que mudam suas vidas para sempre.
              </p>
              <button className='mt-4 w-full bg-gray-700 hover:bg-gray-600 text-white py-2 px-4 rounded-full text-sm transition'>Assistir Trailer</button>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Avaliacao;
