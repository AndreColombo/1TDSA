import { useState } from "react";

const Exemplo01 = () => {
  const [count, setCount] = useState(0);

  return (
    <>
      <h1>Exemplo 1 - Contador</h1>
      <p>Contador: {count}</p>
      <button onClick={() => setCount(count + 1)}>Incrementar</button>
      <button onClick={() => setCount(count - 1)}>Decrementar</button>
    </>
  );
};

export default Exemplo01;
