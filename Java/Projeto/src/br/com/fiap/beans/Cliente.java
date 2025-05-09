package br.com.fiap.beans;

public class Cliente {
    private String nomeCliente;
    private String cpf;
    private int idade;
    private double renda;
    private Endereco endereco;

    // metodo contrutor com parâmentro vazio
    public Cliente() {
    }

    // metodo contrutor com parâmentros para inputs
    public Cliente(String nomeCliente, String cpf, int idade, double renda) {
        this.nomeCliente = nomeCliente;
        this.cpf = cpf;
        this.idade = idade;
        this.renda = renda;
    }

    // metodos setters e getters
    public String getNomeCliente() {
        return nomeCliente;
    }
    public void setNomeCliente(String nomeCliente) {
        this.nomeCliente = nomeCliente;
    }

    public String getCpf() {
        return cpf;
    }
    public void setCpf(String cpf) {
        this.cpf = cpf;
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

    public Endereco getEndereco() {
        return endereco;
    }
    public void setEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    @Override
    public String toString() {
        return "CLIENTE" +
                "\nnome do Cliente = '" + nomeCliente + '\'' +
                "\ncpf = '" + cpf + '\'' +
                "\nidade = " + idade +
                "\nrenda = " + renda +
                "\nENDEREÇO" + endereco;
    }
}
