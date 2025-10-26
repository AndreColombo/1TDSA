import { useEffect } from "react";
import { Link } from "react-router-dom";

export default function NotFound() {
  useEffect(() => {
    document.title = "Página não Encontrada";
  });
  return (
    <div className='flex flex-col items-center justify-center h-full gap-12'>
      <div className='flex flex-col md:flex-row gap-6 items-center justify-center w-[90%]'>
        <img src='/icons/chef-hat.svg' className='h-16 select-none' />
        <h1 className='text-4xl md:text-5xl lg:text-7xl xl:text-8xl text-[#F59E0B] font-semibold text-center md:text-start'>Página não encontrada</h1>
      </div>
      <h2 className='text-xl md:text-2xl lg:text-[1.7rem] xl:text-3xl text-[#1F2937] w-[90%] text-center'>
        Parece que você entrou em uma página que não existe, volte e tente novamente
      </h2>
      <Link to='/' className='bg-[#F59E0b] px-4 py-2 rounded-lg text-[#F3F4F4] text-xl font-medium'>
        Voltar para a tela inicial
      </Link>
    </div>
  );
}
