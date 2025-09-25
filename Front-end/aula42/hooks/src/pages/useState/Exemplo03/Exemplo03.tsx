import { useState } from "react";

const Exemplo03 = () => {
  const [nome, setNome] = useState("");

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setNome(event.target.value);
  };
  return (
    <>
      <h1>Exemplo 3 - Formulário 01: Exibe a modificação enquanto o valor é digitado</h1>
      <form>
        <label>Nome: </label>
        <input type='text' onChange={handleChange} />
        <p>O nome digitado é: {nome}</p>
      </form>
    </>
  );
};

export default Exemplo03;
