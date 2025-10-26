import { useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useForm, type SubmitHandler } from "react-hook-form";
import Header from "../../components/Header/Header";

type FormValues = {
  nome: string;
  email: string;
  senha: string;
  confSenha: string;
  termos: string;
};

const requisitosSenha = [
  { message: "Mínimo de 6 caracteres", test: (val: string) => val?.length >= 6 },
  { message: "Deve conter uma letra maiúscula", test: (val: string) => /[A-Z]/.test(val) },
  { message: "Deve conter uma letra minúscula", test: (val: string) => /[a-z]/.test(val) },
  { message: "Deve conter um número", test: (val: string) => /\d/.test(val) },
  { message: "Deve conter um caracter especial", test: (val: string) => /[^A-Za-z0-9]/.test(val) },
];

export default function Login() {
  const voltar = useNavigate();

  useEffect(() => {
    document.title = "Login";
  });

  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<FormValues>();

  const senha = watch("senha");

  const onSubmit: SubmitHandler<FormValues> = (data) => {
    console.log(data);
  };

  return (
    <>
      <Header titulo='Login' />
      <Link
        to=''
        onClick={(e) => {
          e.preventDefault();
          voltar(-1);
        }}>
        <img src='/icons/chevron-left-branco.svg' className='absolute left-4 md:left-6 lg:left-10 top-6 md:top-7 lg:h-8' />
      </Link>
      <div className='flex flex-col items-center py-12 gap-6'>
        <form onSubmit={handleSubmit(onSubmit)} className='flex flex-col gap-5 w-[90%] md:w-[80%] lg:w-[60%] xl:w-[45%]'>
          <div className='flex flex-col'>
            <label htmlFor='email' className='text-xl text-[#1F2937] font-semibold'>
              Email
            </label>
            <input
              id='email'
              type='email'
              autoComplete='username'
              placeholder='seuemail@exemplo.com.br'
              {...register("email", {
                required: "O email é obrigatório!",
                pattern: {
                  value: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
                  message: "Digite um email correto",
                },
              })}
              className='text-[#4B5563] placeholder-[#9CA3AF] text-xl px-2 py-1 m-2 outline-none border-2 border-[#FBBF24] focus:border-[#D97706] invalid:border-[#EF4444] rounded-md'
            />
            {errors.email && <span style={{ fontSize: "1.15rem", color: "#EF4444" }}>{errors.email.message}</span>}
          </div>
          <div className='flex flex-col'>
            <label htmlFor='senha' className='text-xl text-[#1F2937] font-semibold'>
              Senha
            </label>
            <input
              id='senha'
              type='password'
              autoComplete='current-password'
              {...register("senha", {
                required: "A senha é obrigatória!",
              })}
              className='text-[#4B5563] text-xl px-2 py-1 m-2 outline-none border-2 border-[#FBBF24] focus:border-[#D97706] rounded-md'
            />
            {errors.senha && <span style={{ fontSize: "1.15rem", color: "#EF4444" }}>{errors.senha.message}</span>}
            <ul>
              {requisitosSenha.map((req) => (
                <li key={req.message} style={{ color: req.test(senha) ? "#22C55E" : "#EF4444" }} className='ml-10 list-disc'>
                  {req.message}
                </li>
              ))}
            </ul>
          </div>
          <button type='submit' className='bg-[#F59E0B] hover:bg-[#FBBF24] focus:bg-[#D97706] w-40 px-3 py-1.5 rounded-lg text-[#F3F4F4] text-lg font-medium self-end'>
            Efetuar Login
          </button>
        </form>
        <p>
          Não possui conta?{" "}
          <Link to='/cadastro' className='text-[#F59E0B]'>
            Crie um aqui
          </Link>
        </p>
      </div>
    </>
  );
}
