package br.com.fiap.beans;

public class Aluno extends Pessoa {
    private String turma;
    private String rm;
    private double nota;

    public Aluno() {
    }

    public Aluno(String nome, int idade, String cpf, String rg, String turma, String rm, double nota) {
        super(nome, idade, cpf, rg);
        this.turma = turma;
        this.rm = rm;
        this.nota = nota;
    }

    public String getTurma() {
        return turma;
    }
    public void setTurma(String turma) {
        this.turma = turma;
    }

    public String getRm() {
        return rm;
    }
    public void setRm(String rm) {
        this.rm = rm;
    }

    public double getNota() {
        return nota;
    }
    public void setNota(double nota) {
        this.nota = nota;
    }

    @Override
    public String toString() {
        return "ALUNO" +
                "\nturma = '" + turma + '\'' +
                "\nrm = '" + rm + '\'' +
                "\nnota = " + nota +
                "\n" + super.toString();
    }
}
