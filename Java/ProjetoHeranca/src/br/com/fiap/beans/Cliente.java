package br.com.fiap.beans;

public class Cliente extends Pessoa {
    private String status;
    private Endereco endereco;

    // metodo construtor com parâmetro vazio
    public Cliente() {
    }

    // metodo construtor com parâmetro para inputs
    public Cliente(String nome, String cpf, String rg, int idade, double renda, String status) {
        super(nome, cpf, rg, idade, renda);
        this.status = status;
    }

    public String getStatus() {
        return status;
    }
    public void setStatus(String status) {
        this.status = status;
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
                "\nstatus = '" + status + '\'' +
                super.toString() +
                endereco;
    }
}
