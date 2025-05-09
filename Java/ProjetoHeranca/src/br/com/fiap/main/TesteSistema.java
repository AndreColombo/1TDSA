package br.com.fiap.main;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Colaborador;
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
        // instanciar objetos

        // String nome, String cpf, String rg, int idade, double renda, String status
        Cliente objCliente = new Cliente(
                texto("Nome do cliente"),
                texto("CPF do cliente"),
                texto("RG do cliente"),
                inteiro("Idade do cliente"),
                real("Renda do cliente"),
                texto("Status")
        );

        // String logradouro, int numero, String complemento, String cep, String bairro, String cidade
        Endereco objEndereco = new Endereco(
                texto("Endereço do cliente: Logradouro"),
                inteiro("Número"),
                texto("Complemento"),
                texto("CEP"),
                texto("Bairro"),
                texto("Cidade")
        );

        objCliente.setEndereco(objEndereco);

        // String nome, String cpf, String rg, int idade, double renda, int numeroCracha
        Colaborador objColaborador = new Colaborador(
                texto("Nome do colaborador"),
                texto("CPF do colaborador"),
                texto("RG do colaborador"),
                inteiro("Idade do colaborador"),
                real("Salário do colaborador"),
                inteiro("Informe o número do crachá do colaborador")
        );

        // saída
        System.out.println(objCliente + "" + objColaborador);
    }
}
