package br.com.fiap.main;

import br.com.fiap.beans.Cliente;

import javax.swing.*;

public class TesteSistema {
    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    static int inteiro(String j) {
        return Integer.parseInt(JOptionPane.showInputDialog(j));
    }

    static double real(String j) {
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {
        // Instanciar objetos
        Cliente objCliente = new Cliente();

        // Entrada
        objCliente.setNome(texto("Nome:"));
        objCliente.setCpf(texto("CPF:"));
        objCliente.setNumeroCelular(texto("Celular:"));
        objCliente.setIdade(inteiro("Idade:"));
        objCliente.setRenda(real("Renda:"));

        // Saídas
        System.out.println(objCliente);
    }
}
