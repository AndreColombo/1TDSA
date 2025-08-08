package br.com.fiap.main;

import br.com.fiap.beans.Cliente;

import javax.swing.*;

public class TesteSistema {
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

    public static void main(String[] args) {
        // instanciar objeto
        Cliente objCliente = new Cliente();

        // Entradas
        objCliente.setNome(texto("Nome"));
        objCliente.setCpf(texto("CPF"));
        objCliente.setNumeroCelular(texto("Numero de celular"));
        objCliente.setIdade(inteiro("Idade"));
        objCliente.setRenda(real("Renda"));

        // Saidas
        System.out.println(objCliente);
    }
}
