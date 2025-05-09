package br.com.fiap.beans;

public class Colaborador extends Pessoa {
    private int numeroCracha;

    // metodo construtor com parâmetro vazio
    public Colaborador() {
    }

    // metodo construtor com parâmetro para inputs
    public Colaborador(String nome, String cpf, String rg, int idade, double renda, int numeroCracha) {
        super(nome, cpf, rg, idade, renda);
        this.numeroCracha = numeroCracha;
    }

    public int getCracha() {
        return numeroCracha;
    }
    public void setCracha(int numeroCracha) {
        this.numeroCracha = numeroCracha;
    }

    @Override
    public String toString() {
        return "\n\nCOLABORADOR" +
                "\nnumeroCracha = '" + numeroCracha + '\'' +
                super.toString();
    }
}
