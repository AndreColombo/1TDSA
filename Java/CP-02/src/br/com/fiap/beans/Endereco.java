package br.com.fiap.beans;

public class Endereco {
    private String logradouro;
    private int numero;
    private String cep;
    private String bairro;
    private String cidade;

    public Endereco() {
    }

    public Endereco(String logradouro, int numero, String cep, String bairro, String cidade) {
        this.logradouro = logradouro;
        this.numero = numero;
        this.cep = cep;
        this.bairro = bairro;
        this.cidade = cidade;
    }

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

    public String getCep() {
        return cep;
    }
    public void setCep(String cep) {
        this.cep = cep;
    }

    public String getBairro() {
        return bairro;
    }
    public void setBairro(String bairro) {
        this.bairro = bairro;
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
                "\ncep: " + cep +
                "\nbairro: " + bairro +
                "\ncidade: " + cidade;
    }
}
