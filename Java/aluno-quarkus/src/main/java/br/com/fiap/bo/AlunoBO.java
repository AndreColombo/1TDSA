package br.com.fiap.bo;

import br.com.fiap.beans.Aluno;
import br.com.fiap.dao.AlunoDAO;

import java.sql.SQLException;
import java.util.ArrayList;

public class AlunoBO {
    AlunoDAO alunoDAO;

    // Selecionar
    public ArrayList<Aluno> selecionarB0() throws SQLException, ClassNotFoundException {
        alunoDAO = new AlunoDAO();

        // Regra de negócios

        return (ArrayList<Aluno>) alunoDAO.selecionar();
    }

    // Inserir
    public void inserirBo(Aluno aluno) throws SQLException, ClassNotFoundException {
        AlunoDAO alunoDAO = new AlunoDAO();

        // Regra de negócios

        alunoDAO.inserir(aluno);
    }

    // Atualizar
    public void atualizarBo(Aluno aluno) throws SQLException, ClassNotFoundException {
        AlunoDAO alunoDAO = new AlunoDAO();

        // Regra de negócios

        alunoDAO.atualizar(aluno);
    }

    // Deletar
    public void deletarBo(int rm) throws SQLException, ClassNotFoundException {
        AlunoDAO alunoDAO = new AlunoDAO();

        // Regra de negócios

        alunoDAO.deletar(rm);
    }
}
