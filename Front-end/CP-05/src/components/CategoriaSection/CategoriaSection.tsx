import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import type { CardProps } from "../../Types/CardTipos";
import { BuscarReceitas } from "../../Services/Services";
import Card from "../Card/Card";

export default function CategoriaSection({ categoria }: { categoria: string }) {
  const [receitas, setReceitas] = useState<CardProps[]>([]);

  useEffect(() => {
    BuscarReceitas().then((data) => setReceitas(data));
  }, []);

  const formatarCategoria = (categoria: string) => {
    return categoria.replace("_", " ").replace(/\b\w/g, (l) => l.toUpperCase());
  };

  const categoriaSelecionada = categoria ?? "";

  const receitas_categoria = receitas.filter((receita) => receita.categoria === categoriaSelecionada);
  return (
    <section className='px-6 lg:px-10 py-4 lg:py-6 flex flex-col gap-4 lg:gap-6'>
      <div className='flex justify-between items-end'>
        <h2 className='font-bold italic text-[#1F2937] text-2xl md:text-3xl lg:text-4xl'>{formatarCategoria(categoriaSelecionada)}</h2>
        <Link to={`/categoria/${categoria}`} className='text-[#F59E0B] hover:text-[#D97706] underline md:text-lg lg:text-xl'>
          Ver tudo
        </Link>
      </div>
      <div className='px-2.5 grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-8'>
        {receitas_categoria.slice(0, 6).map((receita) => (
          <Card key={receita.link} src={receita.src} nome={receita.nome} tempo={receita.tempo} link={receita.link} />
        ))}
      </div>
    </section>
  );
}
