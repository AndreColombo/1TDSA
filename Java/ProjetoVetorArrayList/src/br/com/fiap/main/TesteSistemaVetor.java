package br.com.fiap.main;

import br.com.fiap.beans.Aluno;

import javax.swing.*;

public class TesteSistemaVetor {
    // String
    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    // int
    static int inteiro(String j) {
        return Integer.parseInt(JOptionPane.showInputDialog(j));
    }

    // double
    static double real(String j) {
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {
        // Preparar a quantidade máxima de vetores
        Aluno[] vetorAluno = new Aluno[3];

        // Preparar indice para controlar as posições dos vetores
        int indice = 0;

        // Laço de repetição
        do {
            // Entradas
            vetorAluno[indice] = new Aluno();
            vetorAluno[indice].setNome(texto("Nome:"));
            vetorAluno[indice].setRm(texto("RM:"));
            vetorAluno[indice].setTurma(texto("Turma:"));
            vetorAluno[indice].setIdade(inteiro("Idade:"));
            vetorAluno[indice].setNota(real("Nota:"));

            indice++;
        } while (JOptionPane.showConfirmDialog(null, "Cadastrar mais alunos(as)?", "CADASTRO DE ALUNOS", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE) == 0);

        // Saídas utilizando for
        for (int buscar = 0; buscar < indice; buscar++) {
            System.out.println("\n\nNome: " + vetorAluno[buscar].getNome() + "\nRM: " + vetorAluno[buscar].getRm() + "\nTurma: " + vetorAluno[buscar].getTurma() + "\nIdade: " + vetorAluno[buscar].getIdade() + "\nNota: " + vetorAluno[buscar].getNota());

        }
    }
}
