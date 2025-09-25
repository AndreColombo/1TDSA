import { useEffect, useState } from "react";

const UseEffect_Exemplo04 = () => {

    const [largura, setLargura] = useState(window.innerWidth);

    useEffect(() => {
        const atualizarLargura = () => setLargura(window.innerWidth);
        window.addEventListener('resize', atualizarLargura);
        return () =>{
            window.removeEventListener('resize', atualizarLargura);
        }
    }, []);
    return(
        <>
            <h1>Exemplo 04: Detectar e exibir a largura da tela</h1>
            <p>Largura da janela { largura }px</p>
        </>
    )
}
export default UseEffect_Exemplo04;