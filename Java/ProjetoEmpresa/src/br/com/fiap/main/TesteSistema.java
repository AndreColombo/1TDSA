package br.com.fiap.main;

import br.com.fiap.beans.Empresa;
import br.com.fiap.beans.Endereco;
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
        // Instanciar objetos
        Produto objProduto = new Produto(
                inteiro("Informe o código do produto: "),
                texto("Informe o tipo de produto: "),
                texto("Informe a marca: "),
                inteiro("Informe a quantidade disponível: "),
                real("Informe o valor do produto: ")
        );
        Empresa objEmpresa = new Empresa(
                texto("Informe o CNPJ da empresa: "),
                texto("Informe a Razão Social da empresa: "),
                texto("Informe o Nome Fansatia da empresa: "),
                texto("Informe o Segmento da empresa: ")
        );
        Endereco objEndereco = new Endereco(
                texto("ENDEREÇO: Informe o logradouro: "),
                inteiro("Informe o número: "),
                texto("Informe o bairro: "),
                texto("Informe o CEP: "),
                texto("Informe o cidade: ")
        );

        objEmpresa.setEndereco(objEndereco);

        System.out.println(objProduto + "" + objEmpresa);
    }
}
