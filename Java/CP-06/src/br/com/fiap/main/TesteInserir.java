package br.com.fiap.main;

import br.com.fiap.beans.Carro;
import br.com.fiap.dao.CarroDAO;

import javax.swing.*;
import java.sql.SQLException;

public class TesteInserir {
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
        // Instanciar objetos
        CarroDAO carroDAO = new CarroDAO();

        Carro objCarro = new Carro();

        objCarro.setCodigo(inteiro("Informe o Código do carro"));
        objCarro.setMarca(texto("Marca"));
        objCarro.setModelo(texto("Modelo"));
        objCarro.setAno(inteiro("Ano"));
        objCarro.setValor(real("Valor"));

        System.out.println(carroDAO.inserir(objCarro));
    }
}