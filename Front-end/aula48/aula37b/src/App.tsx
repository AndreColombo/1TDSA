import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./pages/Home/Home";
import Filme from "./pages/Filme/Filme";

const App = () => {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/filme/:link' element={<Filme />} />
        </Routes>
      </BrowserRouter>
    </>
  );
};
export default App;
