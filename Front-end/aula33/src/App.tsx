import Botao from "./components/Botao/Botao";
import Mensagem from "./components/Mensagem/Mensagem";
import Alerta from "./components/Alerta/Alerta";

import Homer from "./assets/imagens/homer.png";

const App = () => {
  return (
    <>
      <Alerta />

      <Mensagem />
      <Mensagem />
      <Mensagem />
      <Mensagem />
      <Mensagem />

      <Botao texto='Botão' />
      <Botao texto='Clique Aqui!' />
      <Botao texto='Gravar' />
      <Botao texto='Excluir' />
      <Botao texto='Avançar' />
      <Botao texto='Sair' />

      <br />

      <img src='/imagens/bart.png' alt='Bart Simpson' />
      {/* inserindo imagens a partir da pasta public */}
      <img src={Homer} alt='Homer Simpson' />
      {/* inserindo imagens a partir da pasta src */}
    </>
  );
};

export default App;
