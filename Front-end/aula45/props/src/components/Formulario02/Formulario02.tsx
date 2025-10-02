import { useForm, type SubmitHandler } from "react-hook-form";

type FormValues = {
  nome: string;
  email: string;
  senha: string;
  confSenha: string;
  genero: string;
  pais: string;
  termos: string;
};

const Formulario02 = () => {
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
      <h1>Formulário 02</h1>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div>
          <label>Nome</label>
          <input
            type='text'
            {...register("nome", {
              required: "O nome é obrigatório!",
            })}
          />
          {errors.nome && <span style={{ color: "red" }}>{errors.nome.message}</span>}
        </div>
        <div>
          <label>Email</label>
          <input
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
        <div>
          <label>Senha</label>
          <input
            type='password'
            {...register("senha", {
              required: "A senha é obrigatória!",
              minLength: { value: 6, message: "Mínimo de 6 caracteres" },
              validate: (value) =>
                !/[A-Z]/.test(value)
                  ? "Deve conter uma letra maiúscula"
                  : !/[a-z]/.test(value)
                  ? "Deve conter uma letra minúscula"
                  : !/\d/.test(value)
                  ? "Deve conter um número"
                  : !/[A-Za-z0-9]/.test(value)
                  ? "Deve conter um caracter especial"
                  : true,
            })}
          />
          {errors.senha && <span style={{ color: "red" }}>{errors.senha.message}</span>}
        </div>
        <div>
          <label>Confirmação da senha</label>
          <input />
        </div>
        <div>
          <label>País</label>
          <select>
            <option> Brasil</option>
            <option> EUA</option>
            <option> Japão</option>
            <option> Portugal</option>
          </select>
        </div>
        <div>
          <label>Genero</label>
          <input />
          Masculino
          <input />
          Feminino
        </div>
        <div>
          <label>Aceito</label>
          <input />
        </div>
        <button type='submit'>Enviar</button>
      </form>
    </>
  );
};

export default Formulario02;
