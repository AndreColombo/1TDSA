package br.com.fiap.beans;

public class Cliente extends Pessoa {
    private String status;

    public Cliente() {
    }

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
        return "\nCliente" +
                "\nstatus = '" + status + '\'' +
                "\n\n" + super.toString();
    }

    @Override
    public String identificador() {
        return "Retorno da classe Cliente";
    }
}
