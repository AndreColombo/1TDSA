import type React from "react";

type BotaoProps = {
  cor?: string; // cor do botão, o caracter '?' deixa a prop opcional e não mais obrigatória.
  texto?: string; // texto do botão
  onClick?: () => void; // evento sem retorno
};

const Botao: React.FC<BotaoProps> = ({ cor = "blue", texto = "Clique aqui!", onClick }) => {
  return (
    <>
      <button style={{ backgroundColor: cor }} onClick={onClick}>
        {texto}
      </button>
    </>
  );
};

export default Botao;
