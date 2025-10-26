import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import type { CardProps } from "../../Types/CardTipos";
import { BuscarReceitas } from "../../Services/Services";
import Card from "../../components/Card/Card";

export default function Categoria() {
  const voltar = useNavigate();
  const { categoria } = useParams();
  const [receitas, setReceitas] = useState<CardProps[]>([]);

  useEffect(() => {
    document.title = `Categoria | ${categoria?.replace("_", " ").replace(/\b\w/g, (l) => l.toUpperCase())}`;
  });

  useEffect(() => {
    BuscarReceitas().then((data) => setReceitas(data));
  }, []);

  const formatarCategoria = (categoria: string) => {
    return categoria.replace("_", " ").replace(/\b\w/g, (l) => l.toUpperCase());
  };

  const categoriaSelecionada = categoria ?? "";

  const receitas_categoria = receitas.filter((receita) => receita.categoria === categoriaSelecionada);

  return (
    <>
      <div className='w-full h-auto py-6 flex justify-center bg-[#F59E0B]'>
        <Link
          to=''
          onClick={(e) => {
            e.preventDefault();
            voltar(-1);
          }}>
          <img src='/icons/chevron-left-branco.svg' className='absolute left-5 md:left-8 lg:left-10 top-8 lg:h-8' />
        </Link>
        <h2 className='text-3xl md:text-4xl xl:text-5xl text-[#F3F4F6] font-bold'>{formatarCategoria(categoriaSelecionada)}</h2>
      </div>
      <div className='px-8 lg:px-13 py-12 grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-8'>
        {receitas_categoria.map((receita) => (
          <Card key={receita.link} src={receita.src} nome={receita.nome} tempo={receita.tempo} link={receita.link} />
        ))}
      </div>
    </>
  );
}
