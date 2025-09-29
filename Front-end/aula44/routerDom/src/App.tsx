import { BrowserRouter, Route, Routes } from "react-router-dom";

import Layout from "./components/Layout/Layout";
import Home from "./pages/Home/Home";
import Contato from "./pages/Contato/Contato";
import Sobre from "./pages/Sobre/Sobre";
import ProdutoDetalhes from "./pages/ProdutoDetalhes/ProdutoDetalhes";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Layout />}>
          <Route index path='/' element={<Home />} />
          <Route path='/sobre' element={<Sobre />} />
          <Route path='/contato' element={<Contato />} />
          <Route path='/ProdutoDetalhes/:id' element={<ProdutoDetalhes />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
