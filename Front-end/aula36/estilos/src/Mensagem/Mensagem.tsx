import estilos from "./Mensagem.module.css";
function Mensagem() {
  return (
    <>
      <p className={estilos.paragrafo}>Olá, este é um componente com CSS Module!!</p>
      <p className='paragrafo'>Olá, este é um componente com CSS Module!!</p>
    </>
  );
}

export default Mensagem;
