import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import type { CardProps } from "../../Types/CardTipos";
import { BuscarReceitas } from "../../Services/Services";
import Header from "../../components/Header/Header";

export default function Receita() {
  const voltar = useNavigate();
  const { link } = useParams();
  const [receita, setReceita] = useState<CardProps | null>(null);

  useEffect(() => {
    document.title = `Receita | ${receita?.nome}`;
  });

  useEffect(() => {
    BuscarReceitas().then((data) => {
      const encontrado = data.find((p: CardProps) => p.link === link);
      setReceita(encontrado || null);
    });
  }, [link]);

  const formatarTempo = (tempo: string | undefined): string => {
    return tempo ? tempo.replace("min", " minutos").replace("h", " hora(s)") : "";
  };

  return (
    <>
      <Header titulo='Sabores do Front' />
      <Link
        to=''
        onClick={(e) => {
          e.preventDefault();
          voltar(-1);
        }}>
        <img src='/icons/chevron-left-branco.svg' className='absolute left-4 md:left-6 lg:left-10 top-6 md:top-7 lg:h-8' />
      </Link>
      <div className='relative h-52 md:h-96 flex items-center justify-center'>
        <div className='absolute inset-0 bg-black opacity-30 z-10' />
        <img src={receita?.src} className='w-full h-52 md:h-96 object-cover z-0' />
      </div>
      <div className='flex flex-col px-3 gap-5 md:gap-8 lg:gap-12 py-12'>
        <div className='px-4 lg:px-10 flex flex-col lg:flex-row gap-4 justify-between'>
          <h1 className='text-3xl md:text-4xl lg:text-5xl xl:text-6xl text-[#1F2937] font-bold'>{receita?.nome}</h1>
          <div className='flex items-center gap-2.5'>
            <img src='/icons/clock-amarelo.svg' className='md:h-7 mt-1' />
            <h3 className='text-[#F59E0B] text-xl md:text-2xl lg:text-3xl xl:text-4xl font-semibold text-end'>{formatarTempo(receita?.tempo)}</h3>
          </div>
        </div>
        <section className='px-4 lg:px-10'>
          <div className='px-2.5 flex flex-col gap-3'>
            <h2 className='font-semibold italic text-2xl md:text-3xl lg:text-4xl xl:text-5xl text-[#4B5563]'>Ingredientes</h2>
            <ul className='px-5 text-[#6B7280] text-lg md:text-2xl font-medium italic'>
              {receita?.ingredientes?.map((ingrediente) => (
                <li key={ingrediente} className='list-disc'>
                  {ingrediente}
                </li>
              ))}
            </ul>
          </div>
        </section>
        <section className='px-4 lg:px-10'>
          <div className='px-2.5 flex flex-col gap-3'>
            <h2 className='font-semibold italic text-2xl md:text-3xl lg:text-4xl xl:text-5xl text-[#4B5563]'>Modo de Preparo</h2>
            <ul className='px-5 text-[#6B7280] text-lg md:text-2xl font-medium italic'>
              {receita?.modoPreparo?.map((etapa) => (
                <li key={etapa} className='list-disc'>
                  {etapa}
                </li>
              ))}
            </ul>
          </div>
        </section>
      </div>
    </>
  );
}
