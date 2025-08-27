package br.com.fiap.main;

import br.com.fiap.beans.Carro;

import javax.swing.*;
import java.util.ArrayList;

public class TesteArrayList {
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
        ArrayList<Carro> listaCarro = new ArrayList<Carro>();

        Carro objCarro = null;

        do {
            objCarro = new Carro();
            objCarro.setMarca(texto("Marca:"));
            objCarro.setModelo(texto("Modelo:"));
            objCarro.setDescricao(texto("Descrição:"));
            objCarro.setAno(inteiro("Ano:"));
            objCarro.setValor(real("Valor:"));

            listaCarro.add(objCarro);
        } while (JOptionPane.showConfirmDialog(null, "Adicionar mais produtos?", "CARRINHO DE COMPRAS", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE) == 0);

        for (Carro p : listaCarro) {
            System.out.println("\nMarca: " + p.getMarca() + "\nModelo: " + p.getModelo() + "\nDescrição: " + p.getDescricao() + "\nAno: " + p.getAno() + "\nValor: " + p.getValor());
        }

    }
}