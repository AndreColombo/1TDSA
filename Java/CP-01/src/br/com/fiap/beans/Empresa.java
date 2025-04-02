package br.com.fiap.beans;

public class Empresa {
    private String cnpj;
    private String razaoSocial;
    private String nomeFantasia;
    private String segmento;

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
