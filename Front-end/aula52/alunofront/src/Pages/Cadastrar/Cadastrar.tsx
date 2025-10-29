import { useState } from "react";
import { useNavigate } from "react-router-dom";

type Aluno = {
  id: number;
  rm: number;
  nome: string;
  turma: string;
  nota: number;
};

const Cadastrar = () => {
  const navigate = useNavigate();
  const [aluno, setAluno] = useState<Aluno>({
    id: 0,
    rm: 0,
    nome: "",
    turma: "",
    nota: 0,
  });

  const API_URL = "http://localhost:8080/aluno";

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { id, value } = e.target;
    setAluno({
      ...aluno,
      [id]: id === "rm" || id === "nota" ? Number(value) : value,
    });
  };

  const handlePost = async () => {
    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-type": "application/json" },
        body: JSON.stringify(aluno),
      });
      if (response.ok) {
        alert(`Aluno ${aluno.nome} cadastrado com sucesso!`);
        navigate("/");
      } else {
        const erro = await response.text();
        alert("Erro ao cadastrar aluno: " + erro);
      }
    } catch (error) {
      console.error(error);
      alert("Erro de conexão com o servidor!");
    }
  };

  return (
    <>
      <h1>Cadastrar</h1>
      <div>
        <form id='formaluno'>
          <div>
            <label>Nome: </label>
            <input type='text' id='nome' onChange={handleChange} />
          </div>
          <div>
            <label>RM: </label>
            <input type='number' id='rm' onChange={handleChange} />
          </div>
          <div>
            <label>Turma: </label>
            <input type='text' id='turma' onChange={handleChange} />
          </div>
          <div>
            <label>Nota: </label>
            <input type='number' id='nota' step='0.1' min={0} max={10} onChange={handleChange} />
          </div>
          <div>
            <button onClick={handlePost}>Cadastrar / Atualizar</button>
          </div>
        </form>
      </div>
    </>
  );
};

export default Cadastrar;
