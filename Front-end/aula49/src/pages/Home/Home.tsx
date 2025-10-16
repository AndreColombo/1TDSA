import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import type { FilmeTipos } from "../../Types/FilmeTipos";
import { BuscarTodosFilmes } from "../../Services/Services";

const Home = () => {
  const [filmes, setFilmes] = useState<FilmeTipos[]>([]);

  useEffect(() => {
    const buscarFilmes = async () => {
      try {
        BuscarTodosFilmes()
          .then((data) => setFilmes(data))
          .catch((error) => console.error("Erro na promessa: ", error));
      } catch (error) {
        console.error("Erro ao buscar filmes: ", error);
      }
    };
    buscarFilmes();
  }, []);

  return (
    <>
      <h1>Home Page</h1>
      <ul>
        {filmes.map((filme) => (
          <li key={filme.id}>
            <Link to={`/filme/${filme.link}`}>{filme.titulo}</Link>
          </li>
        ))}
      </ul>
    </>
  );
};
export default Home;
