package br.com.fiap.beans;

public class MediaFinal {
    private double madiaSemestre1;
    private double madiaSemestre2;

    public MediaFinal() {
    }

    public MediaFinal(double madiaSemestre1, double madiaSemestre2) {
        this.madiaSemestre1 = madiaSemestre1;
        this.madiaSemestre2 = madiaSemestre2;
    }

    public double getMadiaSemestre1() {
        return madiaSemestre1;
    }
    public void setMadiaSemestre1(double madiaSemestre1) {
        this.madiaSemestre1 = madiaSemestre1;
    }

    public double getMadiaSemestre2() {
        return madiaSemestre2;
    }
    public void setMadiaSemestre2(double madiaSemestre2) {
        this.madiaSemestre2 = madiaSemestre2;
    }

    @Override
    public String toString() {
        return "MediaFinal" +
                "\nmadiaSemestre1=" + madiaSemestre1 +
                "\nmadiaSemestre2=" + madiaSemestre2;
    }
}