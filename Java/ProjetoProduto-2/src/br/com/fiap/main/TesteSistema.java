package br.com.fiap.main;

import br.com.fiap.beans.Produto;

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
    static double real(String j){
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {
        // instanciar objeto
        Produto objProduto = new Produto();

        //
        objProduto.setCodigo(inteiro("Digite o código"));
        objProduto.setTipo(texto("Digite o tipo de produto"));
        objProduto.setMarca(texto("Informe a marca"));
        objProduto.setQuantidade(inteiro("Informe a quantidade"));
        objProduto.setValor(real("Informe o valor"));

        System.out.println(objProduto);
    }
}
