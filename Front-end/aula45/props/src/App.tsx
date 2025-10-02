import Botao from "./components/Botao/Botao";
import Formulario01 from "./components/Formulario/Formulario";
import Formulario02 from "./components/Formulario02/Formulario02";
import Tarefas from "./components/Tarefas/Tarefas";

function App() {
  return (
    <>
      <h1>Exemplo 01</h1>
      <Botao />

      <h1>Exemplo 02</h1>
      <Botao cor='red' texto='Avançar' onClick={() => alert("Botão Clicado!")} />

      <h1>Exemplo 03</h1>
      <Botao cor='green' onClick={() => alert("Botão 03 Clicado!")} />

      <Tarefas />

      <Formulario01 />
      <Formulario02 />
    </>
  );
}

export default App;
