package br.com.fiap.beans;

public class Colaborador extends Pessoa {
    private int numeroCracha;

    public Colaborador() {
    }

    public Colaborador(String nome, int idade, String cpf, String rg, double renda, int numeroCracha) {
        super(nome, idade, cpf, rg, renda);
        this.numeroCracha = numeroCracha;
    }

    public int getNumeroCracha() {
        return numeroCracha;
    }
    public void setNumeroCracha(int numeroCracha) {
        this.numeroCracha = numeroCracha;
    }

    @Override
    public String toString() {
        return "\n\n\nColaborador" +
                "\nnumeroCracha = " + numeroCracha +
                "\n\n" + super.toString();
    }

    @Override
    public String identificador() {
        return "Retorno da classe Colaborador";
    }
}
