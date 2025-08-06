package br.com.fiap.main;

import br.com.fiap.beans.Cliente;

import javax.swing.*;

public class TesteSistemaVetor {
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
        // Determinar a quantidade máxima de vetores
        Cliente[] vetorCiente = new Cliente[3];
        // Indice para controlar as posições
        int indice = 0;
    }
}
