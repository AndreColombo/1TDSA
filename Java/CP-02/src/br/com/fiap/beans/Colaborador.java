package br.com.fiap.beans;

public class Colaborador {
    private String nome;
    private String setor;
    private String cargo;
    private int quantidadeHora;
    private double valorHora;

    public Colaborador() {
    }

    public Colaborador(String nome, String setor, String cargo, int quantidadeHora, double valorHora) {
        this.nome = nome;
        this.setor = setor;
        this.cargo = cargo;
        this.quantidadeHora = quantidadeHora;
        this.valorHora = valorHora;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSetor() {
        return setor;
    }
    public void setSetor(String setor) {
        this.setor = setor;
    }

    public String getCargo() {
        return cargo;
    }
    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public int getQuantidadeHora() {
        return quantidadeHora;
    }
    public void setQuantidadeHora(int quantidadeHora) {
        this.quantidadeHora = quantidadeHora;
    }

    public double getValorHora() {
        return valorHora;
    }
    public void setValorHora(double valorHora) {
        this.valorHora = valorHora;
    }

    @Override
    public String toString() {
        return "\nCOLABORADOR" +
                "\nnome: " + nome +
                "\nsetor: " + setor +
                "\ncargo: " + cargo +
                "\nquantidadeHora: " + quantidadeHora +
                "\nvalorHora: " + valorHora;
    }
}
