package br.com.fiap.main;

import br.com.fiap.beans.Carro;
import br.com.fiap.dao.CarroDAO;

import javax.swing.*;
import java.sql.SQLException;

public class TesteDeletar {
    // int
    static int inteiro(String j) {
        return Integer.parseInt(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) throws SQLException, ClassNotFoundException {
        CarroDAO carroDAO = new CarroDAO();

        Carro objCarro = new Carro();

        objCarro.setCodigo(inteiro("Informe o Código do carro para ser deletado"));

        System.out.println(carroDAO.deletar(objCarro.getCodigo()));
    }
}