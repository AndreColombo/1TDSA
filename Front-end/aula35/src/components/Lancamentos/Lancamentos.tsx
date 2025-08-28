const Lancamentos = () => {
  return (
    <>
      {/* <!-- Upcoming Movies --> */}
      <section className='mb-16'>
        <div className='flex justify-between items-center mb-8'>
          <h2 className='text-2xl md:text-3xl font-bold'>Próximos Lançamentos</h2>
          <a href='#' className='text-red-400 hover:text-red-300 flex items-center'>
            Ver todos <i className='fas fa-chevron-right ml-2'></i>
          </a>
        </div>

        <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6'>
          {/* <!-- Upcoming Movie 1 --> */}
          <div className='bg-gray-800 rounded-lg overflow-hidden shadow-lg flex'>
            <div className='w-1/3'>
              <img src='imagens/iADOJ8Zymht2JPMoy3R7xceZprc.webp' alt='Furiosa' className='w-full h-full object-cover' />
            </div>
            <div className='w-2/3 p-4 flex flex-col'>
              <h3 className='font-bold text-lg mb-1'>Furiosa: Uma Saga Mad Max</h3>
              <span className='text-yellow-400 text-sm mb-2'>
                <i className='fas fa-calendar-alt mr-1'></i> 23 de Maio, 2024
              </span>
              <div className='flex flex-wrap gap-2 mb-3'>
                <span className='genre-tag text-xs bg-red-900/50 text-red-300 px-2 py-1 rounded-full'>Ação</span>
                <span className='genre-tag text-xs bg-gray-900/50 text-gray-300 px-2 py-1 rounded-full'>Ficção Científica</span>
              </div>
              <p className='text-gray-400 text-sm line-clamp-3'>A história da jovem Imperatriz Furiosa antes de conhecer Max Rockatansky.</p>
              <button className='mt-auto bg-red-600 hover:bg-red-700 text-white py-2 px-4 rounded-full text-sm transition'>+ Minha Lista</button>
            </div>
          </div>

          {/* <!-- Upcoming Movie 2 --> */}
          <div className='bg-gray-800 rounded-lg overflow-hidden shadow-lg flex'>
            <div className='w-1/3'>
              <img src='imagens/xq4v7JE8niZ75OYYPDGNn6Gzpyt.webp' alt='Deadpool & Wolverine' className='w-full h-full object-cover' />
            </div>
            <div className='w-2/3 p-4 flex flex-col'>
              <h3 className='font-bold text-lg mb-1'>Deadpool & Wolverine</h3>
              <span className='text-yellow-400 text-sm mb-2'>
                <i className='fas fa-calendar-alt mr-1'></i> 25 de Julho, 2024
              </span>
              <div className='flex flex-wrap gap-2 mb-3'>
                <span className='genre-tag text-xs bg-red-900/50 text-red-300 px-2 py-1 rounded-full'>Ação</span>
                <span className='genre-tag text-xs bg-blue-900/50 text-blue-300 px-2 py-1 rounded-full'>Comédia</span>
                <span className='genre-tag text-xs bg-purple-900/50 text-purple-300 px-2 py-1 rounded-full'>Ficção Científica</span>
              </div>
              <p className='text-gray-400 text-sm line-clamp-3'>Deadpool muda a história do MCU ao se juntar a Wolverine em uma jornada que vai desafiar o multiverso.</p>
              <button className='mt-auto bg-red-600 hover:bg-red-700 text-white py-2 px-4 rounded-full text-sm transition'>+ Minha Lista</button>
            </div>
          </div>

          {/* <!-- Upcoming Movie 3 --> */}
          <div className='bg-gray-800 rounded-lg overflow-hidden shadow-lg flex'>
            <div className='w-1/3'>
              <img src='imagens/jNttwl5CYgnxNwQ8157BxyYJqu2.webp' alt='Joker 2' className='w-full h-full object-cover' />
            </div>
            <div className='w-2/3 p-4 flex flex-col'>
              <h3 className='font-bold text-lg mb-1'>Joker: Folie à Deux</h3>
              <span className='text-yellow-400 text-sm mb-2'>
                <i className='fas fa-calendar-alt mr-1'></i> 3 de Outubro, 2024
              </span>
              <div className='flex flex-wrap gap-2 mb-3'>
                <span className='genre-tag text-xs bg-purple-900/50 text-purple-300 px-2 py-1 rounded-full'>Drama</span>
                <span className='genre-tag text-xs bg-pink-900/50 text-pink-300 px-2 py-1 rounded-full'>Musical</span>
                <span className='genre-tag text-xs bg-gray-900/50 text-gray-300 px-2 py-1 rounded-full'>Thriller</span>
              </div>
              <p className='text-gray-400 text-sm line-clamp-3'>
                Arthur Fleck encontra Harley Quinn em Arkham Asylum e sua loucura se transforma em um romance distorcido.
              </p>
              <button className='mt-auto bg-red-600 hover:bg-red-700 text-white py-2 px-4 rounded-full text-sm transition'>+ Minha Lista</button>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Lancamentos;
