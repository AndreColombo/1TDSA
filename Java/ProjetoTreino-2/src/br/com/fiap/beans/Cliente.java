package br.com.fiap.beans;

public class Cliente {
    private String cpf;
    private String nome;
    private int idade;
    private String profissao;
    private double renda;
    private Endereco endereco;

    // metodo construtor com parâmetros vazio
    public Cliente() {
    }

    // metodo construtor com parâmetros para input
    public Cliente(String cpf, String nome, int idade, String profissao, double renda) {
        this.cpf = cpf;
        this.nome = nome;
        this.idade = idade;
        this.profissao = profissao;
        this.renda = renda;
    }

    public String getCpf() {
        return cpf;
    }
    public void setCpf(String cpf) {
        this.cpf = cpf;
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

    public String getProfissao() {
        return profissao;
    }
    public void setProfissao(String profissao) {
        this.profissao = profissao;
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
        return "CLIENTE" +
                "\ncpf: " + cpf +
                "\nnome: " + nome +
                "\nidade: " + idade +
                "\nprofissao: " + profissao +
                "\nrenda: " + renda +
                "\nENDEREÇO: " + endereco;
    }
}
