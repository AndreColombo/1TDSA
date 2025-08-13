package br.com.fiap.beans;

public class Aluno {
    private String nome;
    private String rm;
    private String turma;
    private int idade;
    private double nota;

    public Aluno() {
    }

    public Aluno(String nome, String rm, String turma, int idade, double nota) {
        this.nome = nome;
        this.rm = rm;
        this.turma = turma;
        this.idade = idade;
        this.nota = nota;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getRm() {
        return rm;
    }
    public void setRm(String rm) {
        this.rm = rm;
    }

    public String getTurma() {
        return turma;
    }
    public void setTurma(String turma) {
        this.turma = turma;
    }

    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }

    public double getNota() {
        return nota;
    }
    public void setNota(double nota) {
        this.nota = nota;
    }

    @Override
    public String toString() {
        return "Aluno" +
                "\nnome='" + nome + '\'' +
                "\nrm='" + rm + '\'' +
                "\nturma='" + turma + '\'' +
                "\nidade=" + idade +
                "\nnota=" + nota;
    }
}
