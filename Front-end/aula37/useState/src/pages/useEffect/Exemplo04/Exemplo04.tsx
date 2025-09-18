import { useEffect, useState } from "react";

const Exemplo04 = () => {
  const [largura, setLargura] = useState(window.innerWidth);

  useEffect(() => {
    const atualizarLargura = () => setLargura(window.innerWidth);
    window.addEventListener("resize", atualizarLargura);
    return () => {
      window.removeEventListener("resize", atualizarLargura);
    };
  });

  return (
    <>
      <h1>Exemplo 4 - Detectar e exibir a largura da tela</h1>
      <p>Largura da tela {largura}px</p>
    </>
  );
};
export default Exemplo04;
