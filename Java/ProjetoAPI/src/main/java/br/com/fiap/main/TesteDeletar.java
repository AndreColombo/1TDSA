package br.com.fiap.main;

import br.com.fiap.beans.Aluno;
import br.com.fiap.dao.AlunoDAO;

import javax.swing.*;
import java.sql.SQLException;

public class TesteDeletar {

    // int
    static int inteiro(String j){
        return  Integer.parseInt(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) throws SQLException, ClassNotFoundException {

        AlunoDAO alunoDAO = new AlunoDAO();

        Aluno objAluno = new Aluno();

        objAluno.setRm(inteiro("Informe o RM do aluno para ser deletado"));

        System.out.println(alunoDAO.deletar(objAluno.getRm()));



    }
}
