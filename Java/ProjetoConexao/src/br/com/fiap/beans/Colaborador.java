package br.com.fiap.beans;

public class Colaborador {
    private String nome;
    private String cargo;
    private int idade;
    private double salario;

    public Colaborador() {
    }

    public Colaborador(String nome, String cargo, int idade, double salario) {
        this.nome = nome;
        this.cargo = cargo;
        this.idade = idade;
        this.salario = salario;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCargo() {
        return cargo;
    }
    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }

    public double getSalario() {
        return salario;
    }
    public void setSalario(double salario) {
        this.salario = salario;
    }

    @Override
    public String toString() {
        return "Colaborador" +
                "\nnome='" + nome + '\'' +
                "\ncargo='" + cargo + '\'' +
                "\nidade=" + idade +
                "\nsalario=" + salario;
    }
}
