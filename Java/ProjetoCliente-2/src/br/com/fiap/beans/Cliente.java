package br.com.fiap.beans;

public class Cliente {
    // Visibilidade, tipo de dados e atributos
    private String nome;
    private String cpf;
    private String numeroCelular;
    private int idade;
    private double renda;

    // Metodo construtor vazio
    public Cliente() {
    }

    // Metodo construtor cheio
    public Cliente(String nome, String cpf, String numeroCelular, int idade, double renda) {
        this.nome = nome;
        this.cpf = cpf;
        this.numeroCelular = numeroCelular;
        this.idade = idade;
        this.renda = renda;
    }

    // Setters (entrada) e getters (retornar / exibir)
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCpf() {
        return cpf;
    }
    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getNumeroCelular() {
        return numeroCelular;
    }
    public void setNumeroCelular(String numeroCelular) {
        this.numeroCelular = numeroCelular;
    }

    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }

    public double getRenda() {
        return renda;
    }
    public void setRenda(double renda) {
        this.renda = renda;
    }

    // toString

    @Override
    public String toString() {
        return "Cliente" +
                "\nnome='" + nome + '\'' +
                "\ncpf='" + cpf + '\'' +
                "\nnumeroCelular='" + numeroCelular + '\'' +
                "\nidade=" + idade +
                "\nrenda=" + renda;
    }
}
