package br.com.fiap.beans;

public class Carro {
    private String marca;
    private String modelo;
    private String descricao;
    private int ano;
    private double valor;

    public Carro() {
    }

    public Carro(String marca, String modelo, String descricao, int ano, double valor) {
        this.marca = marca;
        this.modelo = modelo;
        this.descricao = descricao;
        this.ano = ano;
        this.valor = valor;
    }

    public String getMarca() {
        return marca;
    }
    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return modelo;
    }
    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getDescricao() {
        return descricao;
    }
    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public int getAno() {
        return ano;
    }
    public void setAno(int ano) {
        this.ano = ano;
    }

    public double getValor() {
        return valor;
    }
    public void setValor(double valor) {
        this.valor = valor;
    }
}
