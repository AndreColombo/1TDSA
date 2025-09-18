import { useEffect, useState } from "react";

const Exemplo02 = () => {
  const frases = [
    "Frase 01: A persistência é o caminho do êxito.",
    "Frase 02: A vida trará coisas boas se tiveres paciência.",
    "Frase 03: Dificuldades são oportunidades para se mostrar o que sabe.",
    "Frase 04: Não existe um caminho para a felicidade. A felicidade é o caminho.",
    "Frase 05: O que você faz hoje pode melhorar todos os seus amanhãs.",
    "Frase 06: Código limpo é MENTE FELIZ.",
  ];

  const [indice, setIndice] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setIndice((indice) => (indice + 1) % frases.length);
    }, 3000);
    return () => clearInterval(timer);
  }, [frases.length]);

  return (
    <>
      <h1>Exemplo 2 - Exibe mensagens após um período de tempo</h1>
      <p>{frases[indice]}</p>
    </>
  );
};

export default Exemplo02;
