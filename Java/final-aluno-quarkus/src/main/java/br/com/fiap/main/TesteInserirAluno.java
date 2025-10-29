package br.com.fiap.main;

import br.com.fiap.beans.Aluno;
import br.com.fiap.dao.AlunoDAO;

import javax.swing.*;
import java.sql.SQLException;

public class TesteInserirAluno {

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

    public static void main(String[] args) throws SQLException, ClassNotFoundException {

        Aluno objAluno = new Aluno();

        AlunoDAO objAlunoDao = new AlunoDAO();

        objAluno.setRm(inteiro("Informe o RM do Aluno"));
        objAluno.setNome(texto("Informe o Nome do Aluno"));
        objAluno.setTurma(texto("Informe a Turma do Aluno"));
        objAluno.setNota(real("Informe a Nota do Aluno"));

        System.out.println(objAlunoDao.inserir(objAluno));

    }

}
