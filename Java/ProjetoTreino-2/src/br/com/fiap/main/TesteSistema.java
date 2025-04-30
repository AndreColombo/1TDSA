package br.com.fiap.main;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Produto;
import br.com.fiap.beans.Endereco;

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
        Cliente objCliente = new Cliente(
                texto("Informe o CPF do cliente: "),
                texto("Informe o Nome: "),
                inteiro("Informe a idade: "),
                texto("Profissão: "),
                real("Renda: ")
        );
        Endereco objEndereco = new Endereco(
                texto("Informe o logradouro do endereço do cliente: "),
                inteiro("Número do endereço: "),
                texto("CEP: "),
                texto("Bairro: "),
                texto("Cidade: ")
        );

        objCliente.setEndereco(objEndereco);

        Produto objProduto = new Produto(
                inteiro("Informe o código do produto: "),
                texto("Informe o tipo do produto: "),
                texto("Marca: "),
                inteiro("Quantidade: "),
                real("Valor: ")
        );

        System.out.println(objCliente + "" + objProduto);
    }
}
