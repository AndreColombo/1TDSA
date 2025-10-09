import { useEffect, useCallback } from "react";
import { useForm, type SubmitHandler } from "react-hook-form";

type FormValues = {
  nome: string;
  email: string;
  senha: string;
  confSenha: string;
  genero: string;
  pais: string;
  termos: string;
  cep: string;
  logradouro: string;
  numero: string;
  bairro: string;
  cidade: string;
  uf: string;
};

const Formulario02 = () => {
  const {
    register,
    handleSubmit,
    watch,
    setFocus,
    setValue,
    formState: { errors },
  } = useForm<FormValues>();

  const senha = watch("senha");
  const cep = watch("cep");

  const onSubmit: SubmitHandler<FormValues> = (data) => {
    console.log(data);
  };

  const buscarEndereco = useCallback(
    async (cep: string) => {
      if (cep.length === 8) {
        try {
          const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
          const dados = await response.json();

          setValue("logradouro", dados.logradouro);
          setValue("bairro", dados.bairro);
          setValue("cidade", dados.localidade);
          setValue("uf", dados.uf);
          setFocus("numero");
        } catch (error) {
          console.error("Erro ao buscar o endereço: ", error);
        }
      }
    },
    [setValue, setFocus]
  );

  useEffect(() => {
    if (cep && cep.length === 8) {
      buscarEndereco(cep);
    }
  }, [cep, buscarEndereco]);

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
          <input
            type='password'
            {...register("confSenha", {
              required: "A confirmação de senha é obrigatória",
              minLength: { value: 6, message: "Mínimo de 6 caracteres" },
              validate: (value) => value === senha || "As senhas não coincidem",
            })}
          />
          {errors.confSenha && <span style={{ color: "red" }}>{errors.confSenha.message}</span>}
        </div>
        <div>
          <label>País</label>
          <select
            {...register("pais", {
              required: "O país é obrigatório",
            })}>
            <option value=''>Selecione</option>
            <option value='BR'>Brasil</option>
            <option value='USA'>EUA</option>
            <option value='JP'>Japão</option>
            <option value='PT'>Portugal</option>
          </select>
          {errors.pais && <span style={{ color: "red" }}>{errors.pais.message}</span>}
        </div>
        <div>
          <label>Gênero</label>
          <input
            type='radio'
            value='masculino'
            id='generoMasculino'
            {...register("genero", {
              required: "O gênero é obrigatório",
            })}
          />
          <label htmlFor='generoMasculino'>Masculino</label>
          <input
            type='radio'
            value='feminino'
            id='generoFeminino'
            {...register("genero", {
              required: "O gênero é obrigatório",
            })}
          />
          <label htmlFor='generoFeminino'>Feminino</label>
          {errors.genero && <span style={{ color: "red" }}>{errors.genero.message}</span>}
        </div>
        <div>
          <label>Aceite de Termos</label>
          <input
            type='checkbox'
            {...register("termos", {
              required: "Você deve aceitar os termos",
            })}
          />
          {errors.termos && <span style={{ color: "red" }}>{errors.termos.message}</span>}
        </div>
        <div>
          <label>CEP</label>
          <input
            type='text'
            maxLength={8}
            {...register("cep", {
              required: "O CEP é obrigatório",
              validate: (value) => (value.length !== 8 ? "O CEP deve ter 8 caracteres" : !/^[0-9]+$/.test(value) ? "O CEP deve conter apenas números" : true),
            })}
          />
          {errors.cep && <span style={{ color: "red" }}>{errors.cep.message}</span>}
        </div>
        <div>
          <label>Endereço</label>
          <input type='text' {...register("logradouro")} readOnly />
        </div>
        <div>
          <label>Numero</label>
          <input type='text' {...register("numero")} />
        </div>
        <div>
          <label>Bairro</label>
          <input type='text' {...register("bairro")} readOnly />
        </div>
        <div>
          <label>Cidade</label>
          <input type='text' {...register("cidade")} readOnly />
        </div>
        <div>
          <label>UF</label>
          <input type='text' {...register("uf")} readOnly />
        </div>
        <button type='submit'>Enviar</button>
      </form>
    </>
  );
};
export default Formulario02;
