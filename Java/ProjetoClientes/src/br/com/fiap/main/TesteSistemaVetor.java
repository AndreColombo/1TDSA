package br.com.fiap.main;

import br.com.fiap.beans.Cliente;

import javax.swing.*;

public class TesteSistemaVetor {
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
        // Determinar a quantidade máxima de posições / vetores
        Cliente[] vetorCliente = new Cliente[3]; // [0] [1] [2]

        // índice para controlar as posições
        int indice = 0;

        // laço de repetição para as entradas
        // do / while ------ faça / enquanto
        do {
            vetorCliente[indice] = new Cliente();
            vetorCliente[indice].setNome(texto("Nome"));
            vetorCliente[indice].setCpf(texto("CPF"));
            vetorCliente[indice].setNumeroCelular(texto("Celular"));
            vetorCliente[indice].setIdade(inteiro("Idade"));
            vetorCliente[indice].setRenda(real("Renda"));

            indice++;
        } while (
                JOptionPane.showConfirmDialog(
                        null, "Cadastrar mais clientes?", "CADASTRO DE CLIENTES", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE)
                        == 0);

        // Saídas utilizando o for
        for (int buscar = 0; buscar < indice; buscar++) {
            System.out.println(
                    "\n\nNome: " + vetorCliente[buscar].getNome() +
                    "\nCPF: " + vetorCliente[buscar].getCpf() +
                    "\nNúmero de Celular: " + vetorCliente[buscar].getNumeroCelular() +
                    "\nIdade: " + vetorCliente[buscar].getIdade() +
                    "\nRenda: " + vetorCliente[buscar].getRenda()
            );
        }
    }
}
