import { useState } from "react";

const Exemplo02 = () => {
  const [countA, setCountA] = useState(0);
  return (
    <>
      <h2>Exemplo 2 - Habilitar/Desabilitar botões</h2>
      <p>Contador A: {countA}</p>
      <button onClick={() => setCountA(countA + 1)} disabled={countA >= 10}>
        Incrementar
      </button>
      <button onClick={() => setCountA(countA - 1)} disabled={countA == 0}>
        Decrementar
      </button>
      <button onClick={() => setCountA(0)}>Reset</button>
    </>
  );
};

export default Exemplo02;
