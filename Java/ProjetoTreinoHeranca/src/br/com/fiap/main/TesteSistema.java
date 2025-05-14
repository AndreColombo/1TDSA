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

    // int
    static int inteiro(String j) {
        return Integer.parseInt(JOptionPane.showInputDialog(j));
    }

    // double
    static double real(String j) {
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {
        // instanciar objetos

        // String nome, int idade, String cpf, String rg, double renda, String status
        Cliente objCliente = new Cliente(
                texto("Nome do cliente"),
                inteiro("Idade do cliente"),
                texto("CPF do cliente"),
                texto("RG do cliente"),
                real("Renda do cliente"),
                texto("Status do cliente")
        );

        // String logradouro, int numero, String cep, String bairro, String cidade
        Endereco objEndereco = new Endereco(
                texto("Logradouro"),
                inteiro("Número"),
                texto("CEP"),
                texto("Bairro"),
                texto("Cidade")
        );

        objCliente.setEndereco(objEndereco);

        // String nome, int idade, String cpf, String rg, double renda, int numeroCracha
        Colaborador objColaborador = new Colaborador(
                texto("Nome do colaborador"),
                inteiro("Idade do colaborador"),
                texto("CPF do colaborador"),
                texto("RG do colaborador"),
                real("Renda do colaborador"),
                inteiro("Número de Crachá")
        );

        System.out.println(objCliente + "" + objColaborador);

        System.out.println("\n\n\n" + objCliente.identificador() +
                "\n" + objColaborador.identificador()
        );
    }
}
