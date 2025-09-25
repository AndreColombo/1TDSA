import { useState } from "react";

const Exemplo04 = () => {
  const [nome, setNome] = useState("");
  const [nomeExibido, setNomeExibido] = useState("");

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setNome(event.target.value);
  };
  const handleSubmit = () => {
    setNomeExibido(nome);
    setNome("");
  };
  return (
    <>
      <h1>Exemplo 4 - Formulário 02: Exibe a modificação somente após clicar no botão</h1>
      <form onSubmit={(e) => e.preventDefault()}>
        <label>Nome: </label>
        <input type='text' value={nome} onChange={handleChange} />
        <button onClick={handleSubmit}>Enviar</button>
        {nomeExibido && <p>O nome digitado é: {nomeExibido}</p>}
      </form>
    </>
  );
};

export default Exemplo04;
