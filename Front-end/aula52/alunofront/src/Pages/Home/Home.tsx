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
    fetchAlunos();
  }, []);
  const fetchAlunos = async () => {
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

  return (
    <>
      <h1>Home</h1>
      <Link to='/cadastrar'>Cadastrar alunos</Link>
      <div>
        {loading && <p>Carregando alunos...</p>}
        {error && <p>{error}</p>}
        {!loading && aluno.length === 0 && !error && <p>Nenhum aluno cadastrado</p>}
      </div>
    </>
  );
};

export default Home;
