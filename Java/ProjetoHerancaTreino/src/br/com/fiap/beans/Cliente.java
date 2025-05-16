package br.com.fiap.beans;

public class Cliente extends Pessoa {
    private String status;

    //  metodo construtor vazio
    public Cliente() {
    }

    //  metodo construtor com herança
    public Cliente(String nome, int idade, String cpf, String rg, double renda, String status) {
        super(nome, idade, cpf, rg, renda);
        this.status = status;
    }

    public String getStatus() {
        return status;
    }
    public void setStatus(String status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "\n\n"+ identificador() +
                "\nstatus = '" + status + '\'' +
                "\n" + super.toString();
    }

    @Override
    public String identificador() {
        return "INFORMAÇÕES DO CLIENTE";
    }
}
