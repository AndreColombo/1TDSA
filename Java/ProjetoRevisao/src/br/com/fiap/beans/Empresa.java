package br.com.fiap.beans;

public class Empresa {
    // visibilidade, tipo de dados e atributos
    private String cnpj;
    private String razaoSocial;
    private String nomeFantasia;
    private String segmento;

    // métodos setters (entradas) métodos getters (retornar \ exibir)
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
}
