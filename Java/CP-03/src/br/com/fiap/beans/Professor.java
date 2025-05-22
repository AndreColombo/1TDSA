package br.com.fiap.beans;

public class Professor extends Pessoa {
    private int quantidadeTurmas;

    public Professor() {
    }

    public Professor(String nome, int idade, String cpf, String rg, int quantidadeTurmas) {
        super(nome, idade, cpf, rg);
        this.quantidadeTurmas = quantidadeTurmas;
    }

    public int getQuantidadeTurmas() {
        return quantidadeTurmas;
    }
    public void setQuantidadeTurmas(int quantidadeTurmas) {
        this.quantidadeTurmas = quantidadeTurmas;
    }

    @Override
    public String toString() {
        return "\n\nPROFESSOR" +
                "\nquantidadeTurmas = " + quantidadeTurmas +
                "\n" + super.toString();
    }
}
