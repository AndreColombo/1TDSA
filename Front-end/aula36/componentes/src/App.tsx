import Botao from "./components/Botao/Botao";
import Mensagem from "./components/Mensagem/Mensagem";

function App() {
  return (
    <>
      <Mensagem></Mensagem>
      <Mensagem />
      <Botao texto='Cancelar' />
      <Botao texto='Atualizar' />
      <Botao texto='Excluir' />
      <Botao texto='Gravar' />
    </>
  );
}

export default App;
