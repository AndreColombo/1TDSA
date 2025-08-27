package br.com.fiap.main;

import br.com.fiap.beans.Carro;

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
        Carro[] vetorCarro = new Carro[3];

        int indice = 0;

        do {
            vetorCarro[indice] = new Carro();
            vetorCarro[indice].setMarca(texto("Marca:"));
            vetorCarro[indice].setModelo(texto("Modelo:"));
            vetorCarro[indice].setDescricao(texto("Descrição:"));
            vetorCarro[indice].setAno(inteiro("Ano:"));
            vetorCarro[indice].setValor(real("Valor:"));

            indice++;
        } while (JOptionPane.showConfirmDialog(null, "Adicionar mais produtos?", "CARRINHO DE COMPRAS", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE) == 0);

        for (int buscar = 0; buscar < indice; buscar++) {
            System.out.println("\nMarca: " + vetorCarro[buscar].getMarca() + "\nModelo: " + vetorCarro[buscar].getModelo() + "\nDescrição: " + vetorCarro[buscar].getDescricao() + "\nAno: " + vetorCarro[buscar].getAno() + "\nValor: " + vetorCarro[buscar].getValor());
        }

    }
}