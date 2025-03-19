package br.com.fiap.beans;

public class Produto {
    // Tipo de dado e atributos
    int codigo;
    String tipo;
    String marca;
    double valor;

    // Métodos Setters (entrada)
    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }
    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public void setMarca(String marca) {
        this.marca = marca;
    }
    public void setValor(double valor) {
        this.valor = valor;
    }

    // Métodos Gatters (retornar / exibir)
    // Alt+Insert
    // Getter and Setter
    // Selecionar todos
    public int getCodigo() {
        return codigo;
    }
    public String getTipo() {
        return tipo;
    }
    public String getMarca() {
        return marca;
    }
    public double getValor() {
        return valor;
    }
}