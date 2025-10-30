package br.com.fiap.main;

import br.com.fiap.factory.ConnectionFactory;
import br.com.fiap.excecoes.ExcecoesConexao;

import java.sql.Connection;
import java.sql.SQLException;

public class TesteConexao {

    public static void main(String[] args) throws ExcecoesConexao, SQLException, ClassNotFoundException {

        Connection cn = null;

        try {
           cn = new ConnectionFactory().conexao();
            System.out.println("Conectado com o banco de dados");
        } catch ( Exception e) {
            throw new ExcecoesConexao(e);
        }   finally {
            System.out.println("OK");
            cn.close();
        }

    }

}
