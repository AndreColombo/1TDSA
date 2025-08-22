package br.com.fiap.main;

import br.com.fiap.beans.Produto;

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
        ArrayList<Produto> listaProduto = new ArrayList<Produto>();

        Produto objProduto = null;

        do {
            // Entrada para adicionar Produto
            objProduto = new Produto();
            objProduto.setCodigo(inteiro("Código"));
            objProduto.setTipo(texto("Tipo:"));
            objProduto.setMarca(texto("Marca:"));
            objProduto.setDescricao(texto("Descrição:"));
            objProduto.setValor(real("Valor:"));

            listaProduto.add(objProduto);
        } while (JOptionPane.showConfirmDialog(null, "Adicionar mais produtos no carrinho de compras?", "CARRINHO DE COMPRAS", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE) == 0);

        // Saídas utilizando o foreach
        for (Produto p : listaProduto) {
            System.out.println("\nCódigo: " + p.getCodigo() + "\nTipo: " + p.getTipo() + "\nMarca: " + p.getMarca() + "\nDescrição: " + p.getDescricao() + "\nValor: " + p.getValor());
        }
    }
}
