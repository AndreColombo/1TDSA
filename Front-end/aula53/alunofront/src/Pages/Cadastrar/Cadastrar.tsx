import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

type Aluno = {
  id?: number;
  rm: number;
  nome: string;
  turma: string;
  nota: number;
};

const Cadastrar = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const alunoEdicao = location.state as Aluno | undefined;
  const [aluno, setAluno] = useState<Aluno>({
    id: alunoEdicao?.id ?? undefined,
    rm: alunoEdicao?.rm ?? 0,
    nome: alunoEdicao?.nome ?? "",
    turma: alunoEdicao?.turma ?? "",
    nota: alunoEdicao?.nota ?? 0,
  });

  useEffect(() => {
    if (alunoEdicao) {
      setAluno(alunoEdicao);
    }
  }, [alunoEdicao]);

  const API_URL = "http://localhost:8080/aluno";

  const url = aluno.id ? `${API_URL}/${aluno.id}` : API_URL;

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { id, value } = e.target;
    setAluno({
      ...aluno,
      [id]: id === "rm" || id === "nota" ? Number(value) : value,
    });
  };

  const handlePost = async () => {
    const method = aluno.id ? "PUT" : "POST";
    try {
      const response = await fetch(url, {
        method: method,
        headers: { "Content-type": "application/json" },
        body: JSON.stringify(aluno),
      });
      if (response.ok) {
        alert(aluno.id ? `Aluno ${aluno.nome} atualizado com sucesso!` : `Aluno ${aluno.nome} cadastrado com sucesso!`);
        navigate("/");
      } else {
        const erro = await response.text();
        alert(aluno.id ? "Erro ao atualizar aluno: " + erro : "Erro ao cadastrar aluno: " + erro);
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
            <input type='text' id='nome' onChange={handleChange} value={aluno.nome} />
          </div>
          <div>
            <label>RM: </label>
            <input type='number' id='rm' onChange={handleChange} value={aluno.rm} />
          </div>
          <div>
            <label>Turma: </label>
            <input type='text' id='turma' onChange={handleChange} value={aluno.turma} />
          </div>
          <div>
            <label>Nota: </label>
            <input type='number' id='nota' step='0.1' min={0} max={10} onChange={handleChange} value={aluno.nota} />
          </div>
          <div>
            <button onClick={handlePost}>{aluno.id ? "Atualizar" : "Cadastrar"}</button>
          </div>
        </form>
      </div>
    </>
  );
};

export default Cadastrar;
