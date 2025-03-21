package br.com.fiap.beans;

public class Cliente {
    // Visibilidade, tipo de dados e atributos
    private int idade;
    private String nome;
    private String email;
    private double renda;

    // Setters (entrada) e Getters (retornar \ exibir)
    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }

    public double getRenda() {
        return renda;
    }
    public void setRenda(double renda) {
        this.renda = renda;
    }
}
