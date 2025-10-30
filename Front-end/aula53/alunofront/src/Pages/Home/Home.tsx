import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";

type Aluno = {
  id: number;
  rm: number;
  nome: string;
  turma: string;
  nota: number;
};

const Home = () => {
  const [aluno, setAluno] = useState<Aluno[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const API_URL = "http://localhost:8080/aluno";

  useEffect(() => {
    listarAlunos();
  }, []);
  const listarAlunos = async () => {
    setLoading(true);
    setError("");

    try {
      const response = await fetch(API_URL);
      if (!response.ok) throw new Error("Erro ao buscar Alunos!");
      const data = await response.json();
      setAluno(data);
    } catch (err) {
      setError(`Falha ao carregar a lista de Aluno: ${err}`);
    } finally {
      setLoading(false);
    }
  };

  const editarAluno = (aluno: Aluno) => {
    navigate(`atualizar/${aluno.id}`);
  };

  const deletarAluno = async (aluno: Aluno) => {
    if (window.confirm(`Confirma a exclusão do aluno ${aluno.nome}?`)) {
      try {
        const response = await fetch(`${API_URL}/${aluno.id}`, {
          method: "DELETE",
        });
        if (response.ok) {
          alert(`Aluno ${aluno.nome} excluído com sucesso!`);
          listarAlunos();
        } else {
          const erro = await response.text();
          alert("Erro ao excluir aluno: " + erro);
        }
      } catch (error) {
        console.error(error);
        alert("Erro de conexão com o servidor!");
      }
    }
  };

  return (
    <>
      <h1>Home</h1>
      <Link to='/cadastrar'>Cadastrar alunos</Link>
      <div>
        {loading && <p>Carregando alunos...</p>}
        {error && <p>{error}</p>}
        {!loading && aluno.length === 0 && !error && <p>Nenhum aluno cadastrado</p>}
      </div>

      {!loading && aluno.length > 0 && (
        <div>
          <table>
            <thead>
              <tr>
                <th>RM</th>
                <th>Nome</th>
                <th>Turma</th>
                <th>Nota</th>
                <th colSpan={2}>Ação</th>
              </tr>
            </thead>
            <tbody>
              {aluno.map((aluno) => (
                <tr key={aluno.id}>
                  <td>{aluno.id}</td>
                  <td>{aluno.rm}</td>
                  <td>{aluno.nome}</td>
                  <td>{aluno.turma}</td>
                  <td>{aluno.nota.toFixed(2)}</td>
                  <td>
                    <button onClick={() => editarAluno(aluno)}>Editar</button>
                  </td>
                  <td>
                    <button onClick={() => deletarAluno(aluno)}>Excluir</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </>
  );
};

export default Home;
