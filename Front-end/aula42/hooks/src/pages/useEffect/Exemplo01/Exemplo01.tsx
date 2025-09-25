import { useEffect, useState } from "react";

const Exemplo01 = () => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Você clicou ${count} vezes`;
  }, [count]);

  return (
    <>
      <h1>Exemplo 1 - Contador: Exibe a modificação, na barra de título do navegador página, após clicar no botão</h1>
      <p>Você clicou {count} vezes.</p>
      <button onClick={() => setCount(count + 1)}>Clique Aqui</button>
    </>
  );
};

export default Exemplo01;
