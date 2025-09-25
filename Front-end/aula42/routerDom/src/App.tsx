import { BrowserRouter, Route, Routes } from "react-router-dom";
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";

import Home from "./pages/Home/Home";
import Contato from "./pages/Contato/Contato";
import Sobre from "./pages/Sobre/Sobre";

function App() {
  return (
    <BrowserRouter>
      <div className='flex flex-col min-h-screen h-screen w-screen'>
        <Header />

        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/sobre' element={<Sobre />} />
          <Route path='/contato' element={<Contato />} />
        </Routes>

        <Footer />
      </div>
    </BrowserRouter>
  );
}

export default App;
