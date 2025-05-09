package br.com.fiap.beans;

public abstract class Pessoa {
    private String nome;
    private String cpf;
    private String rg;
    private int idade;
    private double renda;

    public Pessoa() {
    }

    public Pessoa(String nome, String cpf, String rg, int idade, double renda) {
        this.nome = nome;
        this.cpf = cpf;
        this.rg = rg;
        this.idade = idade;
        this.renda = renda;
    }

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

    public String getRg() {
        return rg;
    }
    public void setRg(String rg) {
        this.rg = rg;
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

    @Override
    public String toString() {
        return "\nnome = '" + nome + '\'' +
                "\ncpf = '" + cpf + '\'' +
                "\nrg = '" + rg + '\'' +
                "\nidade = " + idade +
                "\nrenda = " + renda;
    }
}
