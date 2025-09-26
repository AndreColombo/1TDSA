package br.com.fiap.beans;

public class MediaSemestre {
    private double cp1;
    private double cp2;
    private double sprint1;
    private double sprint2;
    private double gs;

    public MediaSemestre() {
    }

    public MediaSemestre(double cp1, double cp2, double sprint1, double sprint2, double gs) {
        this.cp1 = cp1;
        this.cp2 = cp2;
        this.sprint1 = sprint1;
        this.sprint2 = sprint2;
        this.gs = gs;
    }

    public double getCp1() {
        return cp1;
    }
    public void setCp1(double cp1) {
        this.cp1 = cp1;
    }

    public double getCp2() {
        return cp2;
    }
    public void setCp2(double cp2) {
        this.cp2 = cp2;
    }

    public double getSprint1() {
        return sprint1;
    }
    public void setSprint1(double sprint1) {
        this.sprint1 = sprint1;
    }

    public double getSprint2() {
        return sprint2;
    }
    public void setSprint2(double sprint2) {
        this.sprint2 = sprint2;
    }

    public double getGs() {
        return gs;
    }
    public void setGs(double gs) {
        this.gs = gs;
    }

    @Override
    public String toString() {
        return "MediaSemestre" +
                "\ncp1=" + cp1 +
                "\ncp2=" + cp2 +
                "\nsprint1=" + sprint1 +
                "\nsprint2=" + sprint2 +
                "\ngs=" + gs;
    }

    // MÉTODOS P/ AS CPS

    // calcularMediaCps
    public double calcularMediaCps() {
        double soma = cp1 + cp2;
        return soma / 2;
    }

    // pontosCps
    public double pontosCps() {
        return calcularMediaCps() * 20 / 100;
    }

    // MÉTODOS P/ AS SPRINTS

    // calcularMediaSprints
    public double calcularMediaSprints() {
        double soma = sprint1 + sprint2;
        return soma / 2;
    }

    // pontosSprints
    public double pontosSprints() {
        return calcularMediaSprints() * 20 / 100;
    }

    // CPS + SPRINTS

    //mediaCpsSprints
    public double mediaCpsSprints() {
        double soma = calcularMediaCps() + calcularMediaSprints();
        return soma / 2;
    }

    // pontosCpsSprints
    public double pontosCpsSprints() {
        return pontosCps() + pontosSprints();
    }

    // MÉTODOS P/ A GLOBAL SOLUTION
    public double pontosGs() {
        return gs * 60 / 100;
    }

    // mediaSemestral
    public double mediaSemestral() {
        return pontosGs() + pontosCpsSprints();
    }
}
