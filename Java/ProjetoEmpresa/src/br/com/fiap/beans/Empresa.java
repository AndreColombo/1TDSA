package br.com.fiap.beans;

public class Empresa {
    private String cnpj;
    private String razaoSocial;
    private String nomeFantasia;
    private String segmento;
    private Endereco endereco;

    // metodo construtor com parâmentro vazio
    public Empresa() {
    }

    // metodo construtor com parâmentro cheio
    public Empresa(String cnpj, String razaoSocial, String nomeFantasia, String segmento) {
        this.cnpj = cnpj;
        this.razaoSocial = razaoSocial;
        this.nomeFantasia = nomeFantasia;
        this.segmento = segmento;
    }

    // getters e setters
    public String getCnpj() {
        return cnpj;
    }
    public void setCnpj(String cnpj) {
        this.cnpj = cnpj;
    }

    public String getRazaoSocial() {
        return razaoSocial;
    }
    public void setRazaoSocial(String razaoSocial) {
        this.razaoSocial = razaoSocial;
    }

    public String getNomeFantasia() {
        return nomeFantasia;
    }
    public void setNomeFantasia(String nomeFantasia) {
        this.nomeFantasia = nomeFantasia;
    }

    public String getSegmento() {
        return segmento;
    }
    public void setSegmento(String segmento) {
        this.segmento = segmento;
    }

    public Endereco getEndereco() {
        return endereco;
    }
    public void setEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    @Override
    public String toString() {
        return "\n\nEMPRESA:" +
                "\ncnpj: " + cnpj +
                "\nrazaoSocial: " + razaoSocial +
                "\nnomeFantasia: " + nomeFantasia +
                "\nsegmento: " + segmento +
                "\nENDEREÇO: " + endereco;
    }
}
