package br.com.fiap.beans;

public class Produto {
    private int codigo;
    private String tipo;
    private String marca;
    private String descricao;
    private double valor;

    public Produto() {
    }

    public Produto(int codigo, String tipo, String marca, String descricao, double valor) {
        this.codigo = codigo;
        this.tipo = tipo;
        this.marca = marca;
        this.descricao = descricao;
        this.valor = valor;
    }

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

    public String getDescricao() {
        return descricao;
    }
    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public double getValor() {
        return valor;
    }
    public void setValor(double valor) {
        this.valor = valor;
    }

    @Override
    public String toString() {
        return "Produto" +
                "\ncodigo=" + codigo +
                "\ntipo='" + tipo + '\'' +
                "\nmarca='" + marca + '\'' +
                "\ndescricao='" + descricao + '\'' +
                "\nvalor=" + valor;
    }
}
