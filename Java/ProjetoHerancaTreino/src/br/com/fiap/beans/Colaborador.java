package br.com.fiap.beans;

public class Colaborador extends Pessoa {
    public int numeroCracha;

    //  metodo construtor vazio
    public Colaborador() {
    }

    //  metodo construtor com herança
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
        return "\n\n" + identificador() +
                "\nnúmero do cracha = " + numeroCracha +
                "\n" + super.toString();
    }

    @Override
    public String identificador() {
        return "INFORMAÇÕES DO COLABORADOR";
    }
}
