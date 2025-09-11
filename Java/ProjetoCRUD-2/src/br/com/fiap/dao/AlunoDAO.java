package br.com.fiap.dao;

import br.com.fiap.beans.Aluno;
import br.com.fiap.conexoes.ConexaoFactory;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class AlunoDAO {
    public Connection minhaConexao;

    public AlunoDAO() throws SQLException, ClassNotFoundException {
        this.minhaConexao = new ConexaoFactory().conexao();
    }

    // Insert
    public String inserir(Aluno aluno) throws SQLException {
        PreparedStatement stmt = minhaConexao.prepareStatement
                ("Insert into T_FIAP_ALUNO values (?, ?, ?, ?)");
        stmt.setInt(1, aluno.getRm());
        stmt.setString(2, aluno.getNome());
        stmt.setString(3, aluno.getTurma());
        stmt.setDouble(4, aluno.getNota());

        stmt.execute();
        stmt.close();

        return "Aluno cadastrado com sucesso!";
    }

    // Delete
    public String deletar(int rm) throws SQLException {
        PreparedStatement stmt = minhaConexao.prepareStatement
                ("Delete from T_FIAP_ALUNO where RM = ?");
        stmt.setInt(1, rm);

        stmt.execute();
        stmt.close();

        return "Aluno deletado com sucesso!";
    }

    // Update
    public String atualizar(Aluno aluno) throws SQLException {
        PreparedStatement stmt = minhaConexao.prepareStatement
                ("Insert into T_FIAP_ALUNO values (?, ?, ?, ?)");
        stmt.setInt(1, aluno.getRm());
        stmt.setString(2, aluno.getNome());
        stmt.setString(3, aluno.getTurma());
        stmt.setDouble(4, aluno.getNota());

        stmt.executeUpdate();
        stmt.close();

        return "Aluno deletado com sucesso!";
    }
}
