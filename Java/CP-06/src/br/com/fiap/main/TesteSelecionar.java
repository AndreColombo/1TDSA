package br.com.fiap.main;

import br.com.fiap.beans.Carro;
import br.com.fiap.dao.CarroDAO;

import java.sql.SQLException;
import java.util.List;

public class TesteSelecionar {
    public static void main(String[] args) throws SQLException, ClassNotFoundException {
        // Instanciar objeto
        CarroDAO objCarroDAO = new CarroDAO();

        List<Carro> listaCarros = objCarroDAO.selecionar();

        if (listaCarros != null) {
            // foreache
            for (Carro carro : listaCarros) {
                System.out.println(
                        carro.getCodigo() + " " + carro.getMarca() + " " + carro.getModelo() + " " + carro.getAno() + " " + carro.getValor() + " \n");
            }
        }
    }
}