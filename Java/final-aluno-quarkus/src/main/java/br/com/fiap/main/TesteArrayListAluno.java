package br.com.fiap.main;

import br.com.fiap.beans.Aluno;

import javax.swing.*;
import java.util.ArrayList;

public class TesteArrayListAluno {

    // String
    static String texto(String j){
        return JOptionPane.showInputDialog(j);
    }

    // int
    static int inteiro(String j){
        return Integer.parseInt(JOptionPane.showInputDialog(j));
    }

    // double
    static double real(String j){
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {

        // Preparar a lista de alunos
        ArrayList<Aluno> listaAlunos = new ArrayList<Aluno>();

        // Preparar objeto null
        Aluno objAluno = null;

        // Laço de repetição (entradas)
        do {

            objAluno = new Aluno();
            objAluno.setRm(inteiro("RM do aluno"));
            objAluno.setNome(texto("Nome do aluno"));
            objAluno.setTurma(texto("Turma do aluno"));
            objAluno.setNota(real("Nota do aluno"));

            listaAlunos.add(objAluno);

        }while( JOptionPane.showConfirmDialog(null,
                "Cadastrar mais aluno?",
                "CADASTRO DE ALUNOS",
                JOptionPane.YES_NO_OPTION,
                JOptionPane.QUESTION_MESSAGE )  == 0);

        // Saidas utilizando o foreach
        for(Aluno a : listaAlunos){
            System.out.println(
                    "\n\nRM: " + a.getRm() +
                    "\nNome: " + a.getNome() +
                    "\nTurma: " + a.getTurma() +
                    "\nNota: " + a.getNota()
            );
        }

    }



}
