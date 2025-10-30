import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./Pages/Home/Home";
import Cadastrar from "./Pages/Cadastrar/Cadastrar";

const App = () => {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />
          <Route path='/cadastrar' element={<Cadastrar />} />
          <Route path='/atualizar' element={<Cadastrar />} />
        </Routes>
      </BrowserRouter>
    </>
  );
};
export default App;
