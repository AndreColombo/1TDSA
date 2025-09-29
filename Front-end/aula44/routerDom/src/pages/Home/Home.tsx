import { Link } from "react-router-dom";
import Card from "../../components/Card/Card";
import produtos from "../../data/produtos.json";

const Home = () => {
  return (
    <>
      <h2 className='text-2xl font-bold mb-4'>Página Home</h2>
      <main className='flex-1 container mx-auto p-6'>
        <div className='grid grid-cols-3 gap-6'>
          {produtos.map((produto) => (
            <Card key={produto.id}>
              <h2 className='font-semibold'>{produto.titulo}</h2>
              <p>{produto.descricao}</p>
              <Link to={`/ProdutoDetalhes/${produto.id}`} className='underline'>
                Ver detalhes
              </Link>
            </Card>
          ))}
        </div>
      </main>
    </>
  );
};

export default Home;
