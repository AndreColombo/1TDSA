import type { FilmeTipos } from "../Types/FilmeTipos";

export async function BuscarTodosFilmes(): Promise<FilmeTipos[]> {
  const response = await fetch("/dados/filmes.json");
  if (!response.ok) {
    throw new Error("Erro ao buscar filmes");
  }
  return await response.json();
}
