// DOM - Document Object Model

let elemento = document.getElementById("msg");
let elemento2 = document.getElementById("novoElemento");

function mensagem() {
  //set de instruções;
  elemento.innerText = "<p>HELLO WORLD!</p>";
  // INNER TEXT - insere no conteúdo do navegador SOMENTE texto, se houverem tags html na string a ser inserida, estas tags serão ignoradas e exibidas como texto

  elemento2.innerHTML = '<p class="cor">INSERINDO NOVO CONTEÚDO COM ELEMENTOS HTML</p>';
  alert("Olá mundo!");

  a = 1.0;
  b = "1";
  if (a === b) {
    document.write("São iguais!");
  } else {
    document.write("São diferentes!");
  }
}
let x = document.getElementById("msg2");
function ola() {
  x.innerText = "Mensagem criada utilizando o evento onmouseover.";
}

function apagar() {
  x.innerText = "";
}

function validar() {
  nome = document.getElementById("nome");
  cpf = document.getElementById("cpf");

  /*  corpo = document.getElementById("corpo");
    corpo.style.backgroundColor = "#ccc" */

  if (nome.value == "") {
    document.getElementById("erroNome").innerText = "Campo nome é de prenchimento obrigatório!";
    //nome.style.borderColor = "#f00";
    nome.focus();
    return false;
  } else {
    document.getElementById("erroNome").innerText = "";
  }

  if (cpf.value == "") {
    document.getElementById("erroCPF").innerText = "Campo CPF é de prenchimento obrigatório!";
    cpf.focus();
    return false;
  } else {
    document.getElementById("erroCPF").innerText = "";
  }
}

function cancelar() {
  document.getElementById("nome").value = "";
}
