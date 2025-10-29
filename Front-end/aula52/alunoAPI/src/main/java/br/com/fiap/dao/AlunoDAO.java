package br.com.fiap.dao;

import br.com.fiap.beans.Aluno;
import br.com.fiap.factory.ConnectionFactory;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class AlunoDAO {

    public Connection minhaConexao;

    // metodo construtor com parâmetro vazio
    public AlunoDAO() throws SQLException, ClassNotFoundException {
        super();
        this.minhaConexao = new ConnectionFactory().conexao();
    }

    // Insert
    public String inserir(Aluno aluno) throws SQLException {
        PreparedStatement stmt = minhaConexao.prepareStatement
                ("Insert into T_FIAP_ALUNO (nome, rm, turma, nota) values (?, ?, ?, ?)");
        stmt.setString(1, aluno.getNome());
        stmt.setInt(2, aluno.getRm());
        stmt.setString(3, aluno.getTurma());
        stmt.setDouble(4, aluno.getNota());

        stmt.execute();
        stmt.close();

        return "Aluno cadastrado com sucesso!";
    }

    // Delete
    public String deletar(int id) throws SQLException {
        PreparedStatement stmt = minhaConexao.prepareStatement
                ("Delete from T_FIAP_ALUNO where ID = ?");
        stmt.setInt(1, id);

        stmt.execute();
        stmt.close();

        return  "Aluno deletado com sucesso!";
    }

    // UpDate
    public String atualizar(Aluno aluno) throws SQLException {
        PreparedStatement stmt = minhaConexao.prepareStatement
    ("Update T_FIAP_ALUNO set NOME = ?, TURMA = ?, NOTA = ?, RM = ?  where ID = ?");
        stmt.setString(1, aluno.getNome());
        stmt.setString(2, aluno.getTurma());
        stmt.setDouble(3, aluno.getNota());
        stmt.setInt(4, aluno.getRm());
        stmt.setInt(5, aluno.getId());

        stmt.executeUpdate();
        stmt.close();

        return "Aluno atualizado com sucesso!";
    }

    // Select
    public List<Aluno> selecionar() throws SQLException {
        List<Aluno> listaAlunos = new ArrayList<Aluno>();
        PreparedStatement stmt = minhaConexao.prepareStatement
                ("select * from T_FIAP_ALUNO order by  Nome");
        ResultSet rs = stmt.executeQuery();

        while(rs.next()){
            Aluno aluno = new Aluno();
            aluno.setId(rs.getInt(1));
            aluno.setNome(rs.getString(2));
            aluno.setRm(rs.getInt(3));
            aluno.setTurma(rs.getString(4));
            aluno.setNota(rs.getDouble(5));
            listaAlunos.add(aluno);
        }
        return listaAlunos;
    }


}
