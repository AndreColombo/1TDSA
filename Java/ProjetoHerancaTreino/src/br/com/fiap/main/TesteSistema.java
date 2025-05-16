package br.com.fiap.main;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Colaborador;
import br.com.fiap.beans.Endereco;

import javax.swing.*;

public class TesteSistema {
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
        // instanciar objetos

        // String nome, int idade, String cpf, String rg, double renda, String status
        Cliente objCliente = new Cliente(
                texto("Informe o nome do cliente"),
                inteiro("Informe a idade do cliente"),
                texto("Informe o CPF do cliente"),
                texto("Informe o RG do cliente"),
                real("Informe a renda do cliente"),
                texto("Informe o status do cliente")
        );

        // String logradouro, int numero, String cep, String complemento, String bairro, String cidade
        Endereco objEnderecoCliente = new Endereco(
                texto("Endereço do cliente: Logradouro"),
                inteiro("Número"),
                texto("Complemento"),
                texto("CEP"),
                texto("Bairro"),
                texto("Cidade")
        );

        objCliente.setEndereco(objEnderecoCliente);

        // String nome, int idade, String cpf, String rg, double renda, int numeroCracha
        Colaborador objColaborador = new Colaborador(
                texto("Informe o nome do colaborador"),
                inteiro("Informe a idade do colaborador"),
                texto("Informe o CPF"),
                texto("Informe o RG"),
                real("Informe o salário"),
                inteiro("Informe o numero do cracha do colaborador")
        );

        // String logradouro, int numero, String cep, String complemento, String bairro, String cidade
        Endereco objEnderecoColaborador = new Endereco(
                texto("Endereço do colaborador: Logradouro"),
                inteiro("Número"),
                texto("Complemento"),
                texto("CEP"),
                texto("Bairro"),
                texto("Cidade")
        );

        objColaborador.setEndereco(objEnderecoColaborador);

        System.out.println(objCliente + " " + objCliente.getEndereco() + " " + objColaborador + " " + objCliente.getEndereco());
    }
}
