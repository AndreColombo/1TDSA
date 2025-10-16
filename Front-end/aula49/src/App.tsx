import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./pages/Home/Home";
import Filme from "./pages/Filme/Filme";
import PaginaErro from "./components/PaginaErro/PaginaErro";

const App = () => {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/filme/:link' element={<Filme />} />
          <Route path='*' element={<PaginaErro />} />
        </Routes>
      </BrowserRouter>
    </>
  );
};
export default App;
