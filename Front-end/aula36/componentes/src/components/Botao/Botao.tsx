function Botao({ texto }: { texto: string }) {
  const estilo = {
    backgroundColor: "#4f46e5",
    color: "#fff",
    padding: "0.5rem 1rem",
    border: "none",
    cursor: "pointer",
  };
  return (
    <>
      <button style={estilo}>{texto}</button>
    </>
  );
}

export default Botao;
