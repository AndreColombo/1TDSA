import { Link, useParams } from "react-router-dom";
import produtos from "../../data/produtos.json";

const ProdutoDetalhes = () => {
  const { id } = useParams();
  const produto = produtos.find((p) => p.id === Number(id));
  if (!produto) {
    return (
      <>
        <section className='px-8 py-16 mas-w-7x1 mx-auto text-center'>
          <h1 className='text-3xl font-bold mb-4'>Produto não encontrado!</h1>
        </section>
      </>
    );
  }
  return (
    <>
      <section className='px-8 py-16 mas-w-7x1 mx-auto'>
        <div className='bg-white shadow-md rounded-lg p-6'>
          <h1 className='text-3xl font-bold mb-4'>{produto.titulo}</h1>
          <p>{produto.descricao}</p>
          <p>
            <Link to='/' className='text-blue-500 underline'>
              Voltar
            </Link>
          </p>
        </div>
      </section>
    </>
  );
};

export default ProdutoDetalhes;
