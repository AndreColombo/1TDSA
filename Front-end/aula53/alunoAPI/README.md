# 📚 API REST - AlunoWEB 🎓

Este projeto foi desenvolvido no contexto da disciplina _Front-End Design Engineering_, pertencente ao curso de Tecnologia em Análise e Desenvolvimento de Sistemas da **FIAP** (Faculdade de Informática e Administração Paulista). O principal objetivo foi aplicar conceitos práticos de desenvolvimento front-end em conjunto com integrações de back-end e banco de dados.

Cabe destacar que os módulos referentes à API (desenvolvida em Java) e ao banco de dados (Oracle) ainda podem ser otimizados. Essas áreas, apesar de funcionais, não constituem meu principal campo de especialização, razão pela qual algumas implementações podem carecer de refinamento técnico.

Aqui está uma visão geral das funcionalidades da API.

---

&nbsp;

## 🧩 Tecnologias Utilizadas

🌐 **FRONTEND**

- **VITE** — Ferramenta moderna de build e bundling para aplicações web, focada em desempenho e simplicidade no desenvolvimento com React ou TypeScript..
    - TypeScript — Fornece tipagem estática ao JavaScript, aumentando a segurança e a manutenibilidade do códig.
        - React Hooks (useState, useEffect, useParams) — Controle de estado, efeitos colaterais e parâmetros de rota nos componentes..
        - Fetch API / Axios — Comunicação assíncrona com o backend Quarkus.
        - Vite Image Plugins / Lazy Loading — Otimização e carregamento dinâmico de imagens, garantindo melhor performance e SEO.
        - Hot Module Replacement (HMR) — Atualização instantânea dos módulos durante o desenvolvimento, sem recarregar toda a aplicação.

⚙️ **BACKEND**

- **QUARKUS**  — Framework Java nativo para a nuvem, otimizado para Kubernetes e containers, ideal para microserviços RESTful.
    - Jakarta REST (JAX-RS) — Implementação de endpoints RESTful com anotações simples e integração com JSON-B/Jackson.
    - DAO Pattern (Data Access Object) — Camada responsável por abstrair a persistência e isolar a lógica de acesso a dados.
    - Hibernate ORM com Panache — Simplifica o uso do JPA para comunicação com o banco de dados (ex: PostgreSQL ou Oracle).
    - Quarkus Dev Mode — Permite hot reload durante o desenvolvimento, acelerando o ciclo de testes e ajustes.

🛢️ **BANCO DE DADOS**

- **Oracle Database** — Armazenamento relacional das entidades (banda, álbum, menu).
    - SQL — Consultas customizadas com JOIN, ORDER BY, DBMS_RANDOM, etc.

🛠️ **Ferramentas de Desenvolvimento**

- **Eclipse IDE ou IntelliJ** — Ambiente de desenvolvimento Java.
- **Postman ou Insomnia** — Testes de endpoints da API.
- **Git/GitHub** — Controle de versão e hospedagem do projeto.

---

&nbsp;

### 🛢️Banco de Dados ![Database](https://img.shields.io/badge/Database-Oracle-blue?logo=oracle)

📁 **Tabelas**

- `aluno`: Informações dos aluno

O SQL da estrutura do banco de dados deve ser exatamene a que está abaixo, respeitando o mesmo nome de entidade e atributos.


## 🧩 Estrutura da Tabela: `T_FIAP_ALUNO`

| Campo   | Tipo                | Descrição                        |
|---------|---------------------|----------------------------------|
| `id`    | NUMBER(9,2)         | Identificador único do aluno     |
| `nome`  | VARCHAR2(50 BYTE)   | Nome do aluno                    |
| `rm`    | NUMBER(9,2)         | Registro de Matrícula do aluno   |
| `turma` | VARCHAR2(20 BYTE)   | Turma do aluno                   |
| `nota`  | NUMBER(9,2)         | Nota do aluno                    |

---

## 🚀 Acesso aos endpoints ![REST API](https://img.shields.io/badge/API-RESTful-green?style=flat&logo=api)
| Método     | Caminho       | Descrição                                                                | Saída                                                                    |
| ---------- | ------------- | ------------------------------------------------------------------------ |--------------------------------------------------------------------------|
| **GET**    | `/aluno`      | Lista **todos os alunos** cadastrados no sistema.                        | `[{ "rm": 12345, "nome": "João Silva", "turma": "1TDS", "NOTA" : 8,2 }]` |
| **POST**   | `/aluno`      | Cadastra um **novo aluno**. Recebe um objeto JSON com os dados do aluno. | **HTTP/1.1 201 Created**                                                 |
| **PUT**    | `/aluno/{rm}` | Atualiza os dados de um aluno existente, identificado pelo `rm`.         | **HTTP/1.1 200 OK**                                                      |
| **DELETE** | `/aluno/{rm}` | Exclui (remove) um aluno do sistema pelo número de registro `rm`.        | **HTTP/1.1 200 OK**                                                      |

---
*Observação:* Para saber o significado dos códigos HTTP/1.1, visualiza a tabela explicativa no final desta documentação.
&nbsp;
---

### 🔁 HTTP - STATUS

---

| Código | Status HTTP                      | Descrição                                                           |
|--------|----------------------------------|---------------------------------------------------------------------|
| 200    | OK                               | A requisição foi bem-sucedida e o servidor retornou a resposta.     |
| 201    | Created                          | A requisição foi bem-sucedida e um novo recurso foi criado.         |
| 202    | Accepted                         | A requisição foi aceita, mas ainda não foi processada.              |
| 204    | No Content                       | A requisição foi bem-sucedida, mas não há conteúdo a ser retornado. |
| 301    | Moved Permanently                | O recurso foi movido permanentemente para outra URL.                |
| 302    | Found                            | O recurso foi temporariamente movido para outra URL.                |
| 400    | Bad Request                      | A requisição não pode ser processada devido a erros de sintaxe.     |
| 401    | Unauthorized                     | A requisição requer autenticação do usuário.                        |
| 403    | Forbidden                        | O servidor entendeu a requisição, mas se recusa a autorizá-la.      |
| 404    | Not Found                        | O recurso solicitado não foi encontrado no servidor.                |
| 405    | Method Not Allowed               | O método HTTP usado não é permitido para o recurso solicitado.      |
| 500    | Internal Server Error            | Ocorreu um erro inesperado no servidor.                             |
| 502    | Bad Gateway                      | O servidor agiu como um gateway e recebeu uma resposta inválida.    |
| 503    | Service Unavailable              | O servidor está temporariamente indisponível.                       |
| 504    | Gateway Timeout                  | O servidor não recebeu uma resposta a tempo de outro servidor.      |

---

## 🧑‍💻 Desenvolvedor

    Prof. Adriano Milanez
    profadriano.milanez@fiap.com.br
    Disciplina: Front-End Design Engineering
    Tecnologia em Análise e Desenvolvimento de Sistemas
    Faculdade de Informática e Administração Paulista - FIAP
