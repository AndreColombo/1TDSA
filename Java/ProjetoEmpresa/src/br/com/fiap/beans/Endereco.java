package br.com.fiap.beans;

public class Endereco {
    private String logradouro;
    private int numero;
    private String bairro;
    private String cep;
    private String cidade;

    // metodo construtor com parâmentro vazio
    public Endereco() {
    }

    // metodo construtor com parâmentro cheio
    public Endereco(String logradouro, int numero, String bairro, String cep, String cidade) {
        this.logradouro = logradouro;
        this.numero = numero;
        this.bairro = bairro;
        this.cep = cep;
        this.cidade = cidade;
    }

    // getters e setters
    public String getLogradouro() {
        return logradouro;
    }
    public void setLogradouro(String logradouro) {
        this.logradouro = logradouro;
    }

    public int getNumero() {
        return numero;
    }
    public void setNumero(int numero) {
        this.numero = numero;
    }

    public String getBairro() {
        return bairro;
    }
    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    public String getCep() {
        return cep;
    }
    public void setCep(String cep) {
        this.cep = cep;
    }

    public String getCidade() {
        return cidade;
    }
    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    @Override
    public String toString() {
        return "\nlogradouro: " + logradouro +
                "\nnumero: " + numero +
                "\nbairro: " + bairro +
                "\ncep: " + cep +
                "\ncidade: " + cidade;
    }
}
