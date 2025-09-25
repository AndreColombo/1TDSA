import Card from "../../components/Card/Card";

const Contato = () => {
  return (
    <>
      <section className='flex-grow p-4'>
        <h2 className='text-2xl font-bold mb-4'>Contato</h2>
        <p>Bem-vindo à página de Contato. Aqui você pode encontrar nossas informações de contato e um formulário para nos enviar uma mensagem.</p>
        <Card>
          <h2 className='font-semibold'>Formulário de Contato</h2>
        </Card>
      </section>
    </>
  );
};

export default Contato;
