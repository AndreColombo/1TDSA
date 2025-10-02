import { useForm, type SubmitHandler } from "react-hook-form";

type FormValues = {
  nome: string;
  sobrenome: string;
};

const Formulario01 = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormValues>();

  const onSubmit: SubmitHandler<FormValues> = (data) => {
    console.log(data);
  };

  return (
    <>
      <h1>Formulário 01</h1>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div>
          <label>Nome</label>
          <input {...register("nome", { required: true })} />
          {errors.nome && <span>Nome é obrigatório!</span>}
        </div>
        <div>
          <label>Sobrenome</label>
          <input {...register("sobrenome", { required: true })} />
          {errors.nome && <span>Sobrenome é obrigatório!</span>}
        </div>
        <button type='submit'>Enviar</button>
      </form>
    </>
  );
};

export default Formulario01;
