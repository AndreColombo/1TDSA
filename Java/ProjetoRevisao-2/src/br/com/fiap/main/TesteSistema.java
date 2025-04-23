package br.com.fiap.main;

import br.com.fiap.beans.Produto;

import javax.swing.*;

public class TesteSistema {
    // String
    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    // Int
    static int inteiro(String j) {
        return Integer.parseInt(JOptionPane.showInputDialog(j));
    }

    // Double
    static double real(String j) {
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {
        // instanciar objetos
        Produto objProduto = new Produto(
                inteiro("Informe o código do produto: "),
                texto("Digite o tipo de produto: "),
                texto("Digite a marca: "),
                inteiro("Quantidade: "),
                real("Informe o valor do produto: ")
        );

        // entradas
        /*
        objProduto.setCodigo(inteiro("Informe o código do produto: "));
        objProduto.setTipo(texto("Digite o tipo de produto: "));
        objProduto.setMarca(texto("Digite a marca: "));
        objProduto.setQuantidade(inteiro("Quantidade: "));
        objProduto.setValor(real("Informe o valor do produto: "));
         */

        // saídas
        System.out.println(objProduto);
    }
}
