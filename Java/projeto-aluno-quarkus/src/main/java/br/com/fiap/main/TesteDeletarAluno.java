package br.com.fiap.main;

import br.com.fiap.beans.Aluno;
import br.com.fiap.dao.AlunoDAO;

import javax.swing.*;
import java.sql.SQLException;

public class TesteDeletarAluno {

    // int
    static int inteiro(String j) {
        return Integer.parseInt(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) throws SQLException, ClassNotFoundException {

        Aluno objAluno = new Aluno();

        AlunoDAO objAlunoDao = new AlunoDAO();

        objAluno.setRm(inteiro("Informe o RM do aluno a ser deletado"));

        System.out.println(objAlunoDao.deletar(objAluno.getRm()));

    }
}
