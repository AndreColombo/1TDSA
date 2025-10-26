export async function BuscarReceitas() {
  const response = await fetch("/data/receitas.json");
  return await response.json();
}
