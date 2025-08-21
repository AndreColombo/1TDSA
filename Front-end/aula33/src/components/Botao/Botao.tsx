const Botao = ({ texto }: { texto: string }) => {
  const estilo = {
    backgroundColor: "blue",
    color: "white",
    padding: "10px 20px",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    fontSize: "16px",
  };
  return (
    <>
      <button style={estilo}>{texto}</button>
    </>
  );
};

export default Botao;
