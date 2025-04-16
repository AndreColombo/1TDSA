package br.com.fiap.beans;

public class Produto {
    private int codigo;
    private String tipo;
    private String marca;
    private int quantidade;
    private double valor;

    public int getCodigo() {
        return codigo;
    }
    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getTipo() {
        return tipo;
    }
    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getMarca() {
        return marca;
    }
    public void setMarca(String marca) {
        this.marca = marca;
    }

    public int getQuantidade() {
        return quantidade;
    }
    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    public double getValor() {
        return valor;
    }
    public void setValor(double valor) {
        this.valor = valor;
    }

    @Override
    public String toString() {
        return "PRODUTO" +
                "\ncodigo: " + codigo +
                "\ntipo: '" + tipo + '\'' +
                "\nmarca: '" + marca + '\'' +
                "\nquantidade: " + quantidade +
                "\nvalor: " + valor +
                "\n\nTotal: " + calcularTotal();
    }

    public double calcularTotal() {
        return quantidade * valor;
    }
}
