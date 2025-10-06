import { useEffect } from "react";
import { useForm, type SubmitHandler } from "react-hook-form";

type FormValues = {
  nome: string;
  email: string;
  titulo: string;
  Mensagem: string;
};

export default function Contato() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormValues>();

  const onSubmit: SubmitHandler<FormValues> = (data) => {
    console.log(data);
  };

  useEffect(() => {
    document.title = "Contato";
  });

  return (
    <>
      <section className='flex flex-col m-auto pt-10 gap-3 w-[60%]'>
        <h2 className='text-2xl font-bold mb-4'>Contato</h2>
        <p>Bem-vindo à página de Contato. Aqui você pode encontrar nossas informações de contato.</p>
        <form className='flex flex-col gap-3' onSubmit={handleSubmit(onSubmit)}>
          <div className='flex gap-2'>
            <label className='text-xl font-semibold'>Nome:</label>
            <input
              className='border-b-2 border-black'
              type='text'
              {...register("nome", {
                required: "O nome é obrigatório!",
              })}
            />
            {errors.nome && <span style={{ color: "red" }}>{errors.nome.message}</span>}
          </div>
          <div className='flex gap-2'>
            <label className='text-xl font-semibold'>Email:</label>
            <input
              className='border-b-2 border-black'
              type='email'
              {...register("email", {
                required: "O email é obrigatório",
                pattern: {
                  value: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
                  message: "Digite um email correto",
                },
              })}
            />
            {errors.email && <span style={{ color: "red" }}>{errors.email.message}</span>}
          </div>
          <div className='flex gap-2'>
            <label className='text-xl font-semibold'>Titulo:</label>
            <input className='border-b-2 border-black' type='titulo' />
          </div>
          <div className='flex gap-2'>
            <label className='text-xl font-semibold'>Mensagem:</label>
            <textarea className='border-2 rounded-md border-black' />
          </div>
          <button
            type='submit'
            className='w-24 self-end font-semibold text-white bg-gray-800 hover:bg-gray-700 focus:outline-none focus:bg-gray-900 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 '>
            Enviar
          </button>
        </form>
      </section>
    </>
  );
}
