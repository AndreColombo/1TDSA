package br.com.fiap.beans;

public class MediaFinal {
    private double mediaSemestre1;
    private double mediaSemestre2;

    public MediaFinal() {
    }

    public MediaFinal(double mediaSemestre1, double mediaSemestre2) {
        this.mediaSemestre1 = mediaSemestre1;
        this.mediaSemestre2 = mediaSemestre2;
    }

    public double getMediaSemestre1() {
        return mediaSemestre1;
    }
    public void setMediaSemestre1(double mediaSemestre1) {
        this.mediaSemestre1 = mediaSemestre1;
    }

    public double getMediaSemestre2() {
        return mediaSemestre2;
    }
    public void setMediaSemestre2(double mediaSemestre2) {
        this.mediaSemestre2 = mediaSemestre2;
    }

    @Override
    public String toString() {
        return "MediaFinal" +
                "\nmediaSemestre1=" + mediaSemestre1 +
                "\nmediaSemestre2=" + mediaSemestre2 +
                "\nMEDIA FINAL: " + mediaFinal() +
                "\nSTATUS FINAL: " + verificarAprovacao();
    }

    // pontosSemestre1
    public double pontosSemestre1() {
        return mediaSemestre1 * 40 / 100;
    }

    // pontosSemestre2
    public double pontosSemestre2() {
        return mediaSemestre2 * 60 / 100;
    }

    // mediaFinal
    public double mediaFinal() {
        return pontosSemestre1() + pontosSemestre2();
    }

    // calculoAprovacao
    public String verificarAprovacao() {
        String informacao = null;
        if (mediaFinal() >= 6) {
            informacao = "Aeeeê! Fiquei acima da média, PASSEI UHUUL !!!";
        } else {
            informacao = "Eita... fiquei abaixo da média, sniff sniff";
        }

        return informacao;
    }
}