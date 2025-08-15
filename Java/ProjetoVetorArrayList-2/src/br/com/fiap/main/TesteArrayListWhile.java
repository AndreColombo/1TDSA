package br.com.fiap.main;

import br.com.fiap.beans.Aluno;

import javax.swing.*;
import java.util.ArrayList;

public class TesteArrayListWhile {
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
        // Preparar a lista
        ArrayList<Aluno> listaAlunos = new ArrayList<Aluno>();

        // Preparar o objeto
        Aluno objAluno = null;

        // Laço de repetição         while
        //                           enquanto / faça

        int condicao = 0;

        while (condicao == 0) {
            objAluno = new Aluno();
            objAluno.setNome(texto("Nome:"));
            objAluno.setRm(texto("RM:"));
            objAluno.setTurma(texto("Turma:"));
            objAluno.setIdade(inteiro("Idade:"));
            objAluno.setNota(real("Nota:"));

            listaAlunos.add(objAluno);

            condicao = JOptionPane.showConfirmDialog(null, "Cadastrar mais alunos(as)?", "CADASTRO DE ALUNOS", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
        }

        // Saídas utilizando o foreach para varrer todas as entradas
        for (Aluno a : listaAlunos) {
            System.out.println("\n\nNome: " + a.getNome() + "\nRM: " + a.getRm() + "\nTurma: " + a.getTurma() + "\nIdade: " + a.getIdade() + "\nNota: " + a.getNota());

        }
    }
}
