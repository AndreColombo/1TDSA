import { Link } from "react-router-dom";

interface LivroProps {
  id: number;
  titulo: string;
  sinopse: string;
  num_paginas: number;
  autor: string;
  capa: string;
}

const Card: React.FC<LivroProps> = ({ id, titulo, sinopse, num_paginas, autor, capa }) => {
  return (
    <div key={id} className='flex flex-col justify-center gap-[8px] w-[230px] bg-gray-300 p-3 rounded-lg'>
      <Link to={`/livro/${id}`}>
        <img className='' src={"../../../public/" + capa} alt={"Capa do Livro " + titulo} />
        <h3 className='text-black font-semibold text-lg'>{titulo}</h3>
        <p className='text-justify text-black line-clamp-4'>{sinopse}</p>
      </Link>
    </div>
  );
};
export default Card;
