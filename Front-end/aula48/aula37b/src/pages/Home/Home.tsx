import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import type { FilmeTipos } from "../../types/FilmeTipos";

const Home = () => {
  const [filmes, setFilmes] = useState<FilmeTipos[]>([]);
  useEffect(() => {
    const buscarFilmes = async () => {
      try {
        const response = await fetch("/dados/filmes.json");
        const data = await response.json();
        setFilmes(data);
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
            <Link to={`filme/${filme.link}`}>{filme.titulo}</Link>
          </li>
        ))}
      </ul>
    </>
  );
};

export default Home;
