package br.com.fiap.beans;

public abstract class Pessoa {
    private String nome;
    private int idade;
    private String cpf;
    private String rg;
    private double renda;
    private Endereco endereco;

    public Pessoa() {
    }

    public Pessoa(String nome, int idade, String cpf, String rg, double renda) {
        this.nome = nome;
        this.idade = idade;
        this.cpf = cpf;
        this.rg = rg;
        this.renda = renda;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
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

    public double getRenda() {
        return renda;
    }
    public void setRenda(double renda) {
        this.renda = renda;
    }

    public Endereco getEndereco() {
        return endereco;
    }
    public void setEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    @Override
    public String toString() {
        return "Pessoa" +
                "\nnome = '" + nome + '\'' +
                "\nidade = " + idade +
                "\ncpf = '" + cpf + '\'' +
                "\nrg = '" + rg + '\'' +
                "\nrenda = " + renda;
    }

    public abstract String identificador();
}
