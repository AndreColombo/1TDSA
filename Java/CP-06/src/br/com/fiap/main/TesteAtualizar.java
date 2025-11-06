package br.com.fiap.main;

import br.com.fiap.beans.Carro;
import br.com.fiap.dao.CarroDAO;

import javax.swing.*;
import java.sql.SQLException;

public class TesteAtualizar {
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

    public static void main(String[] args) throws SQLException, ClassNotFoundException, SQLException {
        Carro objCarro = new Carro();

        CarroDAO alunoDao = new CarroDAO();

        objCarro.setCodigo(inteiro("Informe o código do carro a ser atualizado"));
        objCarro.setMarca(texto("Atualize a Marca"));
        objCarro.setModelo(texto("Atualize o Modelo"));
        objCarro.setAno(inteiro("Atualize o Ano"));
        objCarro.setValor(real("Atualize o Valor"));

        System.out.println(alunoDao.atualizar(objCarro));
    }
}