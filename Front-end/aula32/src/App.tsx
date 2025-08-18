/*
  export default function App(){
  função nomeada COM exportação direta
 */

import Comp from "./Comp";

const App = () => {
  return (
    <>
      <h1>Primeiro componente</h1>
      <Comp></Comp>
      <Comp></Comp>
      <Comp></Comp>
      <Comp></Comp>
    </>
  );
};

export default App;
/*
  função nomeada SEM exportação direta
 */
