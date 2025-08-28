import Destaques from "../../components/Destaques/Destaques";
import Lancamentos from "../../components/Lancamentos/Lancamentos";
import Avaliacao from "../../components/Avaliacao/Avaliacao";

const Home = () => {
  return (
    <>
      <section className='hero-section flex items-center pt-16'>
        <div className='container mx-auto px-4'>
          <div className='max-w-2xl'>
            <h1 className='text-4xl md:text-6xl font-bold mb-4 animate-fade-in' style={{ animationDelay: "0.1s" }}>
              Explore o Universo do Cinema
            </h1>
            <p className='text-lg md:text-xl mb-8 text-gray-300 animate-fade-in' style={{ animationDelay: "0.3s" }}>
              Descubra os melhores filmes, críticas e trailers em um só lugar.
            </p>

            <div className='relative max-w-xl animate-fade-in' style={{ animationDelay: "0.5s" }}>
              <input
                type='text'
                placeholder='Pesquisar filmes...'
                className='w-full py-3 px-5 pr-12 rounded-full search-input focus:outline-none focus:ring-2 focus:ring-red-500'
              />
              <button className='absolute right-3 top-1/2 transform -translate-y-1/2 text-red-500'>
                <i className='fas fa-search'></i>
              </button>
            </div>
          </div>
        </div>
      </section>
      <main className='container mx-auto px-4 py-12'>
        <Destaques />
        <Lancamentos />
        <Avaliacao />
      </main>
    </>
  );
};

export default Home;
