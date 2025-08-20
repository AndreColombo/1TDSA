package br.com.fiap.main;

import br.com.fiap.beans.Produto;

import javax.swing.*;

public class TesteVetor {
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
        // Preparar a quantidade máxima de vetores
        Produto[] vetorProduto = new Produto[3]; // [0] [1] [2]

        // Preparar indice
        int indice = 0;

        // Laçp de Repetição      do   / while
        //                        faça / enquanto
        do {
            // Entradas
            vetorProduto[indice] = new Produto();
            vetorProduto[indice].setCodigo(inteiro("Código:"));
            vetorProduto[indice].setTipo(texto("Tipo:"));
            vetorProduto[indice].setMarca(texto("Marca:"));
            vetorProduto[indice].setDescricao(texto("Descrição:"));
            vetorProduto[indice].setValor(real("Valor:"));

            indice++;
        } while (JOptionPane.showConfirmDialog(null, "Adicionar mais produtos?", "CARRINHO DE COMPRAS", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE) == 0);

        // Saídas utilizando for
        for (int buscar = 0; buscar < indice; buscar++) {
            System.out.println("\nCódigo: " + vetorProduto[buscar].getCodigo() + "\nTipo: " + vetorProduto[buscar].getTipo() + "\nMarca: " + vetorProduto[buscar].getMarca() + "\nDescrição: " + vetorProduto[buscar].getDescricao() + "\nValor: " + vetorProduto[buscar].getValor());
        }

    }
}
