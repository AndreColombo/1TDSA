package br.com.fiap.dao;

import br.com.fiap.beans.Carro;
import br.com.fiap.conexoes.ConexaoFactory;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class CarroDAO {
    public Connection minhaConexao;

    public CarroDAO() throws SQLException, ClassNotFoundException {
        this.minhaConexao = new ConexaoFactory().conexao();
    }

    // insert
    public String inserir(Carro carro) throws SQLException {
        PreparedStatement stmt = minhaConexao.prepareStatement("INSERT INTO FIAP_CARRO values(?,?,?,?,?,)");
        stmt.setInt(1, carro.getCodigo());
        stmt.setString(2, carro.getMarca());
        stmt.setString(3, carro.getModelo());
        stmt.setInt(4, carro.getAno());
        stmt.setDouble(5, carro.getValor());

        stmt.execute();
        stmt.close();

        return "Carro cadastrado com sucesso";
    }

    // Deletar
    public String deletar(int codigo) throws SQLException {
        PreparedStatement stmt = minhaConexao.prepareStatement("DELETE FROM FIAP_CARRO where CODIGO = ?");
        stmt.setInt(1, codigo);

        stmt.execute();
        stmt.close();

        return "Carro deletado com sucesso!";
    }

    // Atualizar
    public String atualizar(Carro carro) throws SQLException {
        PreparedStatement stmt = minhaConexao.prepareStatement
                ("UPDATE FIAP_CARRO set MARCA = ?, MODELO = ?, ANO = ?, VALOR = ?  where CODIGO = ?");
        stmt.setInt(1, carro.getCodigo());
        stmt.setString(2, carro.getMarca());
        stmt.setString(3, carro.getModelo());
        stmt.setInt(4, carro.getAno());
        stmt.setDouble(5, carro.getValor());

        stmt.executeUpdate();
        stmt.close();

        return "Carro atualizado com sucesso!";
    }

    // Selecionar
    public List<Carro> selecionar() throws SQLException {
        List<Carro> listaCarro = new ArrayList<Carro>();
        PreparedStatement stmt = minhaConexao.prepareStatement("SELECT * FROM FIAP_CARRO");

        ResultSet rs = stmt.executeQuery();

        while (rs.next()){
            Carro objCarro = new Carro();
            objCarro.setCodigo(rs.getInt(1));
            objCarro.setMarca(rs.getString(2));
            objCarro.setModelo(rs.getString(3));
            objCarro.setAno(rs.getInt(4));
            objCarro.setValor(rs.getDouble(5));
            listaCarro.add(objCarro);
        }

        return listaCarro;
    }
}
