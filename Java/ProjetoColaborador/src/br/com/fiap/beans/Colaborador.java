package br.com.fiap.beans;

public class Colaborador {
    // visibilidade, tipo de dados e atributos
    private String nome;
    private String email;
    private String cargo;
    private int idade;
    private double quantidadeHoras;
    private double valorHora;

    // métodos setters (entrada) métodos getters (retornar \ exibir)
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public double getQuantidadeHoras() {
        return quantidadeHoras;
    }

    public void setQuantidadeHoras(double quantidadeHoras) {
        this.quantidadeHoras = quantidadeHoras;
    }

    public double getValorHora() {
        return valorHora;
    }

    public void setValorHora(double valorHora) {
        this.valorHora = valorHora;
    }

    @Override
    public String toString() {
        return "Colaborador" +
                "\nnome: '" + nome + '\'' +
                "\nemail: '" + email + '\'' +
                "\ncargo: '" + cargo + '\'' +
                "\nidade: " + idade +
                "\nquantidade de horas: " + quantidadeHoras +
                "\nvalor da hora: " + valorHora;
    }

    // métodos workers
    // calcularSalario
    public double calcularSalario() {
        return quantidadeHoras * valorHora;
    }

    // informacaoSalario
    public String informacaoSalario() {
        String informacao = null;
        if (calcularSalario() <= 7555) {
            informacao = "Salário abaixo ou igual a 7555";
        } else {
            informacao = "Salário acima de 7555";
        }
        return informacao;
    }
}
