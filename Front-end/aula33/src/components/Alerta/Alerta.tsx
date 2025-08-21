const Alerta = () => {
  const caixa = {
    backgroundColor: "red",
    color: "white",
    padding: "15px",
  };
  const estilo = {
    fontSize: "30px",
    fontWeight: "bold",
  };
  const corPreta = {
    color: "black",
  };
  return (
    <>
      <div style={caixa}>
        <h1 style={estilo}>Alerta de Segurança</h1>
        <p style={corPreta}>Este é um alerta importante para todos os usuários.</p>
      </div>
    </>
  );
};

export default Alerta;
