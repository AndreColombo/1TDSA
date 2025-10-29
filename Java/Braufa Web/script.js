const API_URL = "http://localhost:8080/aluno";

//  GET
async function getAlunos() {
  const resp = await fetch(API_URL);
  return await resp.json();
}

async function exibirAlunos() {
  const alunos = await getAlunos();
  const container = document.querySelector("#lista-de-alunos");
  container.innerHTML = "";

  alunos.forEach((aluno) => {
    const card = document.createElement("article");
    card.innerHTML = `
      <header>RM: ${aluno.rm}</header>
      <p>Nome: ${aluno.nome}</p>
      <p>Turma: ${aluno.turma}</p>
      <p>Nota: ${aluno.nota}</p>
      <footer>        
        <button onclick="deletarAluno(${aluno.rm})">Excluir</button>
        
      </footer>
    `;
    container.appendChild(card);
  });
}

//  POST
async function inserirAluno() {
  const aluno = capturarFormulario();
  const resp = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(aluno),
  });
  if (resp.ok) alert("Aluno cadastrado com sucesso!");
}

//  PUT
async function atualizarAluno() {
  const aluno = capturarFormulario();
  const resp = await fetch(API_URL, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(aluno),
  });
  if (resp.ok) alert("Aluno atualizado com sucesso!");
}

//  DELETE
async function deletarAluno(rm) {
  if (!confirm(`Deseja excluir o aluno RM ${rm}?`)) return;

  const resp = await fetch(`${API_URL}/${rm}`, {
    method: "DELETE",
  });

  if (resp.ok) {
    alert("Aluno excluído com sucesso!");
    exibirAlunos();
  } else {
    alert("Erro ao excluir.");
  }
}

//  Helpers
function capturarFormulario() {
  return {
    rm: parseInt(document.getElementById("rm").value),
    nome: document.getElementById("nome").value,
    turma: document.getElementById("turma").value,
    nota: parseFloat(document.getElementById("nota").value),
  };
}

function carregarFormulario(rm, nome, turma, nota) {
  window.location.href = `cadastro.html?rm=${rm}&nome=${encodeURIComponent(nome)}&turma=${encodeURIComponent(turma)}&nota=${nota}`;
}

//  Carregar dados no form se veio da lista
document.addEventListener("DOMContentLoaded", () => {
  if (document.getElementById("lista-de-alunos")) {
    exibirAlunos();
  }

  const btnPost = document.getElementById("btnPost");
  const btnPut = document.getElementById("btnPut");

  if (btnPost) btnPost.addEventListener("click", inserirAluno);
  if (btnPut) btnPut.addEventListener("click", atualizarAluno);

  // Se vier da lista para edição
  const params = new URLSearchParams(window.location.search);
  if (params.has("rm")) {
    document.getElementById("rm").value = params.get("rm");
    document.getElementById("nome").value = params.get("nome");
    document.getElementById("turma").value = params.get("turma");
    document.getElementById("nota").value = params.get("nota");
  }
});
