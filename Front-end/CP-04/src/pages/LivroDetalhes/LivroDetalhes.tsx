import { useParams } from "react-router-dom";
import livros from "../../livros.json";
import { useEffect } from "react";

const LivroDetalhes = () => {
  const { id } = useParams();

  const identificador = Number(id);

  const livroAtual = livros.find((livrinho) => livrinho.id === identificador);

  console.log("LIVRO: " + livroAtual);

  if (livroAtual == undefined) return <div />;

  useEffect(() => {
    document.title = "Detalhes do Livro";
  });

  return (
    <section className='w-screen h-full flex items-center justify-around' key={id}>
      <img className='h-4/5 w-[45%]' src={"../../../public/" + livroAtual.capa} alt={"Capa do Livro " + livroAtual.titulo} />
      <div className='h-4/5 w-[45%] flex flex-col justify-start gap-[16px]'>
        <h2 className='font-bold text-black text-2xl'>{livroAtual.titulo}</h2>
        <p className='text-black text-base text-xl'>{livroAtual.sinopse}</p>
        <div className='w-full flex justify-start gap-[12px] items-center'>
          <div className='text-lg'>
            <strong>Autor: </strong> {livroAtual.autor}
          </div>
          <div className='text-lg'>
            <strong>Páginas: </strong> {livroAtual.num_paginas}
          </div>
        </div>
      </div>
    </section>
  );
};

export default LivroDetalhes;
