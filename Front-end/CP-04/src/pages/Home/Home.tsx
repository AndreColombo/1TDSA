import livros from "../../livros.json";
import Card from "../../components/Card/Card";
import { useEffect } from "react";

export default function Home() {
  let livrosLiteraturaBrasileira = livros.filter((livro) => {
    return livro.categoria == "Literatura Brasileira";
  });
  let livrosFilosofia = livros.filter((livro) => {
    return livro.categoria == "Filosofia";
  });

  useEffect(() => {''
    document.title = "Home";
  });
  return (
    <>
      <div className='flex flex-col p-5 gap-3'>
        <h2 className='text-3xl font-bold'>Literatura Brasileira</h2>
        <section className='max-w-full flex items-center px-10 gap-10'>
          {livrosLiteraturaBrasileira.map((livro) => {
            return (
              <Card key={livro.id} id={livro.id} titulo={livro.titulo} sinopse={livro.sinopse} num_paginas={livro.num_paginas} autor={livro.autor} capa={livro.capa} />
            );
          })}
        </section>
        <h2 className='text-3xl font-bold'>Filosofia</h2>
        <section className='max-w-full flex items-center px-10 gap-10'>
          {livrosFilosofia.map((livro) => {
            return (
              <Card key={livro.id} id={livro.id} titulo={livro.titulo} sinopse={livro.sinopse} num_paginas={livro.num_paginas} autor={livro.autor} capa={livro.capa} />
            );
          })}
        </section>
      </div>
    </>
  );
}
