import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import Footer from "./components/Footer/Footer";
import Home from "./pages/Home/Home";
import Receita from "./pages/Receita/Receita";
import Categoria from "./pages/Categoria/Categoria";
import NotFound from "./pages/NotFound/NotFound";
import Cadastro from "./pages/Cadastro/Cadastro";
import Login from "./pages/Login/Login";

export default function App() {
  return (
    <>
      <BrowserRouter>
        <div className='flex flex-col h-screen'>
          <main className='grow bg-[#F3F4F6]'>
            <Routes>
              <Route path='/' element={<Home />} />
              <Route path='/cadastro' element={<Cadastro />} />
              <Route path='/login' element={<Login />} />
              <Route path='/categoria/:categoria' element={<Categoria />} />
              <Route path='/receita/:link' element={<Receita />} />
              <Route path='*' element={<NotFound />} />
            </Routes>
          </main>
          <Footer />
        </div>
      </BrowserRouter>
    </>
  );
}
