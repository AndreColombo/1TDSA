import { Link } from "react-router-dom";

const PaginaErro = () => {
  return (
    <div>
      <h1>Ops! Algo deu errado.</h1>
      <p>Por favor, tente novamente mais tarde.</p>
      <Link to='/'>Voltar para a página inicial</Link>
    </div>
  );
};

export default PaginaErro;
