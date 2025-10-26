import { Link } from "react-router-dom";

import type { CardProps } from "../../Types/CardTipos";

export default function Card({ link, nome, tempo, src }: CardProps) {
  return (
    <Link to={`/receita/${link}`} className='relative aspect-3/4 lg:aspect-2/3 rounded-xl shadow-xl'>
      <div className='absolute bottom-0 left-0 right-0 top-1/3 bg-linear-to-t from-black rounded-xl z-10' />
      <img src={src} className='h-full object-cover rounded-xl z-0' />
      <div className='absolute bottom-3 left-3 flex flex-col gap-1 lg:gap-3 z-20'>
        <h3 className='text-xl md:text-2xl lg:text-3xl text-[#F3F4F6] font-medium line-clamp-1'>{nome}</h3>
        <div className='flex items-center gap-2'>
          <img src='/icons/clock-cinza.svg' alt='ícone de relógio' className='h-4 lg:h-5 xl:h-6' />
          <p className='lg:text-xl text-[#9CA3AF]'>{tempo}</p>
        </div>
      </div>
    </Link>
  );
}
