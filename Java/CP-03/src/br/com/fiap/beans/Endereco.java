package br.com.fiap.beans;

public class Endereco {
    private String logradouro;
    private int numero;
    private String complemento;
    private String bairro;
    private String cidade;
    private String cep;

    public Endereco() {
    }

    public Endereco(String logradouro, int numero, String complemento, String bairro, String cidade, String cep) {
        this.logradouro = logradouro;
        this.numero = numero;
        this.complemento = complemento;
        this.bairro = bairro;
        this.cidade = cidade;
        this.cep = cep;
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

    public String getComplemento() {
        return complemento;
    }
    public void setComplemento(String complemento) {
        this.complemento = complemento;
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

    public String getCep() {
        return cep;
    }
    public void setCep(String cep) {
        this.cep = cep;
    }

    @Override
    public String toString() {
        return "ENDEREÇO" +
                "\nlogradouro = '" + logradouro + '\'' +
                "\nnumero = " + numero +
                "\ncomplemento = '" + complemento + '\'' +
                "\nbairro = '" + bairro + '\'' +
                "\ncidade = '" + cidade + '\'' +
                "\ncep = '" + cep + '\'';
    }
}
