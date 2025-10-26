import { Link } from "react-router-dom";

export default function Header({ titulo }: { titulo?: string }) {
  return (
    <header className='w-full px-10 md:px-14 lg:px-32 py-6 flex justify-between bg-[#F59E0B] text-[#F3F4F6]'>
      <h1 className='font-bold text-xl md:text-2xl lg:text-3xl xl:text-4xl'>{titulo}</h1>
      <ul className='flex gap-4 lg:gap-12 font-medium md:text-xl lg:text-2xl items-center'>
        <li className='hover:text-[#D1D5DB] underline'>
          <Link to='/'>Início</Link>
        </li>
        <li className='hover:text-[#D1D5DB] underline'>
          <Link to='/login'>Login</Link>
        </li>
      </ul>
    </header>
  );
}
