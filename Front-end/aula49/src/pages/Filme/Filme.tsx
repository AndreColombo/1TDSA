import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import type { FilmeTipos } from "../../Types/FilmeTipos";
import { BuscarTodosFilmes } from "../../Services/Services";

const Filme = () => {
  const { link } = useParams();

  const [filme, setFilme] = useState<FilmeTipos | null>(null);

  useEffect(() => {
    BuscarTodosFilmes()
      .then((data) => {
        const encontrado = data.find((p) => p.link === link);
        setFilme(encontrado || null);
      })
      .catch(() => setFilme(null));
  }, [link]);

  if (!filme) {
    return (
      <>
        <h1>Filme não encontrado!</h1>
      </>
    );
  }
  return (
    <>
      <h1>Filme</h1>
      <b>{filme.titulo}</b>
      <br />
      <img src={`/imagens/${filme.imagem}`} width={"10%"} />
      <br />
      <strong>Estreia: </strong>
      {filme.estreia}
      <br />
      <b>Descrição: </b>
      {filme.descricao}
      <br />
    </>
  );
};
export default Filme;
