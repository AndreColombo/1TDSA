"""
Flask - micro-framework web para Python
 - APIs simples
 - Facilita o processo de transformar uma função Python em rotas webm
 acessíveis via HTTP

 - Requisitos
    - Instalar a biblioteca Flask - pip install Flask
"""

# Exemplo 1 - Hello World API
from flask import Flask

# criar uma instância do aplicativo Flask
app_api = Flask(__name__)


@app_api.route("/")
def hello_world():
    return "Hello, World da API Flask!"


@app_api.route("/hello/<nome>")
def hello_name(nome):
    return f"Hello, {nome}"


@app_api.route("/soma/<int:n1>/<int:n2>")
def soma(n1, n2):
    # lódiga da função
    # manipulação de dados...
    return f"A soma de {n1} com {n2} é {n1 + n2}"


# main
if __name__ == "__main__":
    app_api.run(debug=True)
