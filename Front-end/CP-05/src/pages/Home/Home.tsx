import { useEffect } from "react";
import CategoriaSection from "../../components/CategoriaSection/CategoriaSection";
import Header from "../../components/Header/Header";

export default function Home() {
  useEffect(() => {
    document.title = "Livro de receitas - Sabores do Front";
  });
  return (
    <>
      <Header titulo='Sabores do Front' />
      <div className='relative md:h-96 flex items-center justify-center'>
        <div className='absolute inset-0 bg-black opacity-30' />
        <h1 className='absolute font-light italic text-4xl md:text-5xl lg:text-7xl xl:text-8xl text-[#F3F4F6] select-none'>Receitas à Milaneza</h1>
        <img src='/milaneza.png' className='w-full md:h-96 object-cover' />
      </div>
      <div className='py-6'>
        <CategoriaSection categoria='entradas' />
        <CategoriaSection categoria='pratos_principais' />
        <CategoriaSection categoria='sobremesas' />
        <CategoriaSection categoria='bebidas' />
      </div>
    </>
  );
}
